import tictactoe

#Every move of the player brings him the maximum benefit
#for this purpose the minimax algorithm is used
class Hard():

    good_choose, bad_choose = "", ""
    game_test = None

    def __init__(self):
        self.game_test = tictactoe.Game()

    def move(self, number_move, lst : list):
        best_score = -9999
        self.game_test.set_field(lst)

        if(number_move % 2 == 0):
            self.good_choose = "O"
            self.bad_choose = "X"
        else:
            self.good_choose = "X"
            self.bad_choose = "O"
        
        for i in range(3):
            for j in range(3):
                if lst[i][j] == " ":
                    lst[i][j] = self.good_choose
                    self.game_test.set_field(lst)
                    score = self.minimax(lst, False)
                    lst[i][j] = " "
                    
                    if score > best_score:
                        best_score = score
                        x = i
                        y = j

        lst[x][y] = self.good_choose
        print('Make move level "Hard"')
        return lst
    
    def is_draw(self, lst):
        for i in range(3):
            for j in range(3):
                if lst[i][j] == " ":
                    return False
        return True
    
    #Minimax algorithm
    def minimax(self, lst, isMaximazing):

        #Check situations
        self.game_test.set_field(lst)
        if self.game_test.check() and not isMaximazing:
            return 1
        elif self.game_test.check() and isMaximazing:
            return -1
        elif self.is_draw(lst):
            return 0
        
        #Check who do move
        if isMaximazing:
            best_score = -99999
            for i in range(3):
                for j in range(3):
                    if lst[i][j] == " ":
                        lst[i][j] = self.good_choose
                        
                        score = self.minimax(lst, False)
                        lst[i][j] = " "
                        

                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 99999
            for i in range(3):
                for j in range(3):
                    if lst[i][j] == " ":
                        lst[i][j] = self.bad_choose                      
                        score = self.minimax(lst, True)
                        lst[i][j] = " "
                        if score < best_score:
                            best_score = score
            return best_score