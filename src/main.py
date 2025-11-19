from blog_post import BlogPost
from vector_db.chroma_db import ChromaDB
from vector_db.vector_db import VectorDB
from llm_client.claude_client import ClaudeClient
from llm_client.llm_client import LLMClient

import textwrap

def answer_user_question(llm: LLMClient, db: VectorDB):
    user_query = input('Ask a nutrition question: ')
    print('\n...\n')

    rag_query = generate_rag_query(llm, user_query)
    blog_posts = get_context(db, rag_query)
    response = answer_query_with_context(llm, user_query, blog_posts)
    print(response)
    return

def generate_rag_query(llm: LLMClient, query: str) -> str:
    rag_prompt = build_markdown_llm_prompt({
        "Instructions": "I am searching for nutrition information in a vector database that contains nutrition-related blog posts. Add useful synonyms and keywords to my query, and remove unnecessary words.",
        "Query": query
    })

    return llm.message(rag_prompt)

def get_context(db: VectorDB, query: str) -> list[BlogPost]:
    return db.query_db(query)

def answer_query_with_context(llm: LLMClient, query: str, context: list[BlogPost]) -> str:
    CHAT_INSTRUCTIONS = textwrap.dedent("""
        - You are an AI assistant that answers nutrition-related questions.
        - Use the provided blog content to inform your answers.
        - Cite sources by including the relevant blog post URL in your answers.
    """)

    prompt = build_markdown_llm_prompt({
        "Instructions": CHAT_INSTRUCTIONS,
        "Question": query,
        "Blog Content": convert_blogs_to_text(context)
    })

    response = llm.message(prompt)
    return response

def convert_blogs_to_text(blog_posts: list[BlogPost]) -> str:
    blog_separator = "\n---\n"
    formatted_blogs = [f"Content:\n{blog.content}\nURL:\n{blog.url}" for blog in blog_posts]
    return blog_separator.join(formatted_blogs)

def build_markdown_llm_prompt(elements: dict) -> str:
    sections = [f"# {title}\n{content}" for title, content in elements.items()]
    return "\n\n".join(sections)

llm = ClaudeClient()
db = ChromaDB()
answer_user_question(llm, db)
