from random import randint
import tictactoe

#The player chooses random coordinates
# but first checks if there is no situation in which any of the players can win with one move
class Medium():
    def move(self, number_move, lst):
        for_check = tictactoe.Game(lst)
        if number_move % 2 == 0:
            good_choose = "O"
            bad_choose = "X"
        else:
            good_choose = "X"
            bad_choose = "O"
        print('Making move level "medium"')
        while True:
            #Check situations
            for i in range(3):
                for j in range(3):

                    if lst[i][j] == " ":

                        lst[i][j] = good_choose
                        for_check.set_field(lst)

                        if for_check.check():
                            return lst

                        lst[i][j] = bad_choose
                        for_check.set_field(lst)

                        if for_check.check():
                            lst[i][j] = good_choose
                            return lst

                        lst[i][j] = " "
            #Select randoms coordinates
            X = randint(0, 2)
            Y = randint(0, 2)
            if lst[X][Y] == " ":
                lst[X][Y] = good_choose
                return lst
