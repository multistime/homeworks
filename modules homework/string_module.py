import string
import os

print(os.getcwd())
with open('modules homework/some.txt') as f:
  text = f.read().splitlines()

print(text)

lines = len(text)
words = sum(len(i.split()) for i in text)
# не совсем то, что нужно было
# нужно было найти все буквы, которые используются в тексте,
# и посчитать, сколько раз каждая из них встречается
characters = sum(len(i) for i in text)

print(lines)
print(words)
print(characters)

print('\n')

text2 = open('modules homework/some.txt').read()

print(text2)

string.ascii_letters #все буквы

