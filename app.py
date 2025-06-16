import streamlit as st
from pathlib import Path
import pandas as pd
from flashcard_generator.ingestion import ingest_input
from flashcard_generator.preprocessing import preprocess_text, chunk_txt
from flashcard_generator.llm_interface import generate_flashcard_from_chunks

st.title("LLM Powered Flashcard generator")
st.markdown("Upload educational content and get q&a flashcards automatically!")


uploaded_file = st.file_uploader("Upload a pdf or txt file",type=["pdf","txt"])
pasted_content = st.text_area("Or paste content manually",height=250)

if uploaded_file and pasted_content.strip():
    st.info("You uploaded a file and entered text — the file will be used.")


desired_total = st.number_input(
    "How many flashcards do you want?",
    min_value=10,
    max_value=20,
    step=1
)

if st.button("Generate Flashcards"):
    if not uploaded_file and not pasted_content.strip():
        st.warning("Please Upload a file or enter text first")
        st.stop()

    with st.spinner("Reading and processing input"):
        try:
            raw_text = ingest_input(file=uploaded_file,raw_text=pasted_content)
        except Exception as e:
            st.error(f"Failed to read input: {e}")
            st.stop()

        cleaned_txt = preprocess_text(raw_text)
        chunks = chunk_txt(cleaned_txt)

        flashcards = []
        desired_total = desired_total
        for chunk in chunks:
            if len(flashcards) >= desired_total:
                break
            remaining = desired_total - len(flashcards) 
            chunk_cards = generate_flashcard_from_chunks(chunk,num_cards=remaining)
            flashcards.extend(chunk_cards)
    
    if flashcards:
        st.success(f"Generated {len(flashcards)} flashcards!")

        for i,d in enumerate(flashcards,1):
            st.markdown(f"**Q{i}:** {d['question']}")
            st.markdown(f"**A{i}:** {d['answer']}")
            st.markdown(f"**Difficulty:** {d['difficulty']}")
            st.markdown("------")
        
        export_df = pd.DataFrame(flashcards)

        st.download_button("Download as CSV",export_df.to_csv(index=False),"flashcards.csv","text/csv")

        st.download_button("Download as JSON",export_df.to_json(orient='records',indent=2),"flashcards.json","application/json")
    
    else:
        st.warning("No flashcards were generated. Try with different input")