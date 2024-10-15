import streamlit as st
import os

def read_markdown_file(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        return file.read()

st.title("编程资源")

# 获取"content_scripts/文章"文件夹中的所有Markdown文件
articles_folder = os.path.join("content_scripts", "编程资源")
article_files = [f for f in os.listdir(articles_folder) if f.endswith('.md')]

# 创建一个下拉菜单让用户选择文章
selected_article = st.selectbox("选择一篇文章", article_files)

# 读取并显示选中的文章内容
if selected_article:
    article_path = os.path.join(articles_folder, selected_article)
    article_content = read_markdown_file(article_path)
    st.markdown(article_content, unsafe_allow_html=True)