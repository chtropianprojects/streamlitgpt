from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,

    ServiceContext,
    load_index_from_storage
)
import re
from llama_index.core.response_synthesizers import TreeSummarize
from llama_index.llms.groq import Groq
from llama_index.llms.mistralai import MistralAI
import streamlit as st
import warnings
from request_models import ResumeScreenerDecision

warnings.filterwarnings('ignore')


MISTRAL_API_KEY = st.secrets["MISTRAL_API_KEY"]
GROQ_API_KEY = st.secrets["MISTRAL_API_KEY"]
llm = Groq(model="llama3-70b-8192", api_key=GROQ_API_KEY)
llm = MistralAI(api_key=MISTRAL_API_KEY)
summarizer = TreeSummarize(verbose=True, llm=llm,output_cls=ResumeScreenerDecision)

PITCH_SALES_LANGUAGE="English"

QUERY_TEMPLATE = """
You are an expert resume reviewer.
You job is to decide if the candidate can apply his resume screen given the job description and provide arguments why he cannot apply to the job.  
You must provide a Sales pitch - the tone should be technical validation of the consultant value. All the answers should be in  {language}

### Job Description
{job_description}

"""

