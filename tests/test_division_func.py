from my_funcs.utils import division
import pytest


@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 10, 2),
                                          (10, 5, 2),
                                          (20, 4, 5),
                                          (20, 2, 10),
                                          (200, 4, 50)])
def test_division_positive(a, b, result):
    assert division(a, b) == result


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert division(10, 0)


@pytest.mark.parametrize("exception, divisionable, divider",
                         [(ZeroDivisionError, 10, 0),
                          (TypeError, 20, "2")])
def test_type_error(exception, divisionable, divider):
    with pytest.raises(exception):
        assert division(divisionable, divider)
