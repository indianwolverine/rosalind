def evenLines(file):
    i = 1
    f = open(file, 'r')
    for line in f.readlines():
        if i % 2 == 0:
            print (line)
        i += 1
