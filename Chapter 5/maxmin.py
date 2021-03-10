max = None
min = None

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    else:
        try:
            num = float(inp)
        except:
            print('Invalid input')
            continue
        if max is None or num > max:
            max = num
        if min is None or num < min:
            min = num

print('Max:', max, 'Min:', min)
