from src.configuration.config import Config
from src.model.modules import ModuleGraph
from src.parser import gradle_parser


def parse_module_tree(code_path: str, config: Config) -> ModuleGraph:
    return gradle_parser.create_module_graph(code_path, config)
