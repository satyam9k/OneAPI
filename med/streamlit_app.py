# streamlit_app.py
import streamlit as st
from model import query
from output import generate_table_and_summary

def main():
    st.title("Medical Report Generator")

    # Input text area
    input_text = st.text_area("Enter medical report", "")

    # Button to generate report
    if st.button("Generate Report"):
        if input_text.strip():
            # Process model
            model_output = query({"inputs": input_text})

            # Generate output
            table, summary = generate_table_and_summary(model_output)

            # Display structured table
            st.subheader("Structured Table")
            st.write(table)

            # Display summary
            st.subheader("Summary")
            st.write(summary)
        else:
            st.error("Please enter some input text.")

if __name__ == "__main__":
    main()
