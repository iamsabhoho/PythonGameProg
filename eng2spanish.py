'''eng2spa = {'one': 'uno', 'two': 'dos','three': 'tres','four':'cuatro','five':'cinco',
           'six':'seis','seven':'siete','eight':'ocho','nine':'nueve','ten':'diez'}

user = input('Please enter a number in spanish: ')
x = eng2spa.values()

if user in x:
    print('yes')
else:
    print('no')'''

def generateModel(text):
   model = {}
   for i in range(len(text) - 1):
       fragment = text[i:i+1]
       next_letter = text[i+1]
       if fragment not in model:
           model[fragment] = {}
       if next_letter not in model[fragment]:
           model[fragment][next_letter] = 1
       else:
           model[fragment][next_letter] += 1
   return model

generateModel()
