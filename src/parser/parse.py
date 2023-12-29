from src.configuration.configuration import configuration
from src.model.modules import ModuleGraph
from src.parser import gradle_parser


def parse_module_tree() -> ModuleGraph:
    return gradle_parser.create_module_graph(configuration.get_directory())
