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

def computepay(h, r):
    if h <= 40 :
        pay = r * h
    else:
        pay = (r * 40) + (1.5*r*(h-40))
    print('Pay:', pay)

computepay(hour, rate)
