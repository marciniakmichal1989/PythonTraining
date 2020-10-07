class ProgramFunction:

    def __init__(self):
        pass

    def create_accout(self):

        print("You are in create_accout screan")
        user_name = input("Please enter user name (min 5 characters) : ")

        while len(user_name) <= 5:
            print("user name to short please type once again")
            user_name = input("Please enter user name (min 5 characters) : ")

        user_password = input("Please enter password : ")

        while len(user_password) <= 5:
            print("user password to short plese type once again")
            user_password = input("Please enter user name () : ")

        with open('data.txt', "a") as out_file:
            out_file.write(str(user_name) + " " + str(user_password) + "\n")

        print("User have been created")

#-------------------------------------------------------------------------

    def log_in(self):
        print("You are in log_in screan")
        user_name = input("Please enter user name : ")

        with open('data.txt', "r") as out_file:
            if user_name in out_file.read():
                print(f"Username {user_name} in data base")

                user_password = input("Please enter password : ")
            else:
                print("User dont exist plese try again")
