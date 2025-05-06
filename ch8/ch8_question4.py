# return first non-duplicated letter in a string using hashmap in O(N)
# expected output is n
word = "minimum"

hash = {}

# add each letter in word to a hashmap and count occurences
for i in word:
    if i not in hash:
        hash[i] = 0
    hash[i] += 1

# iterate over hashmap and output the first key with a value of 1
for i in hash:
    if hash[i] == 1:
        print(i)
        break