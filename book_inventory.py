from datetime import datetime
import random
import sys
from time import sleep

def yesNo(question):
    while True:
        reply = str(input(question+' (Y/N): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def inputNumber(prompt):
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Please enter numbers only -- no commas, spaces or currency symbol needed.")
            continue
        else:
            return userInput

def displayMenu(options, choice = 999):
    print("\n:::[MAIN MENU]:::\n")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    while choice >= (len(options)+1):
        choice = inputNumber("\nPlease choose an option: ")
    return choice



class Books:
    def __init__(self, number, title, genre, author, condition, purchase_price, retail_price):
        self.number = number
        self.title = title
        self.genre = genre
        self.author = author
        self.condition = condition
        self.purchase_price = purchase_price
        self.retail_price=retail_price

    @classmethod
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
            '\n\n::: OPTIONS :::   1 = Junk, 2 = Critical, 3 = Bad, 4 = Poor, 5 = Fair, 6 = Good, 7 = Like New, '
            '8 = New   :::   ')
            if (choice > 0) and (choice < 9):
                condition = condition_list[choice - 1]
                break
            else:
                print ("\nPlease choose valid option!")
        return cls(number, title, genre, author, price, retail_price, condition)

    def Display(self):
        print("\n\n     Number:        |",  self.number)
        print("     Title:         |",  self.title.title())
        print("     Genre:         |",  self.genre.title())
        print("     Author:        |",  self.author.title())
        print("     Condition:     |",  self.condition)
        print("     Price:         |",  self.purchase_price)
        print("     Retail Price:  |",  self.retail_price)

    def Return(self):
        extraditedit = {'\n  Number:        |':     self.number,
                            'Title:         |':     self.title,
                            'Genre:         |':     self.genre,
                            'Author:        |':     self.author,
                            'Condition:     |':     self.condition,
                            'Price:         |':     self.purchase_price,
                            'Retail Price:  |':     self.retail_price}
        output = '\n'.join("{!s}  {!r}".format(key,val) for (key,val) in extraditedit.items())
        output = output.replace("'", "")
        return output

class Inventory(object):
    def __init__(self):
        self.inventory = []

    def add_item(self, book):
        self.inventory.append(book)

    def add_from_input(self):
        self.inventory.append(Books.from_input())

    def purchase_item(self):
        pass

    def sell_item(self):
        choice=int(input("Enter Book Id: "))
        pass





    def export_inventory(self):
        userfilename = str(input("\nEnter name to save file (extension will be added automatically): ") + ".txt")
        outfile = open(userfilename, "a")
        outfile.write("\nBOOK INVENTORY PROGRAM OUTPUT: \n")
        for i in range(len(self.inventory)):
            outfile.write('\n' + str(self.inventory[i].Return()) + '\n')
        outfile.close()
        input("\nINVENTORY EXPORT SUCCESSFUL. File was saved as '" + userfilename + "'. [ENTER]")

    def display_inventory(self):
        for i in range(len(self.inventory)):
            self.inventory[i].Display()
            sleep(0.3)

def main():
    inventory = Inventory()
    inventory.add_item(Books("1", "To kill a Mocking Bird", "Drama", "Henry Lee", "Old", 12,14))
    inventory.add_item(Books("2", "The Great Gatsby", "Fiction", "F. Scott Fitzgerald", "Fair", 30,35))
    inventory.add_item(Books("3", "Jane Eyre", "Romance", "Charlotte Bronte", "Good", 29,32))
    inventory.add_item(Books("4", "The Da Vinci Code", "Mystery", "Dan Brown", "Like New", 34,40))
    inventory.add_item(Books("5", "Harry Potter and the Sorcerer's Stone", "Fantasy Fiction", "J.K. Rowling", "Good",45,
                             50))

    menuItems = ['View Inventory','Add Book','Purchase Book', 'Sell Book', 'Export Inventory', 'Quit']

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
            inventory.add_from_input()
            print("\nBOOK ADDITION SUCCESSFUL. Item can now be found in inventory listing.")
        elif choice == 3:
            print("\nPURCHASE BOOK")
            sleep(0.8)
            inventory.purchase_item()
        elif choice == 4:
            print("\nSELL A BOOK")
            sleep(0.8)
            inventory.sell_item()
        elif choice == 5:
            inventory.export_inventory()
        else:
            check = yesNo("\nARE YOU SURE? All data will be lost. Backup?")
            if check:
                inventory.export_inventory()
            print ("\nPROGRAM UNDERGOING TERMINATION.\n\nFinding eels, filling hovercrafts...\n")
            sleep(1)
            quit()

if __name__ == '__main__':
    main()








