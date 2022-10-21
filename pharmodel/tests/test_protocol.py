import unittest
import pytest
import pkmodel as pk
import numpy as np
from pharmodel.protocol import Protocol


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        model = pk.Protocol()
        self.assertEqual(model.value, 43)

    # @pytest.mark.parametrize("test, expected",
    # [( "test_dosis_constant_negative.csv", Protocol("test_dosis_constant_positive.csv"))

    # ])

    # def test_read_dosage(test, expected):
    #     """Test protocol could convert csv files to pandas dataframe"""
        
    #     # if expected_error:
    #     #     with pytest.raises(expected_error):
    #     #         np.assert_array_equal(expected, Protocol(test).read_dosage())
    #     # else:
    #     test = Protocol(test).read_dosage()
    #     assert np.all(len(test.select_dtypes(include=["float", 'int']).columns) \
    #         == len(test.columns))

