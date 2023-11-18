class tables:
    # Class tables
    def __init__(self, number,waiter=None, assigned=False, NumCustomers=0, bill=False):
        self.waiter = waiter
        self.assigned = assigned
        self.NumCustomers = NumCustomers
        self.tableNumber = number
        self.order = []
        self.bill = bill




    def isAssigned(self,waiter):
        # Assigning table to waiter function
        if self.assigned == True:
            print(f' table {self.tableNumber} is already assigned to {waiter}')
            from summative1 import Login
            Login()


        elif self.assigned == False:
             self.waiter = waiter
             self.assigned = True

             print(f' table {self.tableNumber} is now assigned to {waiter}')




    def addCustomers(waiter):
        # Adding customers function
        question = input('Do you want to add customers to the table? (y/n)\n')

        if question == 'y':
            table_numbers = []
            for i in list:
                if i.waiter == waiter:
                    table_numbers.append(i)

            for table_number in table_numbers:
                print('Table', str(table_number.tableNumber))

            ask = int(input('Which table do you want to change customers?\n'))

            found_table = False
            for i in table_numbers:
                if ask == i.tableNumber:
                    amount = int(input('How many customers? \n'))
                    i.NumCustomers = amount

                    print(f"There are now {i.NumCustomers} customers at table {i.tableNumber} ")

                    found_table = True
                    break

            if not found_table:
                print(f"Table {ask} was not found.")


        elif question == 'n':
            pass




        else:
            print('please enter a valid option')
            tables.addCustomers(waiter)


    def add_order(self, item, quantity, price):
        # Appending orders to table Object
        order = {"item": item, "quantity": quantity, "price": price}
        self.order.append(order)

    def prepare_bill(self):
        total_price = 0
        for order in self.order:
            quantity = order["quantity"]
            price = float(order["price"])
            total_price += order["price"]
        return total_price



 #  ANSI escape codes to add colour to prints
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Formatting
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

# Create  table objects from the class

table1 = tables(1)
table2 = tables(2)
table3 = tables(3)
table4 = tables(4)
table5 = tables(5)
table6 = tables(6)

# List containing table Objects
list = [table1,table2,table3,table4,table5,table6]


