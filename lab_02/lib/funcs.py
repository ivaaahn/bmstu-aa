from .types import MatrixInt, VectorInt

__all__ = ['simple_mul', 'win_mul', 'win_mul_imp']


def simple_mul(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    m, n, q = lm.m, lm.n, rm.n
    res = MatrixInt(m, q)

    i = 0
    while i < m:
        j = 0
        while j < q:
            k = 0
            while k < n:
                res[i][j] += lm[i][k] * rm[k][j]
                k += 1
            j += 1
        i += 1

    return res


def _fill_mul_h(mul_h: VectorInt, matrix: MatrixInt) -> None:
    m, n = matrix.m, matrix.n

    i = 0
    while i < m:
        k = 0
        while k < n // 2:
            mul_h[i] = mul_h[i] + matrix[i][2 * k] * matrix[i][2 * k + 1]
            k += 1
        i += 1


def _fill_mul_v(mul_v: VectorInt, matrix: MatrixInt) -> None:
    n, q = matrix.m, matrix.n

    i = 0
    while i < q:
        k = 0
        while k < n // 2:
            mul_v[i] = mul_v[i] + matrix[2 * k][i] * matrix[2 * k + 1][i]
            k += 1
        i += 1


def win_mul(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    m, n, q = lm.m, lm.n, rm.n

    mul_h = VectorInt(m)
    _fill_mul_h(mul_h, lm)

    mul_v = VectorInt(q)
    _fill_mul_v(mul_v, rm)

    res = MatrixInt(m, q)
    i = 0
    while i < m:
        j = 0
        while j < q:
            k = 0
            res[i][j] = - mul_h[i] - mul_v[j]
            while k < n // 2:
                res[i][j] = res[i][j] \
                            + (lm[i][2 * k] + rm[2 * k + 1][j]) \
                            * (lm[i][2 * k + 1] + rm[2 * k][j])
                k += 1
            j += 1
        i += 1

    if n % 2 == 1:
        i = 0
        while i < m:
            j = 0
            while j < q:
                res[i][j] = res[i][j] + lm[i][n - 1] * rm[n - 1][j]
                j += 1
            i += 1
    return res


def _fill_mul_h_imp(mul_h: VectorInt, matrix: MatrixInt) -> None:
    m, n = matrix.m, matrix.n

    i = 0
    while i < m:
        buf, k = 0, 1
        while k < n:
            buf -= matrix[i][k - 1] * matrix[i][k]
            k += 2
        mul_h[i] = buf
        i += 1


def _fill_mul_v_imp(mul_v: VectorInt, matrix: MatrixInt) -> None:
    n, q = matrix.m, matrix.n

    i = 0
    while i < q:
        buf, k = 0, 1
        while k < n:
            buf -= matrix[k - 1][i] * matrix[k][i]
            k += 2
        mul_v[i] = buf
        i += 1


def win_mul_imp(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    m, n, q = lm.m, lm.n, rm.n

    mul_h = VectorInt(m)
    _fill_mul_h_imp(mul_h, lm)

    mul_v = VectorInt(q)
    _fill_mul_v_imp(mul_v, rm)

    is_odd = n & 1
    res = MatrixInt(m, q)
    i = 0
    while i < m:
        j = 0
        while j < q:
            buf, k = mul_h[i] + mul_v[j], 1
            while k < n:
                buf += (lm[i][k - 1] + rm[k][j]) * (lm[i][k] + rm[k - 1][j])
                k += 2
            if is_odd == 1:
                buf += lm[i][n - 1] * rm[n - 1][j]

            res[i][j] = buf
            j += 1
        i += 1

    return res
