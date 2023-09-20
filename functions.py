import random
import user_class


def getUniqueNumber():

    unique = False
    while (not unique):
        num = random.randrange(1, user_class.User.maxUsers)

        if (user_class.User.checkId_num(num) == True):
            unique = True
    return num


def grabDate():
    while (True):
        date = input("Please enter a user's DOB: [mm/dd/yy] ")
        if (len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")


def deleteUser():
    print("\nDeleting user...")
    selector = input("Please enter a name, ID number, or date: ")

    user_class.User.delUser(selector)


def num_there(s):
    return any(i.isdigit() for i in s)


def loadDatabase():

    user_class.User.loadUsers()

# save database to csv file


def save_database():
    print("\nSaving Database....\n")
    user_class.User.saveUsers()
    return 1


def determineState():

    save = input(
        "\nWould you like to save the database before closing? [Y/N]\n")

    if (save.lower() == "y"):
        print("\nSaving database and exiting....\n")
        save_database()
    else:
        print("\nQuitting program without saving....\n")

    return 1


def display_home_message():

    print("\n\t  Customer Details Management System")
    s = input("""\t  ----------------- 
          1 - See Current Customers
          2 - Add Customer
          3 - Delete Customer
          4 - Show a Customer
          5 - Save Database
          7 - Quit
          -----------------\n
          Enter your choise: """)

    return s
