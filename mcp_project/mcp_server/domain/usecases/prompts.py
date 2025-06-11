class PromptUseCase:
    def __init__(self, prompt_repository):
        self.prompt_repository = prompt_repository

    def list_prompts(self):
        return self.prompt_repository.get_prompt()

    def get_prompt(self, name: str, args: dict):
        #TODO: Logica para llamar el prompt dependediendo del nombre del prompt
        return self.prompt_repository.create_prompt(name, args)