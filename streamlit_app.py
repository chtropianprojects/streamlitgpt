import streamlit as st


st.title("stlite sharing: Serverless Streamlit app platform")

a = st.sidebar.radio('Choose:',[1,2])
st.write("DB username:", st.secrets["TEST_SECRET"])
