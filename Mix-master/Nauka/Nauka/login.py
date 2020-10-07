def create_accout():
    user_name = ""
    user_password = ""
    print("You are in create_accout screan")
    user_name = input("Please eter user name : ")


def log_in():
    print("You are in log_in screan: ")





print("to log in press 1, if you dont have acount press 2 to create")

choice = input(" --> ")
while choice.lower() != "exit":
    if choice == "1":
        log_in()
    elif choice == "2":
        create_accout()
    else:
        print("dont recoznice this commend, please try again")
        choice = input(" --> ")




