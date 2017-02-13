userFile = raw_input("Enter file name to read: ")

helloFile = open(userFile)
fileContents = helloFile.read()

print fileContents
