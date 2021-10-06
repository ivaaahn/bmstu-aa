from lib import simple_mul, win_mul_imp
from lib.types import MatrixInt


def test_square() -> None:
    lm, rm = MatrixInt(3, 3).fill_rand(), MatrixInt(3, 3).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)


def test_even() -> None:
    lm, rm = MatrixInt(2, 4).fill_rand(), MatrixInt(4, 6).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)


def test_odd() -> None:
    lm, rm = MatrixInt(3, 5).fill_rand(), MatrixInt(5, 7).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)


def test_vec_dot_mat() -> None:
    lm, rm = MatrixInt(1, 3).fill_rand(), MatrixInt(3, 1).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)

    lm, rm = MatrixInt(1, 3).fill_rand(), MatrixInt(3, 4).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)


def test_col_dot_vec() -> None:
    lm, rm = MatrixInt(3, 1).fill_rand(), MatrixInt(1, 5).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)


def test_single() -> None:
    lm, rm = MatrixInt(1, 1).fill_rand(), MatrixInt(1, 1).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)

    lm, rm = MatrixInt(1, 1).fill_rand(), MatrixInt(1, 2).fill_rand()
    assert simple_mul(lm, rm) == win_mul_imp(lm, rm)
