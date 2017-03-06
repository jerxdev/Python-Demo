aFile = open("Hobbit.txt", "r+")

information = aFile.read();


print("Total number of sentences: ", information.count('.') +
      information.count('!') + information.count('?') -
      information.count('Mr.'))
