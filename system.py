
def validEmail():
    if "@" not in email:
        return False
    pieces = email.split("@")
    if len(pieces) !=2:
        return False
    user, domain = pieces
    if user =="" or domain =="":
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True
   

def addUser():
    name = input("What's your name?")
    if name.strip() == "":
        print("Empty field! Type something.")
    elif name.isdigit():
        print("Only numbers? Type text.")
    else: 
        print("Name added.")
    email = input("What's your best e-mail?")
    validEmail()
    
    birthdate = input("What's your birthdate? Type DD MM AA format")

