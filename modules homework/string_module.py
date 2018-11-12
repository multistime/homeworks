from string import ascii_letters

# 1
with open('/Users/multistime/PycharmProjects/GitHub/modules homework/some.txt', 'r') as f:
    text = f.read()

print('Текст:')
print(text)
print()

# 2
words = text.split()
print('Количество слов: %d' % len(words))
print()

# 3
counts = dict()
for ch in text:
    if ch not in ascii_letters:
        continue
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

for ch, count in counts.items():
    print('%s встречается %d раз' % (ch, count))

print()

# 4
lines = text.splitlines(True)
split = len(lines) // 2
lines = lines[:split] + lines[split:]
text = ''.join(lines)
print(text)

with open('/Users/multistime/PycharmProjects/GitHub/modules homework/some.txt', 'w') as f:
    f.write(text)