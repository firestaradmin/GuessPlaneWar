



class MyChessBoard:
    class PLANE_HEADING:
        up = 0
        down = 1
        left = 2
        right = 3
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.chosen = {"row": 0, "col": 0}
    def show_board(self):
        print("###############################################################")
        for i in range(0,self.row): 
            for j in range(0,self.col): 
                if i == self.chosen['row'] and j == self.chosen['col']:
                    print("|▆", end='')
                else:
                    print("| ", end='')
            print("|\n", end='')
            # print("-----------------\n", end='')
        print("###############################################################")
    def chose(self,row,col):
        self.chosen['row'] = row
        self.chosen['col'] = col