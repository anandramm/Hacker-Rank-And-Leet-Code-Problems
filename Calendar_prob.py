import calendar

calendar.setfirstweekday(calendar.SUNDAY)
k=input().split()
month=int(k[0])
day=int(k[1])
year=int(k[2])

print(calendar.day_name[calendar.weekday(year,month,day)].upper())
