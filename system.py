from datetime import datetime

users = []

 
def mainManu():
     while True:
      options = input("What you wanna do? 1 - Add a new user 2 - Edit a existent user 3 - Delete a user 4 - List the users 5 - Exit")
      if options == '1':
         addUser()
      elif options == '2':
         editUser()
      elif options == '3':
         deleteUser()
      elif options == '4':
         listUser()
      elif options == '5':
          break
      else:
         print("This option doesn't exist.")
         
mainManu()
     





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

    emailDelete = input("Which email do you wanna delete?")
    for user in users:
        if user["email"] == emailDelete:
            users.remove(user)
            print("User deleted!")
            return
    print("User not found!")




