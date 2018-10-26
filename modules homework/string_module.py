import string

with open('some.txt') as f:
  text = f.read().splitlines()

print(text)

lines = len(text)
words = sum(len(i.split()) for i in text)
characters = sum(len(i) for i in text)

print(lines)
print(words)
print(characters)

print('\n')

text2 = open('some.txt').read()

print(text2)