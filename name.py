import random; import pandas as pd
def write_words(): #Imports words, puts them through a profanity filter, writes them to filtered words file. Optional
    from profanity_check import predict #imported here instead of at the top because there are a bunch of warnings when imporint :(
    file = 'english-words\\words_alpha.txt' #Original file.
    with open(file) as word_file:
        valid_words = [word for word in list(word_file.read().split()) if word[-2:len(word)] == "er" and predict([word]) == 0]
        #Takes each word from the original file. Adds them into a list if the last two letters are "er" and if the word is not profane.
    with open('filtered.txt', 'w+') as filter_file:
        for word in valid_words: filter_file.write(word + "\n") #Opens the filtered.txt file and writes the list of words into the file.
    
def load_words(): #Loads the words in the filtered words file.
    with open('filtered.txt') as file:
        valid_words = list(file.read().split())
    return valid_words

if input("Would you like to refresh your words list? yes if you do, anything else if not. ") == "yes": write_words() #Asks if you'd like to refresh the words.

english_words = load_words() #sets the laoded words as a list variable.
i = int(input("How many words? "))
list = []; f = 0 #makes a list, starts the counter at 0.
while f < i: #While there aren't enough words
    item = english_words[random.randint(0, len(english_words))] #chooses random word from the list by randomly picking an index.
    list.append("Kai " + item + "strom"); f += 1 #Adds this to the list.
print(list) #Prints list for confirmation.
if input("would you like to copy this as multiple lines or no? ") == "yes" or "": df=pd.DataFrame([list]) #Copy as multiple lines
else: df=pd.DataFrame(list) #copy as one line
df.to_clipboard(index=False, header=False) #copy to clipboard