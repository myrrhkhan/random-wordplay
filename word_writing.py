#Use this file to establish your criteria.

def conditions(word):
    #Establish conditions here
    from profanity_check import predict
    if word[-2:len(word)] == "er" and predict([word]) == 0: return True
    else: return False

def write_words(): #Imports words, puts them through a profanity filter, writes them to filtered words file. Optional
    file = 'english-words\\words_alpha.txt' #Original file.
    with open(file) as word_file:
        valid_words = [word for word in list(word_file.read().split()) if conditions(word) == True]
        #Takes each word from the original file. Adds them into a list if the last two letters are "er" and if the word is not profane.
    with open('filtered.txt', 'w+') as filter_file:
        for word in valid_words: filter_file.write(word + "\n") #Opens the filtered.txt file and writes the list of words into the file.
    print("Successfully written filtered.txt")
    f = open("filtered.txt")
    print(f.read())