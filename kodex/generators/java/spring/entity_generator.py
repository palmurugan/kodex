from kodex.generators.java.spring.base_generator import GeneratorHandler, GeneratorContext


class EntityGenerator(GeneratorHandler):
    """Generates entity classes"""

    def process(self, context: GeneratorContext) -> bool:
        # Implementation remains the same
        print("Generating entity")
        pass
