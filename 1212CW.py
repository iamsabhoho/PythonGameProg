#validating an email address
import re
#it has to contain a '@'

def EmailValid():
    testing ='testing@gmail.com'
    check = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', testing)

    if check == None:
        print('This is bad syntax')
        raise ValueError('Bad syntax')


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
