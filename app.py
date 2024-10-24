import random

while (True):
    option = input('Roll the Dice? (y/n): ')

    if (option.lower() == 'y'):
        dices = []
        dices.append(random.randint(1, 6))
        dices.append(random.randint(1, 6))

        print('({}, {})'.format(str(dices[0]), str(dices[1])))
    elif (option.lower() == 'n'):
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
