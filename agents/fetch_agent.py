import os
import requests
from bs4 import BeautifulSoup
print("🔑 GITHUB_TOKEN loaded:", bool(os.getenv("MY_GITHUB_TOKEN")))
def fetch_agent(state):
    items = []

    # LangChain Blog
    blog_url = "https://blog.langchain.dev/"
    soup = BeautifulSoup(requests.get(blog_url).text, "html.parser")

    for article in soup.find_all("article"):
        h2 = article.find("h2")
        a = article.find("a")
        if not h2 or not a:
            continue

        items.append({
            "title": h2.text.strip(),
            "url": a["href"],
            "source": "LangChain Blog"
        })

    # LangGraph GitHub Releases (AUTHENTICATED)
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('MY_GITHUB_TOKEN')}"
    }

    resp = requests.get(
        "https://api.github.com/repos/langchain-ai/langgraph/releases",
        headers=headers
    )

    if resp.status_code == 200:
        for r in resp.json()[:3]:
            items.append({
                "title": r.get("name", "No title"),
                "url": r.get("html_url"),
                "source": "LangGraph Release"
            })
    else:
        print("⚠️ GitHub API error:", resp.status_code)

    state["items"] = items
    return state
