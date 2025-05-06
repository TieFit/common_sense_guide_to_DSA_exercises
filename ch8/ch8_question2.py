# return the first duplicate value found in O(N) using a hashmap
arr = ["a", "b", "c", "d", "c", "e", "f"]

hash = {}

# add current index to hash if not already in hashmap. if value already exists then print the pre-existing value and break loop
for i in arr:
    if i not in hash:
        hash[i] = i
    elif i in hash:
        print(i)
        break