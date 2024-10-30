from kodex.generators.java.spring.base_generator import GeneratorContext
from kodex.generators.java.spring.entity_generator import EntityGenerator
from kodex.generators.java.spring.structure_generator import ProjectStructureGenerator


class SpringBootGeneratorOrchestrator:
    """Orchestrator class to manage the generation chain"""

    def __init__(self):
        self._setup_chain()

    def _setup_chain(self) -> None:
        """Initialize and connect the generator chain"""
        self.structure_generator = ProjectStructureGenerator()
        self.entity_generator = EntityGenerator()

        self.structure_generator.set_next(self.entity_generator)

        self.chain_start = self.structure_generator

    def generate(self, context: GeneratorContext) -> bool:
        """Orchestrator for generating the spring boot service"""
        print("Generating project", context.project_name)

        success = self.chain_start.handle(context)
        if success:
            print("success")

        return True
