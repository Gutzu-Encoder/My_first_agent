from tavily import TavilyClient
import os

def execute_tool(name, inputs):
    if name == "web_search":
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        results = tavily.search(query=inputs["query"], max_results=3)
        return "\n".join([r["content"] for r in results["results"]])