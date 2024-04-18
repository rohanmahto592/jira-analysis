import streamlit as st
from docx import Document
from io import BytesIO
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_prd(upload_file):
    time.sleep(5)
    if upload_file is None:
            st.error("Please Select Doc File")
    elif upload_file is not None:
        file_bytes=upload_file.getvalue()
        try:
            if(file_bytes is not None):
                docx =Document(BytesIO(file_bytes))
                splitAndFormatDocFile(doc=docx)
                return {"status":True,"message":"Analysis Completed"}
                
        except Exception as e:
            st.error(f"Error while loading a file \n {e}")
            return {"status":False,"message":"Failed to analyze"}

def process_tickets(file_list):
    st.write("Processing ticket files...")

def initialize_splitter(chunkSize=512,chunkOverlap=64,separators=["\n\n","\n"," ",""]):
    splitter=RecursiveCharacterTextSplitter(
          chunk_size=chunkSize,
          chunk_overlap=chunkOverlap,
          separators=separators
     )
    return splitter
def splitAndFormatDocFile(doc):
    splitter=initialize_splitter()
    splitted_doc=splitter.split_documents(documents=doc)
    print(splitted_doc)