Playing around with my friend's last name

Essentially, this takes a bunch of words in the English language, filters them, and prints them out in a way involving some sort of wordplay.

This repo uses another repository with a list of English words.

Unfortunately, profanity_check has a multitude of warnings when imported. It's possible that this library won't be supported for too long.

Nameplay.py is the main script.
There is a private_vars.py file referenced that establishes a few private variables (i.e. path, etc.). This file is ignored by the gitignore, so the user should create the file themself and establish the variables.

word_writing.py is where the word filtering is configured. The words aren't filtered and written to a filtered.txt file until the nameplay.py file is run and the user agrees to the option of refreshing the filtered.txt file.