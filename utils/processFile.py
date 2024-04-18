import streamlit as st
from docx import Document
from io import BytesIO
import time

def process_prd(upload_file):
    time.sleep(5)
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