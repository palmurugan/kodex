from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict, Any


@dataclass
class GeneratorContext:
    """Context containing all the information needed for generation"""
    project_name: str
    base_package: str
    output_dir: Path
    java_version: str
    dependencies: List[str]

    def __post_init__(self):
        # Create full project path including project name
        self.project_dir = Path(self.output_dir) / self.project_name
        # Create the Java package path
        self.package_dir = self.project_dir / "src" / "main" / "java" / \
                           self.base_package.replace(".", "/")
        # Create resources directory path
        self.resources_dir = self.project_dir / "src" / "main" / "resources"


class GeneratorHandler(ABC):
    """Base handler for the generator chain"""

    def __init__(self, next_handler: Optional['GeneratorHandler'] = None):
        self._next_handler = next_handler

    def set_next(self, handler: 'GeneratorHandler') -> 'GeneratorHandler':
        self._next_handler = handler
        return handler

    def handle(self, context: GeneratorContext) -> bool | None:
        success = self.process(context)

        if success and self._next_handler:
            return self._next_handler.handle(context)

        return success

    @abstractmethod
    def process(self, context: GeneratorContext) -> bool:
        pass