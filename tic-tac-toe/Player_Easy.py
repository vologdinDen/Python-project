from random import randint
#Player select random coordinates
class Easy():
    def move(self, number_move, lst):
        if number_move % 2 == 0:
            choose = "O"
        else:
            choose = "X"
        print('Making move level "easy"')
        while True:
            X = randint(0, 2)
            Y = randint(0, 2)
            if lst[X][Y] == " ":
                lst[X][Y] = choose
                return lst