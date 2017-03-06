def lineaverages(filename):
    averages = []
    with open("numbers.txt") as f:
        for line in f.readlines():
            numbers = [int(x) for x in line.split(',')]
            averages.append(sum(numbers) / float(len(numbers)))
    return averages
print (lineaverages("numbers.txt"))
