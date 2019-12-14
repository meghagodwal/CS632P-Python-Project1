import random
import sys
from time import sleep

#The following useful functions are included to simplify error handling further down.
def yesNo(question):
    while True:
        reply = str(input(question+' (Y/N): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

# Make user enter a number
def inputNumber(prompt):
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Please enter numbers only -- no commas, spaces or currency symbol needed.")
            continue
        else:
            return userInput

# global menu function, takes list of options and takes only valid input
def displayMenu(options, choice = 999):
    print("\n:::[MAIN MENU]:::\n")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    while choice >= (len(options)+1):
        choice = inputNumber("\nPlease choose an option: ")
    return choice

# main book class, has constructor, creator, display and formatting logic built in.
class Books:
    def __init__(self, number, title, genre, author, condition, purchase_price, retail_price):
        self.number = number
        self.title = title
        self.genre = genre
        self.author = author
        self.condition = condition
        self.purchase_price = purchase_price
        self.retail_price=retail_price

    @classmethod    # A user interface for adding new books.
    def from_input(cls):
        number = inputNumber("Please enter book Id: ")
        title = input("Please enter Title: ")
        genre = input("Please enter Genre: ")
        author = input("Please enter Author: ")
        price = inputNumber("Please enter Purchase Price: ")
        retail_price = inputNumber("Please enter Retail Price: ")
        condition_list = ["Junk", "Critical", "Bad", "Poor", "Fair", "Good", "Like New", "New"]
        while True:
            choice = inputNumber("\nCONDITION: Please choose book condition from the list: [1-8]" +
            '\n\n::: OPTIONS :::   1 = Poor, 2 = Fair, 3 = Bad, 4 = Good, 5 = Like New, '
            '6 = New   :::   ')
            if (choice > 0) and (choice < 9):
                condition = condition_list[choice - 1]
                break
            else:
                print ("\nPlease choose valid option!")
        return cls(number, title, genre, author, condition,price, retail_price, )


    def getnumber(self):
        return self.number

    def getprice(self):
        return self.purchase_price

    def Display(self):
        print("\n\n     Number:        |",  self.number)
        print("     Title:         |",  self.title.title())
        print("     Genre:         |",  self.genre.title())
        print("     Author:        |",  self.author.title())
        print("     Condition:     |",  self.condition)
        print("     Price:         |",  self.purchase_price)
        print("     Retail Price:  |",  self.retail_price)

    # setup return function to pipe data elsewhere (such as file). used dictionary to work better for making a
    # string to output to file
    def Return(self):
        extraedit = {'\n  Number:        |':     self.number,
                            'Title:         |':     self.title,
                            'Genre:         |':     self.genre,
                            'Author:        |':     self.author,
                            'Condition:     |':     self.condition,
                            'Price:         |':     self.purchase_price,
                            'Retail Price:  |':     self.retail_price}
        output = '\n'.join("{!s}  {!r}".format(key,val) for (key,val) in extraedit.items())
        output = output.replace("'", "")
        return output

# The inventory keep tracks of array and facilitates purchasing,selling, deletion, updating, displaying and
# exporting of Book items.
class Inventory(object):
    def __init__(self):
        self.inventory = []

    def add_item(self, book):
        self.inventory.append(book)

    def purchase_from_input(self):
        self.inventory.append(Books.from_input())

    def sell_item(self):
        choice = input("Please enter the Book number you wish to sell: ")
        for i in range(len(self.inventory)):
            if self.inventory[i].getnumber() == choice:
                ask= int(input("Please enter the price : "))
                profit = ask - self.inventory[i].getprice()
                if ask > self.inventory[i].getprice():
                    print("Your profit is:" )
                    print(profit)
                else:
                    print("Your loss is : " )
                    print( profit)

    def update_item(self):
        upd_nominee = input("Please enter the book number you wish to update details for: ")
        for i in range(len(self.inventory)):
            if self.inventory[i].getnumber() == upd_nominee.upper():
                print("\nBook", upd_nominee, "was found in list. Enter new attributes:\n")
                self.inventory[i] = Books.from_input()
                print("\nBook", upd_nominee, 'was successfully updated.')
                return upd_nominee
                break
        else:
            print('\nBook of "', upd_nominee,
                  '"not found. Please choose desired option again from menu and ensure correct entry.')

    def export_inventory(self):
        userfilename = str(input("\nEnter name to save file (extension will be added automatically): ") + ".txt")
        outfile = open(userfilename, "a")
        outfile.write("\nBOOK INVENTORY PROGRAM OUTPUT: \n")
        for i in range(len(self.inventory)):
            outfile.write('\n' + str(self.inventory[i].Return()) + '\n')
        outfile.close()
        input("\nINVENTORY EXPORT SUCCESSFUL. File was saved as '" + userfilename + "'. [ENTER]")

    def remove_item(self):
        del_nominee = input("\nPlease enter the Book number you wish to delete: ")
        for i in range(len(self.inventory)):
            if self.inventory[i].getnumber() == del_nominee.upper():
                self.inventory.pop(i)
                print("\nBook with number of",del_nominee,"was removed from inventory.")
                break
        else:
            print("\nBook not found. Please try again from menu and ensure correct entry.")


    def display_inventory(self):
        for i in range(len(self.inventory)):
            self.inventory[i].Display()
            sleep(0.3)


def main():
    # created an empty inventory
    inventory = Inventory()
    inventory.add_item(Books("1", "To kill a Mocking Bird", "Thriller", "Henry Lee", "Old", 12,14))
    inventory.add_item(Books("2", "The Great Gatsby", "Fiction", "F. Scott Fitzgerald", "Fair", 30,35))
    inventory.add_item(Books("3", "Jane Eyre", "Romance", "Charlotte Bronte", "Good", 29,32))
    inventory.add_item(Books("4", "The Da Vinci Code", "Mystery", "Dan Brown", "Like New", 34,40))
    inventory.add_item(Books("5", "Harry Potter and the Sorcerer's Stone", "Fantasy Fiction", "J.K. Rowling", "Good",45,
                             50))
    # List menu items for function
    menuItems = ['View Inventory','Purchase Book', 'Sell Book', 'Update Book Details','Remove Book Entry',
                 'Export Inventory', 'Quit']

    print("\nWelcome to Tim's Book Store")
    while True:
        choice = displayMenu(menuItems)
        if choice == 1:
            print("\nCURRENT BOOK INVENTORY CONTENTS:\n")
            sleep(0.8)
            inventory.display_inventory()
        elif choice == 2:
            print("\nADD NEW BOOK TO INVENTORY:\n")
            sleep(0.8)
            inventory.purchase_from_input()
            print("\nBOOK ADDITION SUCCESSFUL. Item can now be found in inventory listing.")
        elif choice == 3:
            print("\nSELL A BOOK")
            sleep(0.8)
            inventory.sell_item()
        elif choice == 4:
            print("\nUPDATE A BOOK")
            inventory.update_item()
        elif choice == 5:
            print("\nREMOVE A BOOK")
            inventory.remove_item()
        elif choice == 6:
            inventory.export_inventory()
        else:
            check = yesNo("\nARE YOU SURE? All data will be lost. Backup?")
            if check:
                inventory.export_inventory()
            print ("\nPROGRAM UNDERGOING TERMINATION.\n")
            sleep(1)
            quit()

if __name__ == '__main__':
    main()








