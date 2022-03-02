"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [3,4])
    ],
    ids=("Zeroes", "Integers")
)
def test_daily_mean(test, expected):
    """Test daily mean function works for an array of integers and zeroes"""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [5,6])
    ],
    ids=("Zeroes", "Integers")
)
def test_daily_max(test, expected):
    """Test daily max function works for an array of integers and zeroes"""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0], [0,0], [0,0]], [0,0]),
        ([[1,2], [3,4], [5,6]], [1,2])
    ],
    ids=("Zeroes", "Integers")
)
def test_daily_min(test, expected):
    """Test daily min function works for an array of integers and zeroes"""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0,0],[0,0],[0,0]],[0,0]), # Trivial
        ([[1,1],[1,1],[1,1]],[0,0]), # Constant columns have variance 0
        ([[0,0],[1,5]], [0.5,2.5])
    ],
    ids = ('Zeroes','Constants','Knowns')
)

def test_daily_sd(test,expected):
    from inflammation.models import daily_sd
    npt.assert_array_equal(daily_sd(np.array(test)), np.array(expected))



@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
            None
        ),
        (
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            None
        ),
        (
            np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            None
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, float('nan')]]),
            np.array([[0.33, 0.67, 1], [0.67, 0.83, 1], [0.88, 1, 0]]),
            None
        ),
        (
            np.array([[float('nan'), float('nan')], [float('nan'), float('nan')], [float('nan'), float('nan')]]),
            np.array([[0, 0], [0, 0], [0, 0]]),
            None
        ),
        (
            np.array([[-1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
            ValueError
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            TypeError
        ),
        (
            np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]]),
            np.array([[[0.5, 1], [0.75, 1]], [[0.5, 1], [0.75, 1]]]),
            ValueError
        )
    ],
    ids=("Integers", "Zeroes", "Ones", "Some missing", "All missing", "Negatives", "List input", "3 dimensional")
)
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for range of conditions described above.
    Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(test), expected, decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(test), expected, decimal=2)
