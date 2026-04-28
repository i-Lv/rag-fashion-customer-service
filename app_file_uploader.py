"""
知识库文件上传
基于Streamlit完成WEB网页上传服务
pip install streamlit

Streamlit：当WEB页面元素发生变化，则代码重新执行一遍
"""

import os
import streamlit as st
from knowledge_base import KnowledgeBaseService

# 添加网页标题
st.title("📚 知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    "请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,
)

# session_state
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

# 已处理文件名记录，防止 Streamlit 重执行导致重复处理
if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = set()

if uploader_file is not None:
    file_name = uploader_file.name

    # 检查是否已处理过该文件（本次会话内）
    if file_name in st.session_state["uploaded_files"]:
        st.info(f"⚠️ 文件「{file_name}」已在本次会话中处理过，跳过重复载入。")
    else:
        file_type = uploader_file.type
        file_size = uploader_file.size / 1024

        st.subheader(f"文件名：{file_name}")
        st.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

        text = uploader_file.getvalue().decode("utf-8")

        with st.spinner("载入知识库中..."):
            result = st.session_state["service"].upload_by_str(text, file_name)
            st.write(result)
            # 记录已处理
            st.session_state["uploaded_files"].add(file_name)

# 显示知识库统计信息
st.divider()
st.caption("💡 提示：支持 TXT 格式文件上传。相同内容的文件不会重复载入。")
