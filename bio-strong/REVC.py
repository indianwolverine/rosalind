def reverse(string):
    string = string[::-1]
    return string

def revComp(str):
    rev = reverse(str)
    revComp = ''
    for c in rev:
        if c == 'A' or c == "a":
            revComp = revComp + 'T'
        if c == 'T' or c == "t":
            revComp = revComp + 'A'
        if c == 'G' or c == "g":
            revComp = revComp + 'C'
        if c == 'C' or c == "c":
            revComp = revComp + 'G'
    return revComp
