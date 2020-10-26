import random, pandas as pd, os, private_vars, word_writing
os.chdir(private_vars.path)

def load_words(): #Loads the words in the filtered words file.
    with open('filtered.txt') as file:
        valid_words = list(file.read().split())
    return valid_words

i = int(input("How many words? ")) #put this before refresh so that everyting is just "enter"

if input("Would you like to refresh your words list? yes if you do, anything else if not. ") == "yes": 
    word_writing.write_words() #Asks if you'd like to refresh the words.

english_words = load_words() #sets the laoded words as a list variable.

list = []; f = 0 #makes a list, starts the counter at 0.

while f < i: #While there aren't enough words
    item = english_words[random.randint(0, len(english_words))] #chooses random word from the list by randomly picking an index.
    list.append(private_vars.print_mod(item)); f += 1 #Adds this to the list.

print(list) #Prints list for confirmation.
if input("would you like to copy this as multiple lines or no? ") == "yes" or "": 
    df=pd.DataFrame([list]) #Copy as multiple lines
else: 
    df=pd.DataFrame(list) #copy as one line
df.to_clipboard(index=False, header=False) #copy to clipboard