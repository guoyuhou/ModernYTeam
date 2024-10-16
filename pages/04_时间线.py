import streamlit as st
import os

def read_markdown_file(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        return file.read()

st.title("时间线")

introduction_path = os.path.join("content_scripts", "时间线.md")
introduction_content = read_markdown_file(introduction_path)
st.markdown(introduction_content, unsafe_allow_html=True)