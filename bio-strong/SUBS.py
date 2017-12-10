def subs(str, motif):
    i = 0
    while i < len(str):
        i = str.find(motif, i)
        if i == -1:
            break
        print(i + 1, end=' ')
        i += 1
