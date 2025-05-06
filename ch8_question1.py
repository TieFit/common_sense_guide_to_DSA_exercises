# return intersection of two arrays in O(N) time, intersection of these two arrays is 2, 4

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]

hash = {}
intersection = {}

# iterate over first array and add all values to a hashmap for later use
for i in arr1:
    if i not in hash:
        hash[i] = i
# iterate over second array and cross reference all values in hash from array 1 against values in array 2. matching values are added
# to intersection hashmap
for j in arr2:
    if j in hash:
        intersection[j] = j

print(intersection)