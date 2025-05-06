# string will contain all letters in alphabet except one, identify which letter is missing in O(N) using hashmap

import string
# quick way of creating a hashmap that contains every letter in alphabet
hash = {letter: 0 for letter in string.ascii_lowercase}

sentence = "the quick brown box jumps over a lazy dog"

# every time a letter is iterated over, it will increment the value of said letter by 1. Since only 1 letter is missing
# this means that the only key:value pair with a value of 0 is the missing letter
for i in sentence:
    if i in hash:
        hash[i] += 1

# search hashmap for key:value pair with a value of 0 and print what said key is
for i in hash:
    if hash[i] == 0:
        print(i)
        break