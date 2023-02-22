from datetime import date

dateraw = date.today()
dateraw = str(dateraw)

i = 0
datestring = ''
while i < len(dateraw):
    if dateraw[i] == '-':
        datestring = datestring + '/'
    else:
        datestring = datestring + dateraw[i]
    i += 1

print(datestring)