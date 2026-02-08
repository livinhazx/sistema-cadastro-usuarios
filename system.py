
def addUser():
    name = input("What's your name?")
    if name.strip() == "":
        print("Empty field! Type something.")
    elif name.isdigit():
        print("Only numbers? Type text.")
    else: 
        print("Name added.")
    email = input("What's your best e-mail?")

    birthdate = input("What's your birthdate? Type DD MM AA format")

