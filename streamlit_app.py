import streamlit as st
from llama_index.core import (

    SimpleDirectoryReader

)
from llama_index.core.schema import NodeWithScore
from llm_launcher import summarizer
import re
from pypdf import PdfReader
from llm_launcher import QUERY_TEMPLATE, PITCH_SALES_LANGUAGE
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document
import json
import pandas as pd
from llm_launcher import GROQ_API_KEY
from llm_langchain import prompt, model, parser, QUERY_TEMPLATE_langchain
from llm_launcher import program,llm



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
query = ""

genre = st.sidebar.radio(
    "Which parser do you want to use",
    ["Langchain", "llamaindex"],
    captions = ["Langchain - better chained", "Lama clever"])


if mission_ori is not None and cv_ori is not None:
    if st.button('Launch analysis'):
        st.markdown("Analysis on doing here ... ")
 
        Offer_parsing = PdfReader(mission_ori)

        clean_offer = cleaning_docs(Offer_parsing)

        CV_parsing = PdfReader(cv_ori)
        clean_cv = cleaning_docs(CV_parsing)

       
        st.markdown("**CV and offer** have been parsed ")
     # Sample category lists with different lengths
        
        # Combine into dictionary and create DataFrame
        
        #response = summarizer.synthesize(query, nodes = [NodeWithScore(node=doc, score=1.0) for doc in clean_cv])
        # Call the function with your JSON data

        if genre == "Langchain":

                        
            chain = prompt | model | parser
        

            response = chain.invoke({"query": QUERY_TEMPLATE_langchain, "job_description":clean_offer,"cv_candidate":clean_cv})


        else:

            for attempt in range(3):
                try:
                    response = program(job_offer=clean_offer,CV_candidate=clean_cv)
                    """Displays response data in well-formatted tables."""


                    break
                except Exception as e:
                    if attempt == 2:
                        st.write(f"Error: {e}")
                        st.write("Please try again later to have it nice and sexy")
    

         # Criteria Decisions Table
        st.subheader("Criteria Decisions:")
        st.text(response.criteria_decisions)
        if response.criteria_decisions:
            data = {
            "Decision": [],
            "Reasoning": []
            }
            for cd in response.criteria_decisions:
                data["Decision"].append(cd.decision)
                data["Reasoning"].append(cd.reasoning)
            df = pd.DataFrame(data)

            st.table(df)
        else:
            st.write("No Criteria Decisions found.")

        # Supportive Missions Table (if data exists)
        if response.supportive_missions is not None:
            st.subheader("Supportive Missions:")
            if response.supportive_missions:
                data = {
                    "Customer": [],
                    "Technology Used": [],
                    "Mission Content":[]
                    }
                for cd in response.supportive_missions:
                    data["Customer"].append(cd.mission_customer)
                    data["Mission Content"].append(cd.mission_technology_used)
                    data["Technology Used"].append(cd.mission_content)
                
                df = pd.DataFrame(data)

                st.table(df)



        # Missing Experience Decisions Table (if data exists)
        if response.criteria_not_decisions is not None:
            st.subheader("Missing Experience Decisions:")
            if response.criteria_not_decisions:
                    data = {
                        "Experience lacking": [],
                        }
                    for cd in response.criteria_not_decisions:
                        data["Experience lacking"].append(cd.reasoning)
                    
                    df = pd.DataFrame(data)

                    st.table(df)

        # Overall Reasoning and Decision
        st.subheader("Overall Reasoning:")
        st.write(response.overall_reasoning)

        st.subheader("Overall Decision:")
        st.write(response.overall_decision)

        # Sales Pitch
        st.subheader("Sales Pitch:")
        query = f"""Rewrite this *{response.sales_pitch}* in French. The sales pitch should be anonymous - and from the third person. It should be engaging
                I want to keep only the translation not comments.
                """
        response_pitch=llm.complete(query,temperature=0.00001)
        st.write(response_pitch)
