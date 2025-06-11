class ToolsUseCase:
    def __init__(self, tools_repository):
        self.tools_repository = tools_repository

    def list_tools(self):
        return self.tools_repository.get_tools()

    def call_tool(self, name: str, args: dict):
        #TODO: Logica para llamar el tools dependediendo del nombre de la tool
        return self.tools_repository.create_tools(name, args)
