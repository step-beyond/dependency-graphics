import os
import unittest
from assertpy import assert_that

from src.configuration import factory as config_factory


class MyTestCase(unittest.TestCase):

    def test_can_read_configuration(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        config_path: str = os.path.join(this_dir, ".dependency-graphics-rc.yaml")

        config = config_factory.load_config(config_path)

        assert_that(config.get_directory()).is_equal_to("./")


if __name__ == '__main__':
    unittest.main()
