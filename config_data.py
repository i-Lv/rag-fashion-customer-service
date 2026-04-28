
import os

# 项目根目录（基于当前文件所在位置）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DashScope API Key（建议通过环境变量 DASHSCOPE_API_KEY 配置，也可在此直接填写）
DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")

# MD5 去重记录文件
md5_path = os.path.join(BASE_DIR, "md5.txt")

# Chroma 向量数据库
collection_name = "rag"
persist_directory = os.path.join(BASE_DIR, "chroma_db")

# 文本分割器
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number = 1000        # 文本分割的阈值

# 检索参数
top_k = 1                           # 检索返回匹配的文档数量

# 模型配置
embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"
