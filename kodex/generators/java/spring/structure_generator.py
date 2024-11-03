import shutil
from pathlib import Path

from kodex.common.code_generator import CodeGenerator
from kodex.generators.java.spring.base_generator import GeneratorHandler
from kodex.utils.case_convertion_util import kebab_to_pascal_case

# Define this at the top of your file or in a config file
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent  # Adjust based on your structure


def _copy_gradle_wrapper(context):
    template_path = PROJECT_ROOT / "templates" / "java" / "spring" / "gradle_core"
    shutil.copytree(template_path, context["base_dir"], dirs_exist_ok=True)


def _generate_gradle_build(context) -> None:
    CodeGenerator().render('java/spring/build.gradle.j2', 'build.gradle',
                           context["base_dir"], context)


def _generate_gradle_settings(context) -> None:
    CodeGenerator().render('java/spring/settings.gradle.j2', 'settings.gradle',
                           context["base_dir"], context)


def _generate_main_class(context) -> None:
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

            context['application_name'] = kebab_to_pascal_case(context["project_name"]) + "Application"

            # Copy gradle_core wrapper files
            _copy_gradle_wrapper(context)

            # Generate build.gradle_core
            _generate_gradle_build(context)

            # Generating settings.gradle_core
            _generate_gradle_settings(context)

            # Generating the SpringApplication Main Class
            _generate_main_class(context)

            return True
        except Exception as e:
            print(f"Error generating project structure: {str(e)}")
            return False
