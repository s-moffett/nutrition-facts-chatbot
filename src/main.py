from blog_post import BlogPost
from vector_db.chroma_db import ChromaDB
from vector_db.vector_db import VectorDB
from llm_client.claude_client import ClaudeClient
from llm_client.llm_client import LLMClient

def answer_user_question(llm: LLMClient, db: VectorDB):
    user_query = input('Ask a nutrition question: ')
    print('\n...\n')

    rag_query = generate_rag_query(llm, user_query)
    blog_posts = get_context(db, rag_query)
    response = answer_query_with_context(llm, user_query, blog_posts)
    print(response)
    return

def generate_rag_query(llm: LLMClient, query: str) -> str:
    rag_query_prompt = f'The user is searching a vector database that contains nutrition blog posts. Add useful synonyms and keywords to their query, and remove unnecessary words. \n\nUser query: {query}'
    return llm.message(rag_query_prompt)

def get_context(db: VectorDB, query: str) -> list[BlogPost]:
    return db.query_db(query)

def answer_query_with_context(llm: LLMClient, query: str, context: list[BlogPost]) -> str:
    blogs_as_text = convert_blogs_to_text(context)
    prompt = f"Answer the user's question about nutrition based on the included blog content. Cite sources as much as possible by including the relevant blog post URL. User question: {query}\n\nBlog content:\n\n{blogs_as_text}"
    response = llm.message(prompt)
    return response

def convert_blogs_to_text(blog_posts: list[BlogPost]) -> str:
    blog_separator = "\n---\n"
    formatted_blogs = [f"Content:\n{blog.content}\nURL:\n{blog.url}" for blog in blog_posts]
    return blog_separator.join(formatted_blogs)

llm = ClaudeClient()
db = ChromaDB()
answer_user_question(llm, db)
