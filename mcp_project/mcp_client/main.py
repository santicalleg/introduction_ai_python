import asyncio
from typing import List
from mcp.types import CallToolResult, ListToolsResult
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uv",
    args=["run", "/Users/sancalle/projects/ingsw/tmp/mcp_project/mcp_server/main.py"],
    env=None
)

async def chat_loop(self):
    """Run an interactive chat loop"""
    print("\nMCP Chatbot Started!")
    print("Type your queries or 'quit' to exit.")
    
    while True:
        try:
            query = input("\nQuery: ").strip()
    
            if query.lower() == 'quit':
                break
                
            await self.process_query(query)
            print("\n")
                
        except Exception as e:
            print(f"\nError: {str(e)}")

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            available_tools: List[ListToolsResult] = await session.list_tools()
            print("\nConnected to server with tools:", [tool.name for tool in available_tools.tools])

            while True:
                try:
                    arguments = {}
                    query = input("\nAction (the tool): ").strip()
                    if query.lower() == 'quit':
                        break

                    if "search_papers" in query:
                        print(available_tools)
                        tool_name = available_tools.tools[0].name
                        print(tool_name)
                        query = input(f"\nQuery for {tool_name} and quantity results separated with #: ").strip()
                        if query.lower() == 'quit':
                            break
                        topic = query.split("#")[0].strip()
                        quantity = query.split("#")[1].strip() if len(query.split("#")) > 1 else 1
                        arguments = {"topic": topic, "max_results": int(quantity)}
                    elif "extract_info" in query:
                        tool_name = available_tools.tools[1].name
                        query = input(f"\nPaper Id for {tool_name}: ").strip()
                        if query.lower() == 'quit':
                            break
                        arguments = {"paper_id": query}
                    else:
                        print("No matching tool found for the query.")
                        continue

                    result: CallToolResult = await session.call_tool(
                        tool_name,
                        arguments=arguments
                    )

                    print("\nResult from tool call:", [resp.text for resp in result.content])

                except Exception as e:
                    print(f"\nError: {str(e)}")
                    break
            # search_papers_result: CallToolResult = await session.call_tool(
            #     available_tools.tools[0].name,
            #     arguments={"topic": "ML", "max_results": 1}
            # )
            # print("Result from tool call:", search_papers_result)

            # extract_paper_info_result: CallToolResult = await session.call_tool(
            #     available_tools.tools[1].name,
            #     arguments={"paper_id": search_papers_result.content[0].text}
            # )

            # print("Extracted paper info:", extract_paper_info_result.content[0].text)

if __name__ == "__main__":
    asyncio.run(run())
