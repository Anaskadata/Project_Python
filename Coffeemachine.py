user_input = 'random'
data = []

def display_menu():
    print('Menu: ')
    print('1. Buy a drink')
    print('2. Espresso')
    print('3. Americano')
    print('4. Cappuccino')
    print('5. Latte')
    print('6. View the list of drinks')
    print('7. Remove a drink from the list')
    print('8. Finish')

while user_input != '8':

    display_menu()
    user_input = input('Enter your choice: ')

    if user_input == '1':
        print('What drink would you like to buy? Enter your choice: ')
        x = input()

        if x == '2':
            item = 'Espresso'
        elif x == '3':
            item = 'Americano'
        elif x == '4':
            item = 'Cappuccino'
        elif x == '5':
            item = 'Latte'
        elif x == '6':
            item = ''
        elif x == '7':
            item = ''
        elif x == '8':
            item = ''
        data.append(item)
        print('Added item: ' + item)        
                                                   
    elif user_input == '6':
        print('List of drinks to buy: ')
        for item in data:
            print(item)        
    elif user_input == '7':
        item = input('What should be removed from the list? Enter the name of a drink: ')        
        if item in data:
            data.remove(item)
            print('Removed drink: ', item)
        else:
            print('Drink doesn`t exist in the list')
    elif user_input == '8':
        print('Goodbye!')
    else:
        print('Please enter 1, 2, 3, 4, 5, 6, 7 or 8')
   
