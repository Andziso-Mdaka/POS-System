# importing class and objects to main file

from customerClass import tables
from customerClass import table1
from customerClass import table2
from customerClass import table3
from customerClass import table4
from customerClass import table5
from customerClass import table6

# importing colors
from  customerClass import RED
from  customerClass import GREEN
from  customerClass import MAGENTA
from  customerClass import BLUE
from  customerClass import CYAN
from  customerClass import RESET
from  customerClass import BOLD

# initialise global variable for total sales
dailyTotal = 0



def LoginMenu():
    # Login Menu for waiters

    print(f'{MAGENTA} {BOLD}Welcome to Highlands Cafe \n {RESET}')
    print(f'{GREEN}1. Login {RESET}')
    print(f'{CYAN}2. Exit {RESET}')

    choice = int(input('select a choice:\n'))

    if choice == 1:
        Login()

    elif choice == 2:
        exit()

    else:
        print('select a valid option ')
        LoginMenu()


def Login():
    # login function to test username and password against textfile login information
    global username
    while True:
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        with open("Login.txt", "r") as file:
            for line in file:
                FileUsername, FilePassword = line.strip().split(",")

                if username == FileUsername and password == FilePassword:
                    print(f'Welcome, {username}!\n')
                    return  # Exit the Login function and proceed to MainMenu()

        print('Invalid username or password. Please try again.\n')





def MainMenu():
    # Main Menu Function after Login is successful
    print('what would you like to do today? \n')
    print('1. Assign Table')
    print('2. Change customers')
    print('3. Add to Order')
    print('4. Prepare bill')
    print('5. Complete Sale')
    print('6. Cashup')
    print('0. Log Out \n')

    action = int(input('select an option'))

    if action == 1:
        print('please select one of the available tables or press 0 to exit \n')
        print('1. Table 1')
        print('2. Table 2')
        print('3. Table 3')
        print('4. Table 4')
        print('5. Table 5')
        print('6. Table 6 \n')
        print('0. Exit')

        pick = int(input('select a table'))

         # assigning tables to waiters

        if pick == 1:

            tables.isAssigned(table1,username)
            tables.addCustomers(username)
            MainMenu()

        elif pick == 2:

            tables.isAssigned(table2, username)
            tables.addCustomers(username)
            MainMenu()
        elif pick == 3:

            tables.isAssigned(table3, username)
            tables.addCustomers(username)
            MainMenu()
        elif pick == 4:

            tables.isAssigned(table4, username)
            tables.addCustomers(username)
            MainMenu()
        elif pick == 5:

            tables.isAssigned(table5, username)
            tables.addCustomers(username)
            MainMenu()
        elif pick == 6:

            tables.isAssigned(table6, username)
            tables.addCustomers(username)
            MainMenu()
        elif pick == 0:
            exit()
        else:
            print('please enter a valid input')
            MainMenu()

    elif action == 2:

        # Changing customers in a table
        from customerClass import list

        table_numbers = []
        for i in list:
            if i.waiter == username:
                table_numbers.append(i)

        for table_number in table_numbers:
            print('Table', str(table_number.tableNumber))

        ask = int(input('Which table do you want to change customers?\n'))

        found_table = False
        for i in table_numbers:
            if ask == i.tableNumber:
                amount = int(input('How many customers are seated at the table?\n'))
                i.NumCustomers = amount

                print(f"There are now {i.NumCustomers} customers at table {i.tableNumber}")
                MainMenu()
                found_table = True
                break

        if not found_table:
            print(f"Table {ask} was not found.")
            MainMenu()

    elif action == 3:
        # Adding Orders to Tables
        print('Select a table to add orders to:')
        from customerClass import list

        table_numbers = []
        for i in list:
            if i.waiter == username:
                table_numbers.append(i)

        for table_number in table_numbers:
            print('Table', str(table_number.tableNumber))

        ask = int(input('Select a Table\n'))

        found_table = False
        for i in table_numbers:
            if ask == i.tableNumber:

                with open('Stock.txt', 'r') as file:
                    contents = file.readlines()

                orders = []
                for line in contents:
                    item, price = line.strip().split(',')
                    orders.append((item, float(price)))

                # Display the available items
                print("Available Items:")
                for index, order in enumerate(orders):
                    print(f"{index + 1}. {order[0]} - R{order[1]}")

                # Prompt the user to select an item
                selected_item = None
                while selected_item is None:
                    try:
                        choice = int(input("Select an item number to order: "))
                        if 1 <= choice <= len(orders):
                            selected_item = orders[choice - 1]
                        else:
                            print("Invalid choice. Please enter a valid item number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid item number.")

                # Prompt the user to enter the quantity
                quantity = None
                while quantity is None:
                    try:
                        quantity = int(input("Enter the quantity: "))
                        if quantity <= 0:
                            print("Invalid quantity. Please enter a positive number.")
                            quantity = None
                    except ValueError:
                        print("Invalid input. Please enter a valid quantity.")

                # Calculate the total price
                total_price = selected_item[1] * quantity

                # Print the order details
                print(f"You have selected: {selected_item[0]} - R{selected_item[1]}")
                print(f"Quantity: {quantity}")
                print(f"Total Price: R{total_price}")

                tables.add_order(i,selected_item[0],quantity,total_price)


                MainMenu()
                found_table = True
                break

        if not found_table:
            print(f"Table {ask} was not found.")
            MainMenu()


    elif action == 4:
        # Preparing bills for table orders
        print('which table would you like to prepare bill')
        from customerClass import list

        table_numbers = []
        for i in list:
            if i.waiter == username:
                table_numbers.append(i)

        for table_number in table_numbers:
            print('Table', str(table_number.tableNumber))

        ask = int(input('Which table\'s bill do you want to print?\n'))

        found_table = False
        for i in table_numbers:
            if ask == i.tableNumber:



                def prepareBill():

                    global total

                    total = tables.prepare_bill(i)

                   # Structure of the bill
                    print(f'\n{GREEN}------------------------------------------------------------------------{RESET}')
                    print(f'The bill for table {i.tableNumber} ')

                    print('Item              Quantity           Price')
                    for order in i.order:
                        item = order['item']
                        quantity = order['quantity']
                        price = order['price']
                        print(f'{item:20} {quantity}              R{price:.2f}')

                    print(f"\n The Total cost of Table {i.tableNumber} is R{total}")
                    print(f' you were helped by {username}')
                    print(f'{BLUE}-------------------------------------------------------------------------\n{RESET}')

                    i.bill = True


                prepareBill()







                MainMenu()
                found_table = True
                break

        if not found_table:
            print(f"Table {ask} was not found.")
            MainMenu()

    elif action == 5:


        # Completing Sales for Tables
        from customerClass import list

        table_numbers = []
        for i in list:
            if i.waiter == username:
                table_numbers.append(i)

        for table_number in table_numbers:
            print('Table', str(table_number.tableNumber))

        if not table_numbers:
            print(f'{RED}Please prepare bill before completing sale!{RESET}')
            MainMenu()



        ask = int(input('Select a Table to complete sale\n'))

        found_table = False
        for i in table_numbers:
            if ask == i.tableNumber:
                if i.bill == False:
                    print(f'{RED}Please prepare bill before completing sale!{RESET}')
                    MainMenu()
                elif i.bill == True:

                     # waiter prompted for a filename
                    Filename = input('enter a filename:')


                    total = tables.prepare_bill(i)

                      # Contents of the bill written to the file
                    with open(Filename, "w") as file:
                        file.write('-----------------------------------------------------------\n')
                        file.write(f'The bill for table {i.tableNumber}\n')
                        file.write('Item              Quantity           Price\n')

                        for order in i.order:
                            item = order['item']
                            quantity = order['quantity']
                            price = order['price']
                            file.write(f'{item:20} {quantity}              R{price:.2f}\n')

                        file.write(f'\nThe Total cost of Table {i.tableNumber} is R{total}\n')
                        file.write(f'You were helped by {username}\n')
                        file.write(f'-----------------------------------------------------------\n')

                    print(f"{BLUE}The file '{Filename}' has been created.{RESET}")

                    global  dailyTotal

                    dailyTotal = 0

                    dailyTotal = dailyTotal + total
                    # orders cleared and removing waiter assignment for the table
                    i.order.clear()
                    i.waiter = None
                    MainMenu()








    elif action == 6:
        #Cahup Function
        def CashUp():
            global dailyTotal

            # Displaying total for all sales completed

            print(f'Today we made R{dailyTotal}')

            clear = input('do you wish to clear the daily total?(y/n)')

            if clear == 'y':
                dailyTotal = 0
                MainMenu()
            elif clear == 'n':
                MainMenu()
            else:
                print('please enter a valid input')
                CashUp()
        CashUp()








    elif action == 0:
        print('GoodBye!')
        LoginMenu()

    else:
        print('enter a valid option')
        MainMenu()




LoginMenu()

MainMenu()





