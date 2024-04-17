import streamlit as st
from streamlit import delta_generator
class Form:
    form:delta_generator
    def __init__(self,name="form1"):
        self.name=name
        self.form=st.form(name)
    
    def inputFile(self,fileLabel,submitButtonLabel="Submit",acceptMultipleFiles=False):
        self.label=fileLabel
        self.submitButtonLabel=submitButtonLabel
        self.acceptMultipleFiles=acceptMultipleFiles
        self.form.file_uploader(self.label,accept_multiple_files=self.acceptMultipleFiles)
        self.form.form_submit_button(self.submitButtonLabel)

    def alertSuccessMessage(self,message):
        self.form.success(message)

    def alertErrorMessage(self,message):
        self.form.error(message)

    def alertInfoMessage(self,message):
        self.form.info(message)
        
    def alertException(self,message):
        self.form.exception(message)

    
form=Form(name="form1")
form.inputFile("Upload PRD Document","upload")
form.alertSuccessMessage("uploaded")


