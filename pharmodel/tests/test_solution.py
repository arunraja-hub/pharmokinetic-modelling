import unittest
import pkmodel as pk
import pytest


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    @pytest.mark.parametrize(
    "test, expected",
    [
        ([0], [0]),
       ([1],  [1]),
    ])

    def test_rhs00(test, expected):



