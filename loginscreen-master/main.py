from functionality import ProgramFunction

functionality_object = ProgramFunction()

print("to log in press 1, if you dont have acount press 2 to create")

choice = input(" --> ")
while choice.lower() != "exit":
    if choice == "1":
        functionality_object.log_in()
        break
    elif choice == "2":
        functionality_object.create_accout()
        break
    else:
        print("dont recoznice this commend, please try again")
        choice = input(" --> ")




