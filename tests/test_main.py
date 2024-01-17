import unittest
from assertpy import assert_that

from src import main


class MyTestCase(unittest.TestCase):

    def test_does_not_throw_any_exception(self):
        main.main(".dependency-graphics-rc.yaml")

    def test_does_consider_custom_config(self):
        args = main.parse_args(["-c", ".i_am_not_a_default.yaml"])

        assert_that(args.config).is_equal_to(".i_am_not_a_default.yaml")

    def test_use_default(self):
        args = main.parse_args([])

        assert_that(args.config).is_equal_to(".dependency-graphics-rc.yaml")


if __name__ == '__main__':
    unittest.main()
