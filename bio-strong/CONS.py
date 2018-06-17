#!/usr/local/bin/python3

import sys

if len(sys.argv) != 2:
    print("Error - Usage: ./CONS.py [file]")
else:
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
    f.close()
    A, T, G, C, new_contents = [], [], [], [], []

    i = 0
    while i < len(contents):
        if contents[i][0] == ">":
            j = i + 1
            dna_string = ""
            while j < len(contents) and contents[j][0] != ">":
                dna_string += contents[j].strip("\n")
                j += 1
            new_contents.append(dna_string)
        i += 1

    for i in range(len(new_contents[0])):
        A.append(0)
        T.append(0)
        G.append(0)
        C.append(0)
    for cons in new_contents:
        for index in range(len(cons)):
            if cons[index] == "A":
                A[index] += 1
            elif cons[index] == "T":
                T[index] += 1
            elif cons[index] == "G":
                G[index] += 1
            elif cons[index] == "C":
                C[index] += 1
    consensus = ""
    for i in range(len(A)):
        value = max(A[i], T[i], G[i], C[i])
        if value == A[i]:
            consensus += "A"
        elif value == T[i]:
            consensus += "T"
        elif value == G[i]:
            consensus += "G"
        elif value == C[i]:
            consensus += "C"

    string_A, string_T, string_G, string_C = "", "", "", ""
    for i in A:
        string_A += str(i) + " "
    for i in T:
        string_T += str(i) + " "
    for i in G:
        string_G += str(i) + " "
    for i in C:
        string_C += str(i) + " "

    print(consensus)
    print("A:", string_A, "\nC:", string_C,
          "\nG:", string_G, "\nT:", string_T)
