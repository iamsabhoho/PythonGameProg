wordbank = []
L = False
valid = []

n = int(input())
for i in range(n):
    w = input()
    wordbank.append(w)

letters = input()
tempL = letters

for word in wordbank:
    for char in word.lower():
        if char in tempL:
            inLetters = True
            tempL = tempL.replace(char, '', 1)
        else:
            inLetters = False
            break
    if L:
        valid.append(word)
    L = False
    tempL = letters

points = 0
highscore = 0
finalword = ""
#check for the valid chars
for word in valid:
    for char in word:
        if char in 'eaionrtlsu':
            points += 1
        elif char in 'dg':
            points += 2
        elif char in 'bcmp':
            points += 3
        elif char in 'fhvwy':
            points += 4
        elif char in 'k':
            points += 5
        elif char in 'jx':
            points += 8
        elif char in 'qz':
            points += 10
    if points > highscore:
        finalWord = word
        highscore = points
    points = 0
print(finalWord)
