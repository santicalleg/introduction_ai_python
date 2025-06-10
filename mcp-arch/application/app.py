from mcp.server import Server
from mcp.types import (
    TextContent,
    ImageContent,
    Tool,
    EmbeddedResource
)

class Serve():
    def __init__(self, das: dict):
        print("Initializing Serve with driven adapters:", das)
        self.das = das

    app = Server("example-server")

    @app.list_tools()
    async def list_tools(self) -> list[Tool]:
        tools = []
        for name, func in self.das.items():
            tools.append(
                Tool(
                    name=name,
                    description=func.__doc__ or "No description provided",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            k: {"type": "string"} for k in func.__code__.co_varnames[:func.__code__.co_argcount]
                        },
                        "required": list(func.__code__.co_varnames[:func.__code__.co_argcount])
                    }
                )
            )
        return tools

        # return [
        #     types.Tool(
        #         name="calculate_sum",
        #         description="Add two numbers together",
        #         inputSchema={
        #             "type": "object",
        #             "properties": {
        #                 "a": {"type": "number"},
        #                 "b": {"type": "number"}
        #             },
        #             "required": ["a", "b"]
        #         }
        #     )
        # ]

    @app.call_tool()
    async def call_tool(
        self,
        name: str,
        arguments: dict
    ) -> list[TextContent | ImageContent | EmbeddedResource]:

        if name not in self.das:
            raise ValueError(f"Tool not found: {name}")

        result = await self.das.get(name)(arguments)

        return [TextContent(type="text", text=str(result))]
