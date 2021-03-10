def countletter(word, char):
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(count)

word = input('Word: ')

char = input('Letter to count: ')

countletter(word, char)
