import requests
from bs4 import BeautifulSoup
import time
import os

def save_blog_post(url):
    print(f"Downloading {url}")
    time.sleep(0.25)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    article = soup.article
    text = article.get_text()

    post_name = url.replace("https://nutritionfacts.org/blog/", "").replace("/", "")

    with open(f"data/blogs/{post_name}", "w") as f:
        f.write(text)

with open("data/blog-links.txt") as links_file:
    blog_links = links_file.read().split("\n")

print(f"{len(blog_links)} blogs total")

blog_content = os.listdir("data/blogs/")
print(f"{len(blog_content)} blogs downloaded")

all_posts = set([l.replace("https://nutritionfacts.org/blog/", "").replace("/", "") for l in blog_links])
downloaded = set(blog_content)

not_downloaded = all_posts.difference(downloaded)

for link in not_downloaded:
    save_blog_post("https://nutritionfacts.org/blog/" + link)
