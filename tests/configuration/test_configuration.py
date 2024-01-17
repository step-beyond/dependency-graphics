import os
import unittest
from assertpy import assert_that

from src.configuration.config import Config
from src.configuration import factory as config_factory


class MyTestCase(unittest.TestCase):

    def test_can_read_configuration(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        config_path: str = os.path.join(this_dir, ".dependency-graphics-rc.yaml")

        config = config_factory.load_config(config_path)

        assert_that(config.get_ignore_modules()).is_equal_to(["module_1", "module_2"])


    def test_able_to_build_config_hierarchy(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))

        configs: [] = config_factory.load_configs(this_dir, "./02.yaml")

        assert_that(configs).is_length(2)
        assert_that(configs).contains_sequence(
            Config({'directory': './', 'ignore-modules': ['module_3']}),
            Config({'parent-config': './01.yaml', 'ignore-modules': ['module_1']}))


if __name__ == '__main__':
    unittest.main()
