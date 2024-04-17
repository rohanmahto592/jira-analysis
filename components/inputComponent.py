import streamlit as st
import time
from io import BytesIO
from docx import Document
def process_prd(upload_file):

    if upload_file is None:
            st.error("Please Select Doc File")
    elif upload_file is not None:
        file_bytes=upload_file.getvalue()
        try:
            if(file_bytes is not None):
                docx =Document(BytesIO(file_bytes))
                return docx
                
        except Exception as e:
            st.error(f"Error while loading a file \n {e}")

def process_tickets(file_list):
    st.write("Processing ticket files...")

class InputComponent:

    def __init__(self) -> None:
         pass
    def load(self):
        with st.form("prd_form", clear_on_submit=False):
            st.write("Upload your PRD document:")
            prd_file = st.file_uploader("Choose doc file", type=['docx'], key="prd",accept_multiple_files=False)
            submit_prd = st.form_submit_button("Submit PRD")

        if submit_prd and prd_file is not None:
            with st.spinner('Analysing PRD...'):
                doc=process_prd(upload_file=prd_file) 
                st.write(doc)
            st.success('PRD analysis completed!')

            with st.form("tickets_form", clear_on_submit=False):
                st.write("Upload your ticket files:")
                ticket_files = st.file_uploader(label="Upload doc files", type=['docx'], accept_multiple_files=True, key="tickets")
                submit_tickets = st.form_submit_button("Submit Ticket Files")

                if submit_tickets and ticket_files:
                    process_tickets(ticket_files)  

ic = InputComponent()
ic.load()
         