import streamlit as st
import time

def process_prd(file):
    time.sleep(5)

def process_tickets(file_list):
    st.write("Processing ticket files...")

class InputComponent:

    def __init__(self) -> None:
         pass
    
    def load(self):
        with st.form("prd_form", clear_on_submit=False):
            st.write("Upload your PRD document:")
            prd_file = st.file_uploader("Choose a file", type=['pdf', 'docx'], key="prd")
            submit_prd = st.form_submit_button("Submit PRD")

        if submit_prd and prd_file is not None:
            with st.spinner('Analysing PRD...'):
                process_prd(prd_file) 
            st.success('PRD analysis completed!')

            with st.form("tickets_form", clear_on_submit=True):
                st.write("Upload your ticket files:")
                ticket_files = st.file_uploader("Choose files", type=['csv', 'xlsx'], accept_multiple_files=True, key="tickets")
                submit_tickets = st.form_submit_button("Submit Ticket Files")

                if submit_tickets and ticket_files:
                    process_tickets(ticket_files)  

ic = InputComponent()
ic.load()
         