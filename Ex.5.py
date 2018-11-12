string1 = input('string1:')
string2 = input('string2:')

x = (string2 in string1)

if x == True:
    print('match!')
else:
    print('no matches')