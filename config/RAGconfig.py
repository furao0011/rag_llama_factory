"""
if there is an interface, example:
from multiprocessing.connection import Client

def RAG(user_query: str) -> str:
    try:
        # 使用 with 语句来管理连接
        with Client(('localhost', 6000)) as conn:
            # 发送用户查询
            conn.send(user_query)

            # 接收 RAG 处理后的结果
            result = conn.recv()

        return result

    except Exception as e:
        return f"Error: {e}"
"""
def RAG(user_query: str) -> str:
    processed_query = "我脖子疼," + user_query
    return processed_query