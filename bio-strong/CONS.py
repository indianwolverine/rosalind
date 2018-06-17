#!/usr/local/bin/python3

import sys

if len(sys.argv) != 2:
    print("Error: must provide fasta file as second argument")
else:
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    print(contents)
