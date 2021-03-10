inp = input('Enter score: ' )
try:
    s = float(inp)
except :
    print('Bad Score')
    quit()

def computegrade(score):
    if score > 1:
        return 'Bad score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score >= 0:
        return 'F'
    else:
        return 'Bad score'

grade = computegrade(s)

print(grade)
