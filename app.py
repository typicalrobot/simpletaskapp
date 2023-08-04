user_input = 'random'
data = []


def menu_show():
    print('Menu:')
    print('1 - Add an item')
    print('2 - Mark as done')
    print('3 - View Items')
    print('4 - Exit')


while user_input != '4':

    menu_show()
    user_input = input('Enter your choice between 1 to 4 ')

    if user_input == '1':
        item = input('What is to be finished?  ')
        data.append(item)
        print('Added new item', item)
    elif user_input == '2':
        item = input('What is to be marked as done?  ')
        if item in data:
            data.remove(item)
            print('Removed item is: ')
        else:
            print('Item does not exist!')
    elif user_input == '3':
        print('List of items are: ')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Bye')
    else:
        print('Enter 1-4')