import os
from datetime import datetime
from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from duckduckgo_search import DDGS

# -------------------- SAVE TOOL --------------------
def save_to_txt(data: str, filename="research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = f"\n\n--- {timestamp} ---\n{data}\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(block)
    return f"Saved to {filename}"

save_tool = Tool(
    name="save_to_file",
    func=save_to_txt,
    description="Save the final answer to a local text file."
)

# -------------------- DUCKDUCKGO SEARCH TOOL --------------------
def duckduckgo_search(query: str, max_results: int = 3):
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, region='wt-wt', safesearch='Off', timelimit='y', max_results=max_results):
                results.append(r)

        if not results:
            return "No results found."

        output = ""
        for idx, r in enumerate(results, start=1):
            title = r.get("title", "No title")
            body = r.get("body", "")
            link = r.get("href", "")
            output += f"{idx}. {title}\n{body}\n{link}\n\n"

        return output.strip()

    except Exception as e:
        return f"DuckDuckGo search failed: {e}"

search_tool = Tool(
    name="search",
    func=duckduckgo_search,
    description="Search the web for any information using DuckDuckGo."
)

# -------------------- WIKIPEDIA TOOL --------------------
wiki_api = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=50000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api)
