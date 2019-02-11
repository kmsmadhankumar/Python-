correct_password = "hello123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password :
    password = input("Wrong password! Enter again: ")

# print("Hey {} , you are now logged in" .format(name))
print("Hey %s , you are now logged in!" % name)
