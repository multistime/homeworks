import calendar

calendar.setfirstweekday(0)

bday = input('enter your birthday date DD.MM.YYYY:')

print(bday)
print('\nВы родились:')

bdaysplit = bday.split(".")

print(bdaysplit)

day=int(bdaysplit[0])
month=int(bdaysplit[1])
year=int(bdaysplit[2])

print('\nэто был:')
print(calendar.day_name[calendar.weekday(year, month, day)])