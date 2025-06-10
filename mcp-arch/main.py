import asyncio
from mcp.server.stdio import stdio_server

from application.app import Serve

from infrastructure.driven_adapters.tools.calculate import Calculate

async def run():
    server = Serve(das={
        "add": Calculate.add,
        "subtract": Calculate.subtract
    })

    app = server.app

    print(app)

    async with stdio_server() as streams:
        await app.run(
            streams[0],
            streams[1],
            app.create_initialization_options()
        )

asyncio.run(run())