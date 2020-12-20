user_input = input('Enter your name: ').upper()
welcoming = 'Hello ,'
print(welcoming+user_input)
mylist1 = input('Enter any name to your list: ').upper()
mylist2 = []
def add_item():
        print("What are you going to add?")
        user_input = input().upper()
        mylist2.append(user_input)
        print mylist1, ' =', mylist2
def remove_item():
        if len(mylist2) == 0:
                print'There is nothing to remove an item from list.'
        else:
                print("Which item you are going to remove?")
                print mylist1, ' =', mylist2
                user_input = input().upper()
                mylist2.remove(user_input)
        print mylist1, ' =', mylist2
def edit_item():
        if len(mylist2) == 0:
                print'There is nothing to edit in this list.'
        else:
                print("Which item you are going to edit?")
                print(mylist2)
                user_input = input().upper()
                if user_input in mylist2:
                        mylist2.remove(user_input)
                        print("What is your new item?")
                        user_input = input().upper()
                        mylist2.append(user_input)
                        print mylist1, ' =', mylist2
                else:
                        print'There is no such item.'
                        print mylist1, ' =', mylist2

while True:
        print("What would you like to do?")
        print('1. ADD')
        print('2. REMOVE')
        print('3. EDIT')
        print('4. COUNT NUMBER OF ITEMS')
        print('5. EXIT')
        user_input = int(input())
        if user_input == 1:
                add_item()
        if user_input == 2:
                remove_item()
        if user_input == 3:
                edit_item()
        if user_input == 4:
                print mylist1, ' =', mylist2
                print("Number of items in your list: ", len(mylist2))
        if user_input == 5:
                break
print mylist1, ' =', mylist2
