"""
批量录入知识库脚本
读取 data/ 目录下的所有 TXT 文件，向量化存入 Chroma 数据库
"""
import os
from knowledge_base import KnowledgeBaseService

# data 目录路径
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def main():
    service = KnowledgeBaseService()

    # 获取 data 目录下所有 txt 文件
    txt_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]
    txt_files.sort()

    if not txt_files:
        print("未找到任何 TXT 文件")
        return

    print(f"发现 {len(txt_files)} 个知识库文件：")
    print("-" * 40)

    success_count = 0
    skip_count = 0

    for filename in txt_files:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        result = service.upload_by_str(content, filename)

        if "[成功]" in result:
            print(f"  [OK] {filename} -> 载入成功")
            success_count += 1
        elif "[跳过]" in result:
            print(f"  [SKIP] {filename} -> 已存在，跳过")
            skip_count += 1
        else:
            print(f"  [FAIL] {filename} -> 载入失败：{result}")

    print("-" * 40)
    print(f"完成！成功 {success_count} 个，跳过 {skip_count} 个，共 {len(txt_files)} 个文件")


if __name__ == "__main__":
    main()
