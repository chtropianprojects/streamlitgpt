import streamlit as st
from llama_index.core import (

    SimpleDirectoryReader

)
from llm_launcher import summarizer
import re
from pypdf import PdfReader
from llm_launcher import QUERY_TEMPLATE, PITCH_SALES_LANGUAGE

st.title("stlite sharing: Serverless Streamlit app platform")

mission_ori = st.sidebar.file_uploader("Upload a mission description",type ="pdf")
cv_ori = st.sidebar.file_uploader("Upload a CV", type  = "pdf")

st.markdown("This is an application to analyse if the CV can fit with the mission description")
st.markdown("In order to understand if there is a fit, please upload both the mission and the CV in PDF format*")
   
def cleaning_docs(document):
    final =""
    for i in document.pages:
        final+=i.extract_text()
    s = re.sub(r'[^a-zA-Z0-9 ]', '', final)
    return s


if mission_ori is not None and cv_ori is not None:
    if st.button('Launch analysis'):
        st.markdown("Analysis on doing ere... ")
 

        Offer_parsing = PdfReader(mission_ori)

        clean_offer = cleaning_docs(Offer_parsing)

        CV_parsing = PdfReader(cv_ori)
        clean_cv = CV_parsing

        query = QUERY_TEMPLATE.format(language=PITCH_SALES_LANGUAGE, job_description=clean_offer)

        st.text("query")
        st.text(query)
        st.text("LLM now running...")

        from llama_index.core.schema import NodeWithScore
    
    
    response = summarizer.synthesize(query, nodes = [NodeWithScore(node=doc, score=1.0) for doc in CV_parsing.pages])
    for cd in response.criteria_decisions:
        st.text("### CRITERIA DECISION")
        st.text(cd.reasoning)
        st.text(cd.decision)
    st.text("#### OVERALL REASONING ##### ")
    st.text(str(response.overall_reasoning))
    st.text(str(response.overall_decision))
    st.text("#### SALES PITCH ##### ")
    st.text(str(response.sales_pitch))

