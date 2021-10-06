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