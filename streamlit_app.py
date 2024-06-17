import streamlit as st


st.title("stlite sharing: Serverless Streamlit app platform")

a = st.sidebar.radio('Choose:',[1,2])

if st.secrets["TEST_SECRET"] !="YST":

    st.write("DB username:", "susccesfe")
