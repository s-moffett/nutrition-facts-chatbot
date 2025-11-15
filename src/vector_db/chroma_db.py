import chromadb
from blog_post import BlogPost
from vector_db.vector_db import VectorDB

class ChromaDB(VectorDB):

    def __init__(self):
        self.client = chromadb.PersistentClient(path="chromadb_data")
        self.collection = self.client.get_or_create_collection("documents")

    def query_db(self, query) -> list[BlogPost]:
        blogs: chromadb.QueryResult = self.collection.query(
            query_texts=[query],
            n_results=5
        )

        blog_titles = blogs['ids'][0] if blogs['ids'] is not None else []
        blog_texts = blogs['documents'][0] if blogs['documents'] is not None else []
        blog_metadatas = blogs['metadatas'][0] if blogs['metadatas'] is not None else []
        blog_links = [meta['source'] for meta in blog_metadatas]

        return [BlogPost(title, content, link) for title, content, link in zip(blog_titles, blog_texts, blog_links)]
    