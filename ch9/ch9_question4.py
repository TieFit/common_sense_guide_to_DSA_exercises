# use a stack to reverse a string
# strings are immutable in python so characters in string must first be appended to an array (stack)
word = "abcde"
stack = []
for letter in word:
    stack.append(letter)

# while len(stack) > 0, pop last letter in stack and add to reversed string
rev = ''
while stack:
    rev += stack.pop()
print(rev)