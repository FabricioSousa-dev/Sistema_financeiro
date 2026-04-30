from fileinput import close

username = str(input("Enter your username : ")).split()
id = str(input("Enter your id: ")).split()
password = str(input("Enter your password: ")).split()
name = str(input("Enter your name: ")).split()


if len(username) > 0 and username == str:
    print("Welcome {}".format(username))
elif len(id) > 5:
    print("Id{}".format(id))
elif len(password) > 6:
    print("Password{}".format(password))
elif len(name) > 5:
        print("Name{}".format(name))
else:
    print("Please enter a valid username and password")
    exit()







