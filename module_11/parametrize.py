import pytest as pytest


def calc(num_a, num_b, operation):
    return eval(str(num_a) + operation + str(num_b))


# @pytest.mark.parametrize("num_a, num_b, expected", [(2, 2, 4)])
# def test_summ(num_a, num_b, expected):
#     assert calc(num_a, num_b, "+") == expected
#
#
# @pytest.mark.parametrize("num_a, num_b, expected", [(2, 0, 2), (2, 2, 0)])
# def test_sub(num_a, num_b, expected):
#     assert calc(num_a, num_b, "-") == expected
#
#
# @pytest.mark.parametrize("num_a, num_b, expeced", [(6, 7, 42)])
# def test_mult(num_a, num_b, expeced):
#     assert calc(num_a, num_b, "*") == expeced
#
#
# @pytest.mark.parametrize("num_a, num_b, expeced", [(1, 1, 1)])
# def tets_div(num_a, num_b, expeced):
#     assert calc(num_a, num_b, "/") == expeced


@pytest.mark.parametrize(
    "num_a,num_b,operation,expected",
    [
        (2, 2, "+", 4),
        (2, 0, "-", 2),
        (6, 7, "*", 42),
        (1, 1, "/", 1)
    ]
)
def test_eval(num_a, num_b, operation, expected):
    assert calc(num_a, num_b, operation) == expected
