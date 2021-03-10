total = 0
count = 0
average = 0

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
        total = total + num
        count = count + 1
        average = total / count

print('Total:', total, 'Count:', count, 'Average:',average)
