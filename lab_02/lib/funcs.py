from .types import MatrixInt, VectorInt


def simple_mul(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    resm = MatrixInt(lm.m, rm.n)

    i = 0
    while i < resm.m:
        j = 0
        while j < resm.n:
            k = 0
            while k < lm.n:
                resm[i][j] = resm[i][j] + lm[i][k] * rm[k][j]
                k += 1
            j += 1
        i += 1

    return resm


def _calc_win_rows(m: MatrixInt) -> VectorInt:
    cf = VectorInt(m.m)

    i = 0
    while i < m.m:
        k = 0
        while k < m.n // 2:
            cf[i] = cf[i] + m[i][2 * k] * m[i][2 * k + 1]
            k += 1
        i += 1

    return cf


def _calc_win_rows_imp(m: MatrixInt) -> VectorInt:
    cf = VectorInt(m.m)

    i = 0
    while i < m.m:
        buf, k = 0, 0
        while k < m.n:
            buf -= m[i][k] * m[i][k + 1]
            k += 2
        cf[i] = buf
        i += 1

    return cf


def _calc_win_cols(m: MatrixInt) -> VectorInt:
    cf = VectorInt(m.n)

    i = 0
    while i < m.n:
        k = 0
        while k < m.m // 2:
            cf[i] = cf[i] + m[2 * k][i] * m[2 * k + 1][i]
            k += 1
        i += 1

    return cf


def _calc_win_cols_imp(m: MatrixInt) -> VectorInt:
    cf = VectorInt(m.n)

    i = 0
    while i < m.n:
        buf, k = 0, 0
        while k < m.m:
            buf -= m[k][i] * m[k + 1][i]
            k += 2
        cf[i] = buf
        i += 1

    return cf


def win_mul(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    resm = MatrixInt(lm.m, rm.n)

    mul_h = _calc_win_rows(lm)
    mul_v = _calc_win_cols(rm)

    i = 0
    while i < resm.m:
        j = 0
        while j < resm.n:
            k = 0
            resm[i][j] = - mul_h[i] - mul_v[j]
            while k < lm.n // 2:
                resm[i][j] = resm[i][j] \
                             + (lm[i][2 * k] + rm[2 * k + 1][j]) \
                             * (lm[i][2 * k + 1] + rm[2 * k][j])
                k += 1
            j += 1
        i += 1

        if lm.n % 2:
            i = 0
            while i < resm.m:
                j = 0
                while j < resm.n:
                    resm[i][j] = resm[i][j] \
                                 + lm[i][lm.n - 1] \
                                 * rm[lm.n - 1][j]
                    j += 1
                i += 1

    return resm


def win_mul_imp(lm: MatrixInt, rm: MatrixInt) -> MatrixInt:
    resm = MatrixInt(lm.m, rm.n)

    is_odd = lm.n % 2
    n_minus_one = lm.n - 1

    mul_h = _calc_win_rows_imp(lm)
    mul_v = _calc_win_cols_imp(rm)

    i = 0
    while i < resm.m:
        j = 0
        while j < resm.n:
            buf, k = mul_h[i] + mul_v[j], 0
            while k < lm.n:
                buf += (lm[i][k] + rm[k + 1][j]) * (lm[i][k + 1] + rm[k][j])
                k += 2
            if is_odd:
                buf += lm[i][n_minus_one] * rm[n_minus_one][j]

            resm[i][j] = buf
            j += 1
        i += 1

    return resm
