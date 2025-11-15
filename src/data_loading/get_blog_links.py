import requests
from bs4 import BeautifulSoup

def get_page(url, page_num, blog_links, f):
    f.write("\n")
    print(f"Fetching page: {url}")

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")

    new_blog_links = set([l.get("href") for l in links if "nutritionfacts.org/blog" in l.get("href") and l.get("href") != "https://nutritionfacts.org/blog/" and "/page/" not in l.get("href")])

    print(f"Found {len(new_blog_links)} links")
    # blog_links.update(new_blog_links)
    f.write("\n".join(list(new_blog_links)))

    page_num += 1
    if page_num > max_page:
        return

    next_page = [l.get("href") for l in links if "/page/" in l.get("href")]

    if next_page:
        get_page(next_page[0], page_num, blog_links, f)

max_page = 59
page_num = 1
blog_links = set()

with open("data/blog-links.txt", "w") as f:
    get_page("https://nutritionfacts.org/blog/", page_num, blog_links, f)
