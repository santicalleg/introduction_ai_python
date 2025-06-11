from mcp.server.fastmcp import FastMCP

# from infrastructure.driven_adapters.tools.papers import search_papers, extract_info
from tools.papers import search_papers, extract_info

def start_server():

    mcp = FastMCP("research")

    mcp.add_tool(search_papers)
    mcp.add_tool(extract_info)

    mcp.run(transport='stdio')

    return mcp
