import argparse
import sys

from src.configuration import factory as config_factory
from src.configuration.config import Config
from src.transformation import transformation
from src.graphix import draw
from src.parser import parse


def main(config_file_path: str):
    config: Config = config_factory.load_config(config_file_path)
    module_tree = parse.parse_module_tree(config)
    module_tree = transformation.transform_model(module_tree, config)
    draw.draw_dependency_graph(module_tree, config)


def parse_args(plain_args: []):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default=".dependency-graphics-rc.yaml")
    parsed_args, _ = parser.parse_known_args(plain_args)
    return parsed_args


args = parse_args(sys.argv[1:])
main(args.config)
