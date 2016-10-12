#Write a function for printing menus in the terminal.
#The input is a list of options, and the output is the option selected by the user.

print('The options are: ')
#list = input()
list = ['Meat','Chicken','Fish']
print(list)
print()

def options():
    for i in range(len(list)):
        option = i + 1
        print(str(option) + list[i])

    user = input('What is your preference? Press X to exit: ')
    if user == 'x':
        exit()
    elif user == '1':
        print(list[0])
        return user
    elif user == '2':
        print(list[1])
        return user
    else:
        print(list[2])
        return user
    return user

options()
