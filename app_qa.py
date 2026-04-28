
# 智能客服问答（主界面）

import uuid
import os
import streamlit as st
from rag import RagService
import config_data as config


def get_session_id():
    """获取或创建当前用户的唯一会话 ID"""
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())[:8]
    return st.session_state["session_id"]


def check_api_key():
    """检查 API Key 是否可用"""
    if not os.environ.get("DASHSCOPE_API_KEY"):
        st.error(
            "❌ 未检测到 DASHSCOPE_API_KEY 环境变量。\n\n"
            "请设置后再启动：\n"
            "- 临时设置：`set DASHSCOPE_API_KEY=your_key_here`\n"
            "- 永久设置：在系统环境变量中添加 DASHSCOPE_API_KEY"
        )
        st.stop()


# 启动前校验
check_api_key()

session_id = get_session_id()

# 标题栏（含 session 标识）
col_title, col_session = st.columns([6, 1])
with col_title:
    st.title("🛍️ 智能客服")
with col_session:
    st.caption(f"会话: {session_id}")

st.divider()

# 初始化消息列表
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好！我是智能服装顾问，有什么可以帮你的？"}]

# 初始化 RAG 服务
if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

# 构建当前会话的配置
session_config = {
    "configurable": {
        "session_id": session_id,
    }
}

# 渲染历史消息
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 清空对话按钮
if st.button("🗑️ 清空对话", key="clear_chat"):
    st.session_state["message"] = [{"role": "assistant", "content": "对话已清空，请问有什么可以帮你的？"}]
    from file_history_store import get_history
    get_history(session_id).clear()
    st.rerun()

# 用户输入
prompt = st.chat_input()

if prompt:
    # 显示用户消息
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    ai_res_list = []
    with st.spinner("AI 思考中..."):
        res_stream = st.session_state["rag"].chain.stream({"input": prompt}, session_config)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res_stream, ai_res_list))
        st.session_state["message"].append({"role": "assistant", "content": "".join(ai_res_list)})
