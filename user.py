from fileinput import close

username = str(input("Enter your username : ")).split()
id = str(input("Enter your id: ")).split()
password = str(input("Enter your password: ")).split()
name = str(input("Enter your name: ")).split()





if len(password) < 6:
    print("Password is too short")

else:
    print("Password is correct")

if len(username) <= 0:
    print("Username is too short")
else:
    print("Welcome! {}".format(username))
if len(id) <= 0:
    print("ID is too short")
else:
    print("Welcome! {}".format(id))

if len(name) < 0:
    print("Name is too short")
else:
    print("Welcome! {}".format(name))
    close()







