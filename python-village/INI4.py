def oddSum(a, b):
    if (a % 2 != 0):
        a -= 1
    if (b % 2 != 0):
        b += 1
    return ((b/2) * (b/2) - (a/2) * (a/2))
