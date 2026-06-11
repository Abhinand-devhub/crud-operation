class Restaurands:
    pass
class Foods(Restaurands):
    pass
class Nearby(Restaurands):
    pass
class Account:
    pass
class Login(Account):
    pass


"""conditions and first print..................................................................................."""
#starting page..................................................

def home():
    print('\nWelcome to FooD_to_HomE\n\n' \
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

    if menu==1:
        print('Search Restaurant')
    elif menu==2:
        print('Search Foods')
    elif menu==3:
        print('Nearby Restaurands')
    elif menu==4:
        print('Account')
    elif menu==5:
        print('Login')
    elif menu==6:
        print('Exiting....\nThank you for being with FooD_to_HomE')
    else:
        print('Invalid option. Please select correct option')    
        

# suggesting based on region specials, and suggestion based on time.