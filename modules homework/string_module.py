import string
import os

print(os.getcwd())
with open('modules homework/some.txt') as f:
  text = f.read().splitlines()

print(text)

lines = len(text)
words = sum(len(i.split()) for i in text)
characters = sum(len(i) for i in text)

print(lines)
print(words)
print(characters)

print('\n')

text2 = open('modules homework/some.txt').read()

print(text2)

string.ascii_letters #все буквы

