import numpy as np
from numpy import testing as npt
from inflammation.models import daily_mean, daily_max, daily_min
import pytest

def test_daily_mean_integers():
    test_input = np.array([[1,2], [3,4], [5,6]])
    test_result = [3, 4]
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_zeros():
    test_input = np.zeros((3, 2))
    test_result = np.zeros(2)
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    
    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

test_daily_mean_integers()
test_daily_mean_zeros()
test_daily_min_string()