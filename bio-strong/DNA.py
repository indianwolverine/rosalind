def basePairCount(str):
    count = {
        'A': 0,
        'T': 0,
        'G': 0,
        'C': 0
    }
    for c in str:
        count[c] += 1
    print(count['A'], count['C'], count['G'], count['T'])
