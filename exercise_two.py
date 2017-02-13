userFile = raw_input("Please enter a file name: ")
userData = raw_input("Enter contents: ")

helloFile = open(userFile, 'w')

helloFile.write(userData)

helloFile.close()
