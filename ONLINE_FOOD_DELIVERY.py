#to set delay in operations................................................................
import time

#data stored class...........................................................................
class Server:
    def __init__(self):
        self.admin={"username": "admin123", "password": "admin@26"}
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
            {"name": "Dosa", "restaurant": "paragon", "price": 50},
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


#restaurant searching.................................................................
class Restaurants():
    def __init__(self, data):
        self.d= data
    def restaurant(self):
        name=input('Restaurant Name: ').lower()
        match=False
        i=1
        print()
        for hotels in self.d.restaurants:
            if name==hotels['name'].lower():
                print(f"{i}. {hotels['name']} restaurant - {hotels['place']}")
                match=True
                i+=1
        if match==False:
            print('\nSorry....Restaurant not found\n')
        print()


#food searching........................................................................
class Foods():
    def __init__(self, data):
        self.d= data
    def food(self):
        name=input('Food item: ').lower()
        match=False
        i=1
        print()
        for items in self.d.foods:
            if name == items['name'].lower():
                print(f"{i}. {items['restaurant']} restaurant - {items['price']} rupees")
                match=True
                i+=1
        if match==False:
            print('Sorry....No such food item found')
        print()


#by location searching................................................................
class Nearby():
    def __init__(self, data):
        self.d= data
    def nearby(self):
        print()
        print('1. Turn on your GPS\n2. Go back')
        while True:
            a=int(input('Select your option: '))
            if a==1:
                print('Unable to fetch your location. Please try again later')
            elif a==2:
                home(),opt()
                break
            else:
                print('incorrect option')
        print()


#account option..........................................................................
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
                            print("To home page press '*'")
                            a=input()
                            if a=='*':
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
                break
        # back to home.............................................................................
            elif a==3:
                home(),opt()
                break
        # else condition ............................................................................
            else:
                print('incorrect option')
        print()

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
                        time.sleep(2)
                        home(),opt()
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
                print("Registration successful.")
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

        # else condition ............................................................................
            else:
                print('incorrect option')





"""Main menu screen.........................................................................."""
#starting page................................................................................
def home():
    print('\nWelcome to Eat_it\n\n' \
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
  
        

# suggesting based on region specials, and suggestion based on time.