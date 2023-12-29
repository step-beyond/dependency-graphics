import unittest
from assertpy import assert_that
from src.configuration.configuration import configuration


class MyTestCase(unittest.TestCase):

    def test_can_read_configuration(self):
        directory = configuration.get_directory()

        assert_that(directory).is_equal_to("./")


if __name__ == '__main__':
    unittest.main()
