import re
import turtle
# ---------------Display---------------

print('\nWelcome To Your Contact List.')
print('----------------------')
print('1. - Add A New Contact.')
print('2. - Delete Any Contact.')
print('3. - Show Display Contacts List.')
print('4. - Search Any Contact.')
print('5. - Check Version.')
print('0. - Exit.')
print('----------------------')


# ---------------Main Function---------------


def main():
    while True:
        user_input = int(input('\t Please Choice Any Option : '))
        
        if user_input == 1:
            add_contact()

        elif user_input == 2:
            delete_contact()

        elif user_input == 3:
            show_display_contact()

        elif user_input == 4:
            search_contact()
            
        elif user_input == 5:
            check_version()

        elif user_input == 0:
            break

        else:
            print("Your input is wrong. Please try again.\n Thank you so much.")


# ---------------Function---------------
my_list = []


def add_contact():
    print('Add a new Contact')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    number = input('Phone Number: ')
    flag = True
    while flag:
        email = input('E-mail: ')
        m = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)  #Copy to google.com
        if m:
            flag = False
        else:
            print("Invalid Email")                  
    address = input('Address: ')

    
    tmp = []
    tmp = first_name, last_name, number, email, address

    my_list.append(list(tmp))


def delete_contact():
    print('Delete Contact')
    delete_contact_input = input('Enter contact Phone for delete: ')

    flag = None

    for i in my_list:
        for j in i:
            if delete_contact_input == j:
                flag = my_list[my_list.index(i)]
                break
    if flag is not None:
        my_list.remove(flag)
    else:
        print("Not Found")


def show_display_contact():
    if len(my_list) == 0:
        print("\n\tYour Contact List Is Empty.\n\tPlease try other options")
    
    else:
        print('Show display Contact List')
        count = 0
        for i in my_list:
            count += 1
            print(count)
            print("first_name: ", i[0])
            print("last_name: ", i[1])
            print("number: ", i[2])
            print("email: ", i[3])
            print("address: ", i[4])
            print("----------")
    

def search_contact():
    print('Search A Contact')
    search_input = input('Please enter your input: ')

    flag = None
    for i in my_list:
        for j in i:
            if search_input == j:
                flag = my_list[my_list.index(i)]
                break

    if flag is not None:
        #print(flag)
        print("first_name: ", flag[0])
        print("last_name: ", flag[1])
        print("number: ", flag[2])
        print("email: ", flag[3])
        print("address: ", flag[4])
    else:
        print("Not Found")
        

def check_version():
    print("\n\t@Current Version 00.22.07.19")
    
    #print("Check last version!")
    while True:
        u_input = input("Check last version! (Yes/No): ")
        
        if u_input == "Yes":
#            turtle.shape("turtle")
            turtle.speed(4)
            
            for side_lenght in range(50, 120, 10):
                for i in range(6):
                    turtle.forward(side_lenght)
                    turtle.left(90)
                    
            turtle.exitonclick()
            print("\nThe latest version is already installed.")
            break
            
        elif u_input == "No":
            break
        
        else:
            print("Sorry!! Your Input Wrong.")
            break
    
    


main()

# ---------------Finishing Part---------------

print("\n\n\t\t\t© Copyright 2019, \'Ahasan Software Limited.\' ")