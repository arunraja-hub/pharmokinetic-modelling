import numpy as np
import numpy.testing as npt
import pytest
#from solution import Solution
from protocol import Protocol

@pytest.mark.parametrize("test, expected, expected_error",
    [("/Users/zhujiayuan/Desktop/pharmokinetic-modelling/test_data/test_error.csv",
    None, ValueError)

    ])
def test_read_dosage(test, expected, expected_error):
    """Test protocol could convert csv files to pandas dataframe"""
    
    if expected_error:
        with pytest.raises(expected_error):
            npt.assert_array_equal(expected, Protocol(test).read_dosage())
    else:
        test = Protocol(test).read_dosage()
        assert np.all(len(test.select_dtypes(include=["float", 'int']).columns) \
            == len(test.columns))

# # expected: 1 or 2 or 3 or 4 depends on different cases
# @pytest.mark.parametrize("test, expected, expected_error",
#     [
        

#     ])
# def test_rhs(test, expected, expected_error):
#     """Test right hand equations are in desired size"""
#     from pharmodel.solutions import rhs
#     if expected_error:
#         with pytest.raises(expected_error):
#             npt.assert_array_equal(expected, rhs(test))

#     else:
#         assert(len(rhs(test)) == expected)


# # expected: len(sol.y)
# @pytest.mark.parametrize("test, expected, expected_error",
#     [
        

#     ])
# def test_solver(test, expected, expected_error):
#     """Test the output of solver is in desired size"""
#     from pharmodel.solutions import solver
#     if expected_error:
#         with pytest.raises(expected_error):
#             npt.assert_array_equal(expected, solver(test))
#     else:
#         assert(len(solver(test).y) == expected[1])


# # expected: 1/2/3/... depends on number of doses
# @pytest.mark.parametrize("test, expected, expected_error",
#     [
        

#     ])
# def test_solver_for_list(test, expected, expected_error):
#     """Test the output represents correct number of doses"""
#     from pharmodel.solutions import solver_for_list
#     if expected_error:
#         with pytest.raises(expected_error):
#             npt.assert_array_equal(expected, solver_for_list(test))
#     else:
#         assert len(solver_for_list(test)) == expected
    