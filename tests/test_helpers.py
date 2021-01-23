# -*- coding: utf-8 -*-

from .context import use_hello

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    # def test_get_message(self):
    #     answer = """
    # use_hello world!
    # """
    #     assert (use_hello.helpers.get_message() == answer)


if __name__ == '__main__':
    unittest.main()
