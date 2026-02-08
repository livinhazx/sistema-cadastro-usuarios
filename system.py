from datetime import datetime

users = []

def nameValid():
    while True:

        name = input("What's your name? ")
        if name.strip() == "":
            print("Empty field! Type something.")

        elif name.isdigit():
            print("Only numbers? Type text.")

        else:
            print("Name added.")

            return name
        

def validBirthdate():
     while True:
      birthdate = input("What's your birthdate? Type DD/MM/YYYY format: ")

      try:
            date = datetime.strptime(birthdate, "%d/%m/%Y")
            if date > datetime.now():
                print("Invalid date! You can't be born in the future.")
                continue
            print("Valid date:", birthdate)
            return birthdate
      
      except ValueError:
            print("Invalid format! Use the DD/MM/YYYY format.")
        



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
     

def editUser():
    emailEdit = input("Which email do you wanna edit?")

    for user in users:
        if user["email"] == emailEdit:

            choose = input("1-Name 2-Email 3-Birthdate 4-Exit: ")

            if choose == "1":
                user["name"] = nameValid()
                print("Name updated!")
            elif choose == '2':
                print("Email updated!")
                user["email"] = validEmailInput()
            elif choose == '3':
                user["birthdate"] = validBirthdate()
                print("Birthdate updated!")

            elif choose == "4":
                break
            else:
                print("Invalid option")

            return 

    print("User not found!")


def validEmailInput():
    while True:
     email = input("What's your best e-mail? ")

     if  validEmail(email):
         return email
    
    else:
     print("Email invalid!")
   
           



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

    name = nameValid()
    birthdate = validBirthdate()
    email = validEmailInput()

        
    user = {
        "name": name,
        "email": email,
        "birthdate": birthdate
        }

    users.append(user)
    print("User registered!")



def deleteUser():

    emailDelete = input("Which email do you wanna delete?")
    for user in users:
        if user["email"] == emailDelete:
            users.remove(user)
            print("User deleted!")
            return
    print("User not found!")


if __name__ == "__main__":
    mainManu()

