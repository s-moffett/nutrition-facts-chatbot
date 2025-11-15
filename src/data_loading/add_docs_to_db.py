import chromadb
import os

client = chromadb.PersistentClient(path="chromadb_data")

# client.delete_collection("documents")
collection = client.get_or_create_collection("documents")

# Load blogs into vector DB
blog_files = os.listdir("data/blogs/")

total_blogs = len(blog_files)
print(f"Adding {total_blogs} blogs to vector DB")

for idx, filename in enumerate(blog_files):
    print(f"Processing file {idx + 1} of {total_blogs}: {filename}")
    
    blog_path = os.path.join("data/blogs/", filename)
    with open(blog_path, "r") as f:
        content = f.read()

    # Get url
    blog_url = "https://nutritionfacts.org/blog/" + filename

    collection.add(
        documents=[content],
        ids=[filename],
        metadatas=[{"source": blog_url}]
    )
