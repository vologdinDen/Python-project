from Player_User import PLayer
from Player_Easy import Easy
import Player_Medium
import Player_Hard

#The class responsible for the basic mechanics of the game
class Game():

    field = []
    #You can create clean field or field with some configuration.
    def __init__(self, lst = None):
        if lst == None:
            self.field = [[" " for i in range(3)] for i in range(3)]
        else:
            self.field = list.copy(lst)

    def get_field(self):
        return self.field

    def set_field(self, lst):
        self.field = list.copy(lst)
                   
    #Checking the status on the field
    def check(self):       
        if self.field[0][0] == self.field[0][1] and self.field[0][0] == self.field[0][2] and self.field[0][0] != " ":
            return True
        elif self.field[1][0] == self.field[1][1] and self.field[1][0] == self.field[1][2] and self.field[1][0] != " ":
            return True
        elif self.field[2][0] == self.field[2][1] and self.field[2][0] == self.field[2][2] and self.field[2][0] != " ":
            return True
        elif self.field[0][0] == self.field[1][0] and self.field[0][0] == self.field[2][0] and self.field[0][0] != " ":
            return True
        elif self.field[0][1] == self.field[1][1] and self.field[0][1] == self.field[2][1] and self.field[0][1] != " ":
            return True
        elif self.field[0][2] == self.field[1][2] and self.field[0][2] == self.field[2][2] and self.field[0][2] != " ":
            return True
        elif self.field[0][0] == self.field[1][1] and self.field[0][0] == self.field[2][2] and self.field[0][0] != " ":
            return True
        elif self.field[0][2] == self.field[1][1] and self.field[0][2] == self.field[2][0] and self.field[0][2] != " ":
            return True


    def wins(self, number_move):
        if number_move % 2 == 0:
            choose = "O"
        else:
            choose = "X"
        if number_move != 9:
            print(f"{choose} wins")
        else:
            print("Draw")


    def show(self):
        print("---------")
        for i in self.field:
            print("|", *i, "|")
        print("---------")
    
        
    #Both players do their move
    def match(self, comm_lst, player_1, player_2):
        
        number_move = 1
        while True:
            self.field = player_1.move(number_move, self.field)
            self.show()
            if self.check() or number_move == 9:
                self.wins(number_move)
                break
            number_move += 1
            self.field = player_2.move(number_move, self.field)
            self.show()
            if self.check() or number_move == 9:
                self.wins(number_move)
                break
            number_move += 1



if __name__ == "__main__":
    command = ""
    comm_lst = []
    players_dict = {
                "user": PLayer(),
                "easy": Easy(),
                "medium": Player_Medium.Medium(),
                "hard": Player_Hard.Hard()

            }
    while command == "":
        try:
            print("""Welcome at tic-tac-toe.
    If you wanna play input 'start' and two parameters:
    User - it's you
    Easy - easy level
    Medium - medium level
    Hard - hard level
    Don't wanna play? Input 'exit'""")
            command = str(input("Input command: "))
            comm_lst = command.split(" ")
            if comm_lst[0] == "start":
                player_1 = players_dict[comm_lst[1]]
                player_2 = players_dict[comm_lst[2]]
                game = Game()
                game.match(comm_lst, player_1, player_2)
            elif comm_lst[0] == "exit":
                break
            else:
                print("Bad parameters")
                command = ""
        except KeyError:
            print("Bad parameters")
            command = ""