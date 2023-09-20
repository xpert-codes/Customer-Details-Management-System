import random
import bpy

class User:

    requirePassword = True
    maxUsers = 1000
    usersList = []

    def __init__(self, name, id_num, DOB):
        self.name = name
        self.id_num = id_num
        self.DOB = DOB
        self.usersList.append(self)

    def showUserByPosition(position):
        print(User.usersList[position].name)
        print(User.usersList[position].id_num)
        print(User.usersList[position].DOB,"\n")


    def showUsers():
        print("\nThere are currently", len(User.usersList), "users in the system....")
        for user in User.usersList:

            print(user.name)
            print(user.id_num)
            print(user.DOB,"\n")


    def checkId_num(newNumber):
        for k in range(0,len(User.usersList)):

            if(User.usersList[k].id_num == newNumber ):
                return False
        return True


def getUniqueNumber():

    unique = False 
    while(not unique): 
        num = random.randrange(1,User.maxUsers)
          
        if(User.checkId_num(num) == True):
            unique = True   
    return num


print("\n")
user1 = User("Bob Micheals", getUniqueNumber(), "12/10/87")
user2 = User("Tom Smith", getUniqueNumber(), "01/28/98")
user3 = User("Sarah Smith", getUniqueNumber(), "11/15/00")
user4 = User("Sean Smith", getUniqueNumber(), "07/14/89")
user5 = User("tara toga", getUniqueNumber(), "03/22/93")


print("\ntesting 'showUserByPosition' function.....")
index = 1 
User.showUserByPosition(index)


print("\ntesting 'showUsers' function.....")
User.showUsers()



import bpy


bpy.ops.object.select_all(action='DESELECT')


bpy.data.objects['user4'].select = True


bpy.ops.object.delete()



print("\ntesting 'showUsers' after removing.....")
User.showUsers()
