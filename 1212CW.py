#validating an email address

#it has to contain a '@'

email = input('Please enter an email address: ')

#only one @
#no spaces
#no special charaters

invalidCh = "#%:;,!?-$"
for word in email:
    for ch in word:
        if ch in invalidCh:
            print('This is a invalid email address')
        elif email.count('@') > 1:
            print('This is a invalid email address')





#Write another Python function to validate the input of a date in format yyyy-mm-dd.
# Test your function and indicate the exceptions included (if any).

import datetime

def validate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        print('This is the correct format')
    except ValueError:
        raise ValueError('This is in a incorrect format')


validate('1999-11-07')
