from datetime import datetime

users = []

def validEmail(email):
    if "@" not in email:
        return False
    pieces = email.split("@")
    if len(pieces) != 2:
        return False
    user, domain = pieces
    if user == "" or domain == "":
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True

def addUser():
    while True:
        name = input("What's your name? ")
        if name.strip() == "":
            print("Empty field! Type something.")
            continue
        elif name.isdigit():
            print("Only numbers? Type text.")
            continue
        else:
            print("Name added.")

        email = input("What's your best e-mail? ")
        if not validEmail(email):
            print("Invalid email!")
            continue
        else:
            print("Email valid!")

        while True:
            birthdate = input("What's your birthdate? Type DD/MM/YYYY format: ")
            try:
                date = datetime.strptime(birthdate, "%d/%m/%Y")
                if date > datetime.now():
                    print("Invalid date! You can't be born in the future.")
                else:
                    print("Valid date:", birthdate)
                    break
            except ValueError:
                print("Invalid format! Use the DD/MM/YYYY format.")

        
        user = {
            "name": name,
            "email": email,
            "birthdate": birthdate
        }

        users.append(user)
        print("User registered!")
        break

addUser()

print(users)


def deleteUser():

    emailDelete = ("Which email do you wanna delete?")
    for user in users:
        if user["email"] == emailDelete:
            users.remove(users)
            print("User deleted!")
            return
    print("User not found!")




