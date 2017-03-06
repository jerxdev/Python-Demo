def wcount(filename):
    count = 0
    aFile = open(filename, "r+")
    information = aFile.readlines()
    aFile.close()
    for i in information:
        i = i.split()
        count+=len(i)
    return count

print(wcount("words.txt"))
