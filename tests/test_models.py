"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest


@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (
            pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")),
            "a",
            7,
        ),
        (
            pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")),
            "b",
            0,
        ),
    ],
)
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array and zeroes and positive integers."""
    from lcanalyzer.models import max_mag

    assert max_mag(test_df, test_colname) == expected


@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (
            pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")),
            "a",
            1,
        ),
        (
            pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")),
            "b",
            0,
        ),
    ],
)
def test_min_mag(test_df, test_colname, expected):
    """Test min function works for array and zeroes and positive integers."""
    from lcanalyzer.models import min_mag

    assert min_mag(test_df, test_colname) == expected


@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (
            pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc")),
            "a",
            11 / 3,
        ),
        (
            pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc")),
            "b",
            0,
        ),
    ],
)
def test_mean_mag(test_df, test_colname, expected):
    """Test mean function works for array and zeroes and positive integers."""
    from lcanalyzer.models import mean_mag

    assert mean_mag(test_df, test_colname) == expected
