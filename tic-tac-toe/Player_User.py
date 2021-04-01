
class PLayer():
    def move(self, number_move, lst):
        x, y = -1, -1
        if number_move % 2 == 0:
            choose = "O"
        else:
            choose = "X"
        while True:
            try:
                Coordinates = str(input("Enter the coordinates: "))
                Coordinates_lst = Coordinates.split(" ")
                x, y = Coordinates_lst[0], Coordinates_lst[1]
                y, x = int(y), int(x)
                x -= 1
                y -= 1
                
                if 2 < x or x < 0 or 2 < y  or y < 0:
                    print("Coordinates should be from 1 to 3!")
                elif lst[x][y] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    lst[x][y] = choose
                    return lst
            except Exception:
                continue