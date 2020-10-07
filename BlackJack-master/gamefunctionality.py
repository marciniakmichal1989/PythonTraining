import random

class GameRules():

    def __init__(self):
        pass

    def before20(self):

        player_card = int(random.randint(2, 14));

        if player_card == 11:
            print("Twoja karta to [J]upek o wartosci 10")
            return 10
        elif player_card == 12:
            print("Twoja krata to [D]ama o wartosci 10")
            return 10
        elif player_card == 13:
            print("Twoja krata to [K]rol o wartosci 10")
            return 10
        elif player_card == 14:
            print("""Twoja krata to [A]s 

            masz wybor :

            mozesz dostac 1 punkt wciskajac [1]
            albo 11 wciskajac [11] """)

            player_choice = input("Twoja decyzja : ")

            if (player_choice == "1"):
                return 1
            else:
                return 11
        else:
            print(F"Twoja krata to : {player_card}")
            return player_card


    def casino(self, your_points):

        self.your_points = your_points
        casino_card = int(random.randint(2, 14));

        if casino_card == 11:
            print("Kasyno dostalo [J]upek o wartosci 10")
            return 10
        elif casino_card == 12:
            print("Kasyno dostalo [D]ama o wartosci 10")
            return 10
        elif casino_card == 13:
            print("Kasyno dostalo [K]rol o wartosci 10")
            return 10
        elif casino_card == 14:
            print("Kasyno dostalo [A]s o wartosci 1/11")
            if (your_points >= 10):
                return 1
            else:
                return 11
        else:
            print(f"Kasyno dostalo karte {casino_card}")
            return casino_card



#---------------------------------------------------------------------------------------------------

    def game(self):

        player_choice = input("""Press [1] to start game.
To End game write [exit]
    --> """)
        print(" ")

        player_points = []
        casino_points = []
        first_round = 0

        while (first_round < 2):
            player_points.append(self.before20());
            first_round = first_round + 1;

        print(F"Wszystkie twoje karty : {player_points} | Suma Punktow : {sum(player_points)}")
        print("M========================================================================== ")


        casino_points.append(self.casino(sum(casino_points)))

        print(F"Kasyno : {casino_points} | Suma Punktow Kasyna : {sum(casino_points)}")
        print("M==========================================================================")

        if (sum(casino_points) <= 20):
            while (sum(player_points) <= 20):
                player_choice = input("""Wcisnij [1] by dobrac Karte, 
    [2] by spasowac 
    [exit] To End game write 
            --> """)
                if (player_choice == "1" and sum(casino_points) <= 20):
                    player_points.append(self.before20())
                    print(
                        F"Wszystkie twoje karty : {player_points} | Suma Punktow : {sum(player_points)}")
                    print("")
                # ===============================================================================================================
                elif (player_choice == "2"):
                    print(F"zdobyles : {sum(player_points)}")
                    while sum(casino_points) < 15:
                        casino_points.append(self.casino(sum(casino_points)))
                    print(F"Kasyno : {casino_points} | Suma Punktow Kasyna : {sum(casino_points)}")
                    return sum(player_points) , sum(casino_points)

        # ===============================================================================================================

        elif (sum(casino_points) == 21):
            print("Wygrales")
            print("czy chesz zagrac ponownie ?")
            player_choice = input("zagraj ponownie : 1 jesli chcesz zakaczyc gre napisz 'exit' ")
            if (player_choice == "1"):
                self.game();
            else:
                print("game over")
        else:
            print("Przegrales !! ")
            print("")
            player_choice = input("czy chesz zagrac ponownie ? : 1 jesli chcesz zakaczyc gre napisz 'exit' ")
            if (player_choice == "1"):
                self.game();