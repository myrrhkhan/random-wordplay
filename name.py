import random
def load_words():
    file = 'english-words\\words.txt'
    with open(file) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()
for i in range(input("input how many times this process should be repeated: ")):
    print(random(english_words))