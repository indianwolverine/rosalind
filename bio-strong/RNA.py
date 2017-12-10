def transcribe(str):
    rna = ''
    for c in str:
        if c == 'T':
            rna = rna + 'U'
        else:
            rna = rna + c
    print (rna)
