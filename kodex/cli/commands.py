from pathlib import Path

import click
from colorama import Fore

from kodex.generators.java.spring.SpringBootGeneratorOrchestrator import SpringBootGeneratorOrchestrator
from kodex.generators.java.spring.base_generator import GeneratorContext


@click.group()
@click.version_option()
def main():
    """kodeX - A code generator for Java & Spring Boot Microservices"""
    pass


@main.command()
@click.argument('project_name')
@click.option('--package', '-p', default='com.example',
              help='Base package name for the application')
@click.option('--java-version', '-j', default='17',
              type=click.Choice(['8', '11', '17', '21']),
              help='Java version to use')
@click.option('--dependencies', '-d', multiple=True,
              type=click.Choice(['mysql', 'postgresql']),
              help='Dependencies to include (can be used multiple times)')
@click.option('--output-dir', '-o', type=click.Path(file_okay=False),
              default='.',
              help='Directory where the project will be generated')
def new(project_name: str,
        package: str,
        java_version: str,
        dependencies: list,
        output_dir: str):
    """Generate new service with the project name & packages"""
    click.echo(f"Generating new project with the name {Fore.GREEN}{project_name}")
    click.echo(f"{Fore.BLUE}Creating project: {project_name}")
    click.echo(f"Package: {package}")
    click.echo(f"Java Version: {java_version}")
    click.echo(f"Dependencies: {', '.join(dependencies)}")
    click.echo(f"Output Directory: {output_dir}{Fore.RESET}")

    context = GeneratorContext(project_name=project_name,
                     base_package=package,
                     output_dir=Path(output_dir),
                     java_version=java_version,
                     dependencies=dependencies)

    orchestrator = SpringBootGeneratorOrchestrator()
    orchestrator.generate(context)


if __name__ == '__main__':
    main()
