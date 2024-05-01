from os import remove


users = {}


def printlar():
    global users
    print('1.Register')
    print('2.Login')
    print('3.quit')

    a = input('>>>')
    if a == ('1' or 'Register'):
        register()
    if a == ('2' or 'Login'):
        login()
    if a == ('3' or 'quit'):
        print('xayr')


def register():
    global users
    print('Registratsiya')
    full_name = input('Full name: ')
    username = input('Username: ')
    password = input('password: ')

    if username in users:
        print('bu username bant')
        printlar()
    if username not in users:
        print("Registratsiyadan o'ttingiz")
        d = {'full_name':full_name, 'password':password}
        users[username] = d
        printlar()

def login():
    global users
    print('Login')
    username = input('Username: ')
    password = input('password: ')
    if not username in users:
        print('username yoki parol xato')
        printlar()
    if username in users:
        if users[username]['password'] == password:
            x = users[username]['full_name']
            print(f'Xush kelibsiz  {x}')
            print('1.Logout')
            print('2.Delete account')
            print('3.quit')
            d = input('>>>')
            if d == ('1' or 'Logout'):
                print("logout bo'ldi")
                printlar()
            if d == ('2' or 'Delete account'):
                users[username] = ""
                printlar()
            if d == ('3' or 'quit'):
                print('Raxmat')
    else:
        print('username yoki parol xato')
        printlar()





print('Hellow anonim user')
printlar()