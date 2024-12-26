
# define Your RAG method here
# if u use an interface, plz use flask or others method to RAG
def RAG(user_query: str) -> str:
    processed_query = "我脖子疼," + user_query
    return processed_query