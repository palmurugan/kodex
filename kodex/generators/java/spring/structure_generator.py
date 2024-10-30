from kodex.generators.java.spring.base_generator import GeneratorContext, GeneratorHandler


class ProjectStructureGenerator(GeneratorHandler):
    """Generates the basic project structure"""

    def process(self, context: GeneratorContext) -> bool:
        try:
            print(f"Generating project structure for {context.project_name}")

            # Create project directories
            context.output_dir.mkdir(parents=True, exist_ok=True)
            context.package_dir.mkdir(parents=True, exist_ok=True)
            context.resources_dir.mkdir(parents=True, exist_ok=True)

            # Generate pom.xml
            self._generate_pom_xml(context)

            # Generate application.properties
            self._generate_application_properties(context)

            # Generate main application class
            self._generate_main_class(context)

            return True
        except Exception as e:
            print(f"Error generating project structure: {str(e)}")
            return False

    def _generate_pom_xml(self, context: GeneratorContext) -> None:
        # Implementation remains the same
        pass

    def _generate_application_properties(self, context: GeneratorContext) -> None:
        # Implementation remains the same
        pass

    def _generate_main_class(self, context: GeneratorContext) -> None:
        # Implementation remains the same
        pass
