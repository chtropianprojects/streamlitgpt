from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_groq import ChatGroq
import streamlit as st
from request_models import ResumeScreenerDecision

MISTRAL_API_KEY = st.secrets["MISTRAL_API_KEY"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
model = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY,temperature=0)
parser = PydanticOutputParser(pydantic_object=ResumeScreenerDecision)

prompt = PromptTemplate(
    template="""Answer the user query.\n{format_instructions}\n{query}\n
                ### Job Description
            {job_description}

            ### Candidate cv
            {cv_candidate}""",
    input_variables=["query", "job_description", "cv_candidate"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)



QUERY_TEMPLATE_langchain = """
You are an expert resume reviewer.
You job is to decide if the candidate can apply his resume screen given the job description and provide arguments why he cannot apply to the job.  

"""