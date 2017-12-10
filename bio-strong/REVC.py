def reverse(string):
    string = string[::-1]
    return string

def revComp(str):
    rev = reverse(str)
    revComp = ''
    for c in rev:
        if c == 'A':
            revComp = revComp + 'T'
        if c == 'T':
            revComp = revComp + 'A'
        if c == 'G':
            revComp = revComp + 'C'
        if c == 'C':
            revComp = revComp + 'G'
    return revComp
