def GC(str):
    GC = 0.0
    total = len(str)
    for c in str:
        if c == 'G':
            GC = GC + 1
        if c == 'C':
            GC = GC + 1
    content = GC / total * 100
    return content
