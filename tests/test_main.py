import unittest
from assertpy import assert_that

from src import run


class MyTestCase(unittest.TestCase):

    def test_does_not_throw_any_exception(self):
        run.execute("./",
                    ".dependency-graphics-rc.yaml",
                    "./out/test",
                    "./resources/example_project")

    def test_does_consider_custom_config(self):
        args = run.parse_args(["-c",
                               ".i_am_not_a_default.yaml",
                               "-w", "./",
                               "-o", "out_file",
                               "-a", "./code"])

        assert_that(args.config).is_equal_to(".i_am_not_a_default.yaml")

    def test_use_default(self):
        args = run.parse_args(["-w", "./", "-o", "out_file", "-a", "./code"])

        assert_that(args.config).is_equal_to(".dependency-graphics-rc.yaml")


if __name__ == '__main__':
    unittest.main()
