#data stored class...........................................................................
class Server:
    def __init__(self):
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
class Restaurants(Server):
    def restaurant(self):
        name=input('Restaurant Name: ').lower()
        match=False
        for hotels in self.restaurants:
            if name==hotels['name'].lower():
                print(f'{hotels['name']} restaurant - {hotels['place']}')
                match=True
        if match==False:
            print('\nSorry....Restaurant not found\n')


#food searching........................................................................
class Foods(Server):
    def food(self):
        name=input('Food item: ').lower()
        match=False
        for items in self.foods:
            if name == items['name'].lower():
                print(f'{items['restaurant']} restaurant - {items['price']} rupees')
                match=True
        if match==False:
            print('Sorry....No such food item found')


#by location searching................................................................
class Nearby(Server):
    pass
class Account:
    pass
class Login(Account):
    pass




"""conditions and first print.........................................................................."""
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
while True:
    menu=int(input('Select your choice: '))
    if 1<=menu<=6:
        break
    else:
        print('Invalid option. Please select correct option')  

if menu==1:
    r=Restaurants()
    r.restaurant()
elif menu==2:
    f=Foods()
    f.food()
elif menu==3:
    n=Nearby()
    n.nearby()
elif menu==4:
    a=Account()
    a.account()
elif menu==5:
    l=Login()
    l.login()
elif menu==6:
    print('Exiting....\nThank you for being with FooD_to_HomE')
  
        

# suggesting based on region specials, and suggestion based on time.