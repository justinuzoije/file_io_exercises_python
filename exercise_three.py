def letter_histogram(word):
    letterDict = {}
    for char in word:
        #The key is the character
        #The value is given the default value of 0 if it is not there
        #The value is then given + 1 to increase it
        #The key-value pair is the letter and the number of times it appears
        letterDict[char] = letterDict.get(char, 0) + 1

    print letterDict

def word_histogram(paragraph):
    wordCount = {}
    splitParagarph = paragraph.split()

    for word in splitParagarph:
        wordCount[word] = wordCount.get(word, 0) + 1

    print wordCount

userFile = raw_input("Please enter the file name: ")
helloFile = open(userFile)
fileData = helloFile.read()

print "Letter Histogram Data"
letter_histogram(fileData)

print ""

print "Word Histogram Data"
word_histogram(fileData)

#print letter_histogram(fileContents)
#print word_histogram(fileContents)

helloFile.close()
