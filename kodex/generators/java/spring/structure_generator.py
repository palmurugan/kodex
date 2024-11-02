import shutil
from pathlib import Path

from kodex.common.code_generator import CodeGenerator
from kodex.generators.java.spring.base_generator import GeneratorHandler

# Define this at the top of your file or in a config file
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent  # Adjust based on your structure

def kebab_to_pascal_case(s: str) -> str:
    # Split the string by hyphens, capitalize each part, and join them together
    return ''.join(word.capitalize() for word in s.split('-'))

def _copy_gradle_wrapper(context):
    template_path = PROJECT_ROOT / "templates" / "java" / "spring" / "gradle_core"
    shutil.copytree(template_path, context["base_dir"], dirs_exist_ok=True)


def _generate_gradle_build(context) -> None:
    CodeGenerator().render('java/spring/build.gradle.j2', 'build.gradle',
                           context["base_dir"], context)


def _generate_gradle_settings(context) -> None:
    CodeGenerator().render('java/spring/settings.gradle.j2', 'settings.gradle',
                           context["base_dir"], context)


def _generate_spring_application(context) -> None:
    CodeGenerator().render('java/spring/app/spring_application.j2', context['application_name'] + '.java',
                           context['package_dir'], context)


class ProjectStructureGenerator(GeneratorHandler):
    """Generates the basic project structure"""

    def process(self, context) -> bool:
        try:
            print(f"Generating project structure for {context["project_name"]}")

            # Create the Java package path
            Path(context["output_dir"] / context["project_name"] / "src" / "main" / "java" / \
                 context["base_package"].replace(".", "/")).mkdir(parents=True, exist_ok=True)
            Path(context["output_dir"] / context["project_name"] / "src" / "main" / "resources").mkdir(parents=True,
                                                                                                       exist_ok=True)

            # Assigning package and resource directories
            context["base_dir"] = context["output_dir"] / context["project_name"]
            context["package_dir"] = context["output_dir"] / context["project_name"] / "src" / "main" / "java" / \
                                     context["base_package"].replace(".", "/")
            context["resource_dir"] = context["output_dir"] / context["project_name"] / "src" / "main" / "resources"

            context['application_name'] = kebab_to_pascal_case(context["project_name"])+"Application"

            # Copy gradle_core wrapper files
            _copy_gradle_wrapper(context)

            # Generate build.gradle_core
            _generate_gradle_build(context)

            # Generating settings.gradle_core
            _generate_gradle_settings(context)

            _generate_spring_application(context)

            # Generate application.properties
            self._generate_application_properties(context)

            # Generate main application class
            self._generate_main_class(context)

            return True
        except Exception as e:
            print(f"Error generating project structure: {str(e)}")
            return False

    def _generate_pom_xml(self, context) -> None:
        # Implementation remains the same
        pass

    def _generate_application_properties(self, context) -> None:
        # Implementation remains the same
        pass

    def _generate_main_class(self, context) -> None:
        # Implementation remains the same
        pass
