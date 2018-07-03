def successiveSum(n):
    if n == 1:
        return 1
    else:
        return successiveSum(n - 1) + n

def mendel(k, m, n):
    total = k + m + n
    totalChildren = successiveSum(total - 1) * 4
    totalDominant = successiveSum(k - 1) * 4 + successiveSum(m - 1) * 3 + k * m * 4 + k * n * 4 + m * n * 2

    return (totalDominant/totalChildren)
