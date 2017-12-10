def wordCount(str):
    dict = {}
    arr = str.split(' ')
    for word in arr:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    for key, value in dict.items():
        print (key, value)
