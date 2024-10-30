import streamlit as st
import os
from pathlib import Path

# 设置页面标题
st.title("工具箱")

# 获取resource文件夹路径
resource_path = Path("resource")

# 确保resource文件夹存在
if not resource_path.exists():
    st.error("resource文件夹不存在!")
else:
    # 获取所有文件
    files = list(resource_path.glob("*"))   
    
    if not files:
        st.info("resource文件夹为空")
    else:
        st.write("### 可用资源:")
        
        # 创建文件列表
        for file in files:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"📄 {file.name}")
            
            with col2:
                # 读取文件内容
                with open(file, "rb") as f:
                    file_content = f.read()
                # 创建下载按钮    
                st.download_button(
                    label="下载",
                    data=file_content,
                    file_name=file.name,
                    mime="application/octet-stream"
                )

