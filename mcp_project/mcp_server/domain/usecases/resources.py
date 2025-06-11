class ResourcesUseCase:
    def __init__(self, driven_adapter):
        self.driven_adapter = driven_adapter

    def list_resources(self):
        return self.driven_adapter.get_prompt()

    def read_resource(self, name: str, args: dict):
        #TODO: Logica para llamar el prompt dependediendo del nombre del prompt
        return self.driven_adapter.create_prompt(name, args)