def hamming(str, str2):
    count = 0
    for i in range(len(str)):
        if str[i] != str2[i]:
            count = count + 1
    return count
