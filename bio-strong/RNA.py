def transcribe(str):
    """
    Returns RNA transcription of a given DNA string STR.

    >>> transcribe('ATGC')
    AUGC

    """
    rna = ''
    for c in str:
        if c == 'T':
            rna = rna + 'U'
        else:
            rna = rna + c
    print (rna)
