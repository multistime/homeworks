x=input("input string 1:")

y=input("input string 2:")

x=str(x)
y=str(y)

Y=(y[::-1])

print(x)
print(y)
print(Y)

if x==Y:
    print("It's palindrome!")
else:
    print('not today...')