import os
class Save:
    def __init__(self,board,turn):
        self.board = board
        self.turn = turn
    def run(self):
                        file = open("Save.txt", "w")
                        file1 = open("Save_turn.txt","w")
                        file1.write(self.turn)
                        file1.close()
                        for x in self.board:
                            for y in x:
                                temp = str(y) + "\n"
                                file.write(temp)
                            file.write('reset\n')
                        file.close()
class Load():
    def __init__(self):
        self.loader = []
    def run(self):
        if os.path.isfile("Save.txt"):
                            self.loader = []
                            temp_dummy = []
                            file = open("Save.txt", "r")
                            for x in file:
                                if x == "reset\n":
                                    self.loader.append(list(temp_dummy))
                                    temp_dummy.clear()
                                else:
                                    temp_dummy.append(x[0:2])
                            return self.loader
