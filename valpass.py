details = {
    "name":"pass",
    "name1":"pass1",
    "name2":"pass2",
    "name3":"pass3",
    "name4":"pass4",
}

passin = input("Enter Username: ")

if passin in details:
    passin1 = input("What is the password: ")
    if passin1 != details[passin]:
        print("Incorrect Password")
    else:
        print("You are logged in")
else:
    print("Incorrect Username")