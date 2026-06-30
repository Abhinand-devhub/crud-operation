#to set delay in operations................................................................
import time
import datetime

#to confirm login before order.............................................................
login_value=False

#data stored class.........................................................................
class Server:
    def __init__(self):
        self.admin={"username": "admin", "password": "admin12"}
        self.users=[
            {"name": "abhi12", "password": "abh123"},
            {"name": "shahil23", "password": "sha234"},
            {"name": "yasir34", "password": "yas345"}
        ]
        self.foods=[
            {"name": "Biriyani", "restaurant": "Paragon", "price": 190},
            {"name": "Biriyani", "restaurant": "Topform", "price": 180},
            {"name": "Biriyani", "restaurant": "Bombay", "price": 180},
            {"name": "Dosa", "restaurant": "Dakshin", "price": 50},
            {"name": "Dosa", "restaurant": "Paragon", "price": 50},
            {"name": "Dosa", "restaurant": "Ruchibhavan", "price": 50},
            {"name": "Porotta", "restaurant": "Rahmath", "price": 15},
            {"name": "Porotta", "restaurant": "Sagar", "price": 15},
            {"name": "Porotta", "restaurant": "Bombay", "price": 15},
            {"name": "Friedrice", "restaurant": "Sagar", "price": 140},
            {"name": "Friedrice", "restaurant": "Topform", "price": 140},
            {"name": "Friedrice", "restaurant": "Rahmath", "price": 150}
        ]
        self.restaurants=[
            {"name": "Paragon", "place": "Mananchira"},
            {"name": "Paragon", "place": "South beach"},
            {"name": "Topform", "place": "Mavoor road"},
            {"name": "Topform", "place": "SM street"},
            {"name": "Bombay", "place": "Silk street"},
            {"name": "Dakshin", "place": "Mavoor road"},
            {"name": "Rahmath", "place": "Stadium junction"},
            {"name": "Rahmath", "place": "Aravindhghosh road"},
            {"name": "Sagar", "place": "Mavoor road"},
            {"name": "Sagar", "place": "Arayidathupalam"},
            {"name": "Ruchibhavan", "place": "Mavoor road"}
        ]

#restaurant searching......................................................................
class Restaurants():
    def __init__(self, data):
        self.d= data
    def restaurant(self):
        name=input('Restaurant Name: ').lower()
        apnd_list=[]
        match=False
        i=1
        print()
        for hotels in self.d.restaurants:
            if name==hotels['name'].lower():
                apnd_list.append(hotels)
                print(f"{i}. {hotels['name']} restaurant - {hotels['place']}")
                match=True
                i+=1
        if match==False:
            print('\nSorry....Restaurant not found')
            time.sleep(2)
            home(),opt()

        #to food menu.......................................................................
        if match==True:
            resto=int(input('Enter your choice: '))
            
            if 0<resto<=len(apnd_list):
                print(f"\n{apnd_list[resto-1]['name']}-{apnd_list[resto-1]['place']}")
                fd=False
                apnd_fd=[]
                i=1
                for foods in self.d.foods:
                    if foods['restaurant'].lower==apnd_list[resto-1]['name'].lower:
                        apnd_fd.append(foods)
                        print(f"{i}. {foods['name']}- {foods['price']}")
                        fd=True
                        i+=1
                if fd==False:
                    print('\ninvalid restaurant choice')
                    time.sleep(2)
                    self.restaurant()
                    fd==False
            else:
                time.sleep(2)
                self.restaurant()

        #to food selection............................................................
        if fd==True:
            foodselect=int(input('Select Food item: '))
            if 0<foodselect<=len(apnd_fd):
                print(f"Proceeding with {apnd_fd[foodselect-1]['name']}....")
                total=apnd_fd[foodselect-1]['price']+20
                print(f"Total price of order:- {total}. Inclusive delivery charges")
                global login_value
                if login_value==True:
                    addess=input("Enter your adress: ")
                    print("Proceed with payment.")
                    payment=input(f"Enter $ after payment {total}-Rupees.\n")
                    if payment=='$':
                        print("\nOrder placed successfully. Order will reach you ASAP\nA traking id will be send to your mobile to track your order status.")
                        print("\nThank You For Being With FooD_to_HomE\nHave a Good Day")
                        time.sleep(5)
                        home(),opt()

                    else:
                        time.sleep(2)
                        self.restaurant()
                else:
                    time.sleep(2)
                    print("Please Login to continue your order....")
                    home(),opt()
                    
            else:
                print('\ninvalid food choice')
                time.sleep(2)
                self.restaurant()
            
#food searching............................................................................
class Foods():
    def __init__(self, data):
        self.d= data
    def food(self):
        name=input('\nFood item: ').lower()
        match=False
        apnd_rest=[]
        i=1
        print()
        for items in self.d.foods:
            if name == items['name'].lower():
                apnd_rest.append(items)
                print(f"{i}. {items['restaurant']} restaurant - {items['price']} rupees")
                match=True
                i+=1
        if match==False:
            print('Sorry....No such food item found')
    # to restaurant selection......................................................................
        if match==True:
            resto=int(input('Enter your choice: '))
            print()
            if 0<resto<=len(apnd_rest):
                rest=False
                i=1
                listofhotel=[]
                for hotels in self.d.restaurants:
                    if apnd_rest[resto-1]['restaurant']==hotels['name']:
                        listofhotel.append(hotels)
                        print(f"{i}. {hotels['name']}-{hotels['place']}")
                        rest=True
                        i+=1
            else:
                print("Invalid choice....")
                time.sleep(2)
                self.food()
    # to item order.........................................................................
        if rest==True:
            place=int(input("Enter your choice: "))
            if 0<place<=len(listofhotel):
                total=apnd_rest[resto-1]['price']+20
                print(f"Total price of order:- {total}. Inclusive delivery charges")
                global login_value
                if login_value==True:
                    addess=input("Enter your adress: ")
                    print(f"\nOrder confrimed from {listofhotel[place-1]['name']}-{listofhotel[place-1]['place']} restaurant")
                    print("Proceed with payment.")
                    payment=input(f"Enter $ after payment {total}-Rupees.\n")
                    if payment=='$':
                        print("\nOrder placed successfully. Order will reach you ASAP\nA traking id will be send to your mobile to track your order status.")
                        print("\nThank You For Being With FooD_to_HomE\nHave a Good Day")
                        time.sleep(5)
                        home(),opt()
                    else:
                        time.sleep(2)
                        self.food()
                else:
                    time.sleep(2)
                    print("Please Login to continue your order....")
                    home(),opt()
            else:
                print("Invalid choice....")
                time.sleep(2)
                self.food()

#by location searching..........................................................................
class Nearby():
    def __init__(self, data):
        self.d= data
    def nearby(self):
        print()
        print('1. Turn on your GPS\n2. Go back')
        while True:
            a=int(input('Enter your option: '))
            if a==1:
                print('Unable to fetch your location. Please try again later')
            elif a==2:
                home(),opt()
                break
            else:
                print('incorrect option')
        print()

#account option.................................................................................
class Account():
    def __init__(self, data):
        self.d= data
    def account(self):
        print()
        print('1. Update username/password\n2. Delete account\n3. Go back')
        while True:
            a=int(input('Select your option: '))
        # update password....................................................................
            if a==1:
                while True:
                    Username=input("Username: ")
                    Password=input("Password: ")
                    for user in self.d.users:
                        if Username==user['name'] and Password==user['password']:
                            print('\nEnter new Username & Password\n')
                            user['name']=input("New username: ")
                            user['password']=input("New Password: ")
                            print('\nUsername/Password changed successfully\n')
                            print(f"Updated Username: {user['name']}\n        Password: {user['password']}")
                            print("\nRedirecting to log-in menu")
                            time.sleep(2)
                            home(),opt()
                            break
                    else:
                        print('Incorrect username or password')
                        continue
                    break
        # delete account.........................................................................
            elif a==2:
                Username=input("Username: ")
                Password=input("Password: ")
                for user in self.d.users:
                    if Username==user['name'] and Password==user['password']:
                        self.d.users.remove(user)
                        print('\nAccount deleted successfully\n')
                        time.sleep(2)
                        home(),opt()
                    else:
                        print("\nAccount not found")
                        time.sleep(2)
                        home(),opt()
                break
        # back to home.............................................................................
            elif a==3:
                home(),opt()
                break
        # else condition ............................................................................
            else:
                print('incorrect option')
        print()

#login option....................................................................................
class Login():
    def __init__(self, data):
        self.d= data
    def login(self):
        print()
        print("1. Log-in\n2. Sign-up\n3. Admin log-in")
        while True:
            a=int(input('Select your option: '))
        # user login ...........................................................................
            if a==1:
                print('\nUser login')
                Username=input("Username: ")
                Password=input("Password: ")
                for user in self.d.users:
                    if Username==user['name'] and Password==user['password']:
                        print('\nLogin successful')
                        global login_value
                        login_value=True
                        time.sleep(2)
                        home(),opt()
                        break
                else:
                    print('\nIncorrect username or password\nif you are a new user, Register to contine')
                    time.sleep(2)
                    self.login()
                break
        # register new user .........................................................................
            elif a==2:
                print('\nRegister as new user')
                newuser=input("Create username: ")
                newpass=input("Create password: ")
                for  user in self.d.users:
                    if newuser==user['name'] or newpass==user['password']:
                        print("\nUsername/ Password already exist")
                self.d.users.append({"name": newuser, "password": newpass})
                print("\nRegistration successful.")
                time.sleep(2)
                self.login()
                break
        # admin login ...............................................................................
            elif a==3:
                print('\nAdmin login')
                Username=input("Admin Username: ")
                Password=input("Admin Password: ")
                if Username!=self.d.admin['username'] or Password!=self.d.admin['password']:
                    print('\nInvalid Credentials..!!')
                    time.sleep(2)
                    self.login()
                    return
            #admin menu.........................................................................
                def admin_menu():
                #restaurant section......................................................................
                    def restaurant_sec():
                        print("\n1. View Restaurants\n2. Add Restaurant\n3. Delete Restaurant\n4. Update Restaurant")
                        while True:
                            opt=int(input('Select your choice: '))
                            print()
                            if opt==1:                                  #view restaurant
                                i=1
                                for li in self.d.restaurants:
                                    print(i,'-',li['name'],'Restaurant-',li['place'])
                                    i+=1
                                while True:
                                    a=input('enter * to go back: ')
                                    if a=='*':
                                        time.sleep(1)
                                        admin_menu()
                                        break
                                    else:
                                        print('Invalid input')
                                break
                            elif opt==2:                                  #add restaurant
                                self.d.restaurants.append({'name':input('Enter Restuarant name: '),'place':input('Enter Restuarant Place: ')})
                                print('\nRestaurant added.')
                                time.sleep(1)
                                admin_menu()
                                break
                            elif opt==3:                                   #delete restaurant
                                name=input("Enter restaurant name to delete: ").lower()
                                i=1
                                for li in self.d.restaurants:
                                    if name==li['name'].lower():
                                        print(f"{i}- {li['place']}")
                                        i+=1
                                pla=input("\nEnter place to confirm: ").lower()
                                for li in self.d.restaurants:
                                    if pla==li['place'].lower() and name==li['name'].lower():
                                        self.d.restaurants.remove(li)
                                        print('\nRestaurant deleted.')
                                        time.sleep(1)
                                        admin_menu()
                                break
                            elif opt==4:                                   #update restaurant
                                name=input("Enter restaurant name: ").lower()
                                i=1
                                for li in self.d.restaurants:
                                    if name==li['name'].lower():
                                        print(f"{i}- {li['place']}")
                                        i+=1
                                pla=input("\nEnter place: ").lower()
                                for li in self.d.restaurants:
                                    if pla==li['place'].lower() and name==li['name'].lower():
                                        li['place']=input("Enter new location: ")
                                        print('\nRestaurant updated.')
                                        time.sleep(1)
                                        admin_menu()
                                break
                            else:
                                print("Invalid choice")
                            break
                #food section............................................................................
                    def food_sec():                               
                        print("\n1. Add Food\n2. Delete Food\n3. Update Food Price\n4. View food items")
                        while True:
                            opt=int(input('Select your choice: '))
                            print()
                            if opt==1:                                  #add food item
                                self.d.foods.append({'name':input('Enter Food name: '),
                                                     'restaurant':input('Enter Restuarant name: '),
                                                     'price':float(input('Enter Price of the item: '))})
                                print('\nFood item added.')
                                time.sleep(1)
                                admin_menu()
                                break
                            elif opt==2:                                #delete food item
                                name=input("Enter Food name: ")
                                i=1
                                for item in self.d.foods:
                                    if name==item['name'].lower():
                                        print(f"{i}- {item['restaurant']}")
                                        i+=1
                                resto=input('Enter Restuarant name: ')
                                for li in self.d.foods:
                                    if resto==li['restaurant'].lower() and name==li['name'].lower():
                                        self.d.foods.remove(li)
                                        print('\nFood item Deleted.')
                                        time.sleep(1)
                                        admin_menu()
                                break
                            elif opt==3:                                   #update food
                                name=input("Enter Food name: ").lower()
                                i=1
                                for li in self.d.foods:
                                    if name==li['name'].lower():
                                        print(f"{i}- {li['place']}")
                                        i+=1
                                rest=input("\nEnter Restaurant Name: ").lower()
                                for li in self.d.foods:
                                    if rest==li['restaurant'].lower() and name==li['name'].lower():
                                        li['price']=float(input('Enter New Price of the item: '))
                                        print('\nFood Price updated.')
                                        time.sleep(1)
                                        admin_menu()
                                break
                            elif opt==4:                                    #view food item
                                i=1
                                for li in self.d.foods:
                                    print(f"{i}- {li['name']}-{li['restaurant']}")
                                    i+=1
                                while True:
                                    a=input('enter * to go back: ')
                                    if a=='*':
                                        time.sleep(1)
                                        admin_menu()
                                        break
                                    else:
                                        print('Invalid input')
                                break
                            else:
                                print("invalid choice")
                            break
                #user section............................................................................
                    def user_sec():                                
                        print("\n1. View Users\n2. Delete User")
                        while True:
                            opt=int(input('Select your choice: '))
                            print()
                            if opt==1:                                  #view users
                                i=1
                                for usr in self.d.users:
                                    print(f"{i}- {usr['name']}")
                                    i+=1
                                while True:
                                    a=input('enter * to go back: ')
                                    if a=='*':
                                        time.sleep(1)
                                        admin_menu()
                                        break
                                    else:
                                        print('Invalid input')
                                break
                            elif opt==2:                                #delete user
                                name=input("Username: ")
                                for user in self.d.users:
                                    if name==user['name']:
                                        self.d.users.remove(user)
                                        print('\nUser account deleted.')
                                        time.sleep(1)
                                        admin_menu()
                                    else:
                                        print("\nAccount not found")
                                        time.sleep(1)
                                        admin_menu()
                                break
                            else:
                                print("invalid choice")
                            break
                #admin menu options......................................................................
                    while True:
                        print("\n1. Restaurant Section \n2. Food  Section\n3. Users  Section\n4. Log-out")
                        select=int(input('Select your choice: '))
                        if select==1:
                            restaurant_sec()
                            break
                        elif select==2:
                            food_sec() 
                            break  
                        elif select==3:
                            user_sec()
                            break
                        elif select==4:
                                print('\nYou are Logged-out....\n')
                                time.sleep(2)
                                home(),opt()
                                break
                        else:
                            print('Invalid option')
                
                admin_menu()
                break
        # else condition ............................................................................
            else:
                print('incorrect option')

# suggestion based on time.......................................................................
x=datetime.datetime.now()
tym=x.hour
if 6<=tym<=11:
    print("Good Morning....Have breakfast with FooD_to_HomE")
    print("Order now the Dosa/Porotta and get discount coupon for next purchase")
elif 12<=tym<=15:
    print("Good Afternoon....Explore lunch with FooD_to_HomE")
    print("Order now the Biriyani and get discount coupon for next purchase")
elif 16<=tym<=20:
    print("Good Evning....Lets make the evening with FooD_to_HomE")
    print("Order now Porotta and get discount coupon for next purchase")
elif 21<=tym<=24:
    print("It's Supper time....Check it on FooD_to_HomE")
    print("Order now the Fried rice and get discount coupon for next purchase")
else:
    pass


"""Main menu screen###################################################################################################"""
#starting page................................................................................
def home():
    print('\n' \
'   1- Search Restaurants\n'\
'   2- Search foods\n' \
'   3- Nearby Restaurants\n' \
'   4- Account\n' \
'   5- Login\n' \
'   6- Exit') 
home()

#object creation & invoking function............................................................
data=Server()
r=Restaurants(data)
f=Foods(data)
n=Nearby(data)
a=Account(data)
l=Login(data)

def opt():
    while True:
        menu=int(input('Select your choice: '))
        if 1<=menu<=6:
            break
        else:
            print('Invalid option. Please select correct option') 
    if menu==1:
        r.restaurant()
    elif menu==2:
        f.food()
    elif menu==3:
        n.nearby()
    elif menu==4: 
        a.account()
    elif menu==5:
        l.login()
    elif menu==6:
        print('Exiting....\nThank you for being with FooD_to_HomE')
opt()
