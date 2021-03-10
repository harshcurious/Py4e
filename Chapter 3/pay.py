inpHours = input('Enter Hours: ')

try:
    hour = float(inpHours)
except:
    print('Error, please enter numeric input')
    exit(0)

inpRate = input('Enter Rate: ')

try:
    rate = float(inpRate)
except:
    print('Error, please enter numeric input')
    exit(0)

if hour <= 40 :
    pay = rate * hour
else:
    pay = (rate * 40) + (1.5*rate*(hour-40))
print('Pay:', pay)
