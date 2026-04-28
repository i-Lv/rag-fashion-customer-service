# 🛍️ 服装商品智能客服

基于 **RAG（检索增强生成）** 技术的服装商品智能客服系统，集成 LangChain + Chroma 向量数据库 + 通义千问大模型，支持自然语言问答、知识库管理等功能。

## ✨ 功能特性

- 🤖 **智能问答**：基于 RAG 的客服对话，结合知识库精准回答用户问题
- 📚 **知识库管理**：支持上传 TXT 文件，自动文本分割与向量化存储
- 🧠 **多轮对话**：基于会话历史理解上下文，支持连续追问
- 🔍 **语义检索**：使用 text-embedding-v4 向量化，语义级别匹配商品知识
- 🗑️ **对话管理**：支持清空当前会话历史
- 👥 **多用户隔离**：基于 UUID 的会话隔离，避免多用户对话串台

## 🏗️ 项目结构

```
服装商品智能客服/
├── app_qa.py              # 客服问答主界面（Streamlit）
├── app_file_uploader.py   # 知识库文件上传界面
├── rag.py                 # RAG 链路服务（检索 + 生成）
├── knowledge_base.py      # 知识库上传与向量化
├── vector_stores.py       # Chroma 向量检索服务
├── file_history_store.py  # 基于文件的对话历史存储
├── config_data.py         # 全局配置
├── requirements.txt       # Python 依赖
├── data/                  # 示例知识库文档
│   ├── 尺码推荐.txt
│   ├── 洗涤养护.txt
│   └── 颜色选择.txt
├── chroma_db/             # Chroma 向量数据库（自动生成）
└── chat_history/          # 对话历史记录（自动生成）
```

## 🛠️ 技术栈

| 组件 | 技术选型 |
|------|----------|
| 大语言模型 | 通义千问 qwen3-max（ChatTongyi） |
| Embedding | text-embedding-v4（DashScope） |
| 向量数据库 | Chroma（本地持久化） |
| 开发框架 | LangChain + Streamlit |

## 🚀 快速开始

### 1. 环境要求

- Python 3.9+
- 阿里云 DashScope API Key（[申请地址](https://dashscope.console.aliyun.com/)）

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

**方式一（推荐）：环境变量**

```bash
# Windows PowerShell
$env:DASHSCOPE_API_KEY = "your_api_key_here"

# Linux / macOS
export DASHSCOPE_API_KEY="your_api_key_here"
```

**方式二：.env 文件**

在项目根目录创建 `.env` 文件：

```env
DASHSCOPE_API_KEY=your_api_key_here
```

### 4. 启动应用

**启动客服主界面：**

```bash
streamlit run app_qa.py
```

**启动知识库上传界面（可选）：**

```bash
streamlit run app_file_uploader.py
```

## 📖 使用说明

### 知识库管理

1. 启动知识库上传界面：`streamlit run app_file_uploader.py`
2. 上传 TXT 格式的知识库文件
3. 系统自动进行文本分割、向量化并存入 Chroma 数据库
4. 相同内容的文件不会重复载入

### 客服问答

1. 启动客服界面：`streamlit run app_qa.py`
2. 在对话框中输入问题，如"针织毛衣如何保养？"
3. AI 会基于知识库内容进行回答
4. 点击「清空对话」可重置当前会话

## ⚙️ 配置说明

在 `config_data.py` 中可调整以下参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `chunk_size` | 文本分割最大长度 | 1000 |
| `chunk_overlap` | 分割重叠字符数 | 100 |
| `top_k` | 检索返回文档数量 | 1 |
| `chat_model_name` | 大语言模型名称 | qwen3-max |
| `embedding_model_name` | 向量化模型名称 | text-embedding-v4 |

## 📄 License

MIT
