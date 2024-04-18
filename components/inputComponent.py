import streamlit as st
import sys
sys.path.append('../')
from utils.processFile import process_prd,process_tickets
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

                if submit_tickets and ticket_files is not None:
                    process_tickets(ticket_files)  

ic = InputComponent()
ic.load()
         