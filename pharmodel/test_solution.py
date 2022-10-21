import unittest
import pkmodel as pk
import pytest

import numpy as np
import numpy.testing as npt


# class SolutionTest(unittest.TestCase):
    # """
    # Tests the :class:`Solution` class.
    # """
@pytest.mark.parametrize(
"test, expected",
[
    ([1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],[0]),
    ([1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],[0]),
    ([1, 0, 0.5, 0, 0, 1, 1, 1, 1, 1, 1, 1],[0.5])
])

def test_rhs00(test, expected):
    """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
    from pharmodel import Protocol,Solution, Model
    dose_rec = Protocol('test_doses_combined.csv')
    dose_df = dose_rec.read_dosage()
    # print(dose_df)
    model_params = Model(absorb = 0, comp = 0, V_c = 1, CL = 1, Q_p1 = 1, V_p1 = 1, Q_p2 = 1.0, V_p2 = 1, k_a = 1.0)
    df_to_solve = Solution(dose_df, model_params)
    npt.assert_array_equal(np.array(expected), df_to_solve.rhs_00(*test))

########################


@pytest.mark.parametrize(
"test, expected",
[
    ([1, 0, [0,0], 0, 0, 1, 1, 1, 1, 1, 1, 1],[[0,0]]),
    ([1, 0, [1,1], 0, 0, 1, 1, 1, 1, 1, 1, 1],[[1,1]]),
    ([1, 0, [0.5,0.5], 0, 0, 1, 1, 1, 1, 1, 1, 1],[[0.5,0.5]])
])

def test_rhs10(test, expected):
    """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
    from pharmodel import Protocol,Solution, Model
    dose_rec = Protocol('test_doses_combined.csv')
    dose_df = dose_rec.read_dosage()
    # print(dose_df)
    model_params = Model(absorb = 0, comp = 0, V_c = 1, CL = .1, Q_p1 = 1.1, V_p1 = 0.1, Q_p2 = 1.0, V_p2 = 0.1, k_a = 1.0)
    df_to_solve = Solution(dose_df, model_params)
    npt.assert_array_equal(np.array(expected), df_to_solve.rhs_10(*test))