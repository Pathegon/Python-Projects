import sys
import pygame
pygame.init()
import Sound
import Save_Load
class GameEngine():
    preset = [
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                    ]
    def __init__(self,first_move,board = preset):
                    global click_motion
                    global is_check
                    global protected
                    global validmove
                    global piecefinal
                    global movecount
                    global move_list
                    global dumbo
                    global coord
                    global lst
                    global checkmate
                    global is_check
                    global protected_store
                    global is_check
                    global protected
                    global validmove
                    global piecefinal
                    global movecount
                    global move_list
                    global dumbo
                    global protected_store
                    global coord
                    global piecetype
                    global lst
                    global mainsound
                    global maxspacecount
                    global emptyspacecount
                    maxspacecount = 32
                    emptyspacecount = 32
                    preset = [
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                    ]
                    protected = []
                    WHITE = (255, 255, 255)  # Color Codes
                    GREY = (128, 128, 128)
                    YELLOW = (204, 204, 0)
                    BLUE = (50, 255, 255)
                    BLACK = (0, 0, 0)
                    DARK_SQUARE = (126, 217, 87)
                    LIGHT_SQUARE = (255, 255, 255)
                    HIGHLIGHTCOLOR = (186, 202, 68)
                    DARK_SQUARE_PNG = pygame.transform.scale(pygame.image.load("ChessImage/darksquare.jpg"), (100, 100))
                    LIGHT_SQUARE_PNG = pygame.transform.scale(pygame.image.load("ChessImage/lightsquare.png"), (100, 100))
                    pygame.init()
                    font = pygame.font.SysFont('Minecraft', 70)
                    font_movelist = pygame.font.SysFont('Minecraft', 30)
                    '''
                    font = pygame.font.SysFont('Minecraft', 32)
                    textRect = text.get_rect()
                    '''
                    DIMENSION = 8
                    lst = []
                    is_check = False

                    WIDTH, HEIGHT = 800, 800
                    # chess is 8x8
                    squaresize = HEIGHT // DIMENSION
                    screen = pygame.display.set_mode((1200, HEIGHT))
                    screen.fill(pygame.Color("white"))
                    pygame.display.update()
                    pygame.display.set_caption("Dumb Chess (Don't know how we managed to do this)")

                    '''
                    board =[
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bp", "bp", "bp", "bp",  "bp", "bp", "bp", "bp"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                        ]
                    '''
                    board_reference = [
                        ["0,0", "0,1", "0,2", "0,3", "0,4", "0,5", "0,6", "0,7"],
                        ["1,0", "1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7"],
                        ["2,0", "2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7"],
                        ["3,0", "3,1", "3,2", "3,3", "3,4", "3,5", "3,6", "3,7"],
                        ["4,0", "4,1", "4,2", "4,3", "4,4", "4,5", "4,6", "4,7"],
                        ["5,0", "5,1", "5,2", "5,3", "5,4", "5,5", "5,6", "5,7"],
                        ["6,0", "6,1", "6,2", "6,3", "6,4", "6,5", "6,6", "6,7"],
                        ["7,0", "7,1", "7,2", "7,3", "7,4", "7,5", "7,6", "7,7"]
                    ]

                    protected_store = list()
                    highlight = pygame.transform.scale(pygame.image.load("ChessImage/highlightcolor.png"), (100, 100))
                    Graphics = {}


                    def LoadAllGraphics():
                        pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bN', 'bN', 'bB', 'bR', 'bK', 'bQ']
                        for piece in pieces:
                            Graphics[piece] = pygame.transform.scale(pygame.image.load("ChessImage/" + piece + ".png"), (75, 80))


                    LoadAllGraphics()
                    print(Graphics)


                    def test():
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                piece = board[r][c]
                                if piece != '--':
                                    screen.blit(Graphics[piece], pygame.Rect(squaresize * c * 1.02, squaresize * r, squaresize, squaresize))

                    def save():
                        print (board)
                        return board
                    def save_button():
                        color = pygame.transform.scale(pygame.image.load("ChessImage/save.png"), (400, 100))
                        screen.blit(color,pygame.Rect(8 * squaresize, 7 * squaresize, squaresize, squaresize))


                    '''
                    def drawBoard(): # THIS IS THE WORKING DRAW BOARD FUNCTION THAT USES GRIDS
                        colors = [pygame.Color(LIGHT_SQUARE), pygame.Color(DARK_SQUARE)]
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                color = colors[((r+c) % 2)]
                                pygame.draw.rect(screen, color, pygame.Rect(c*squaresize, r*squaresize, squaresize, squaresize))
                    '''


                    def drawBoard():
                        colors = [LIGHT_SQUARE_PNG, DARK_SQUARE_PNG]
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                color = colors[((r + c) % 2)]
                                screen.blit(color, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))
                        pygame.draw.line(screen, BLACK, (800, 0), (800, 800))
                        pygame.draw.line(screen, BLACK, (800, 0), (1200, 0))
                        pygame.draw.line(screen, BLACK, (1200, 0), (1200, 800))
                        pygame.draw.line(screen, BLACK, (800, 800), (1200, 1200))


                    def drawPiece1():
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                piece = board[r][c]
                                if piece != "--":
                                    screen.blit(Graphics[piece], pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))


                    def existsonboard(x, y):
                        if x <= 7 and y <= 7 and x >= 0 and y >= 0:
                            return True
                        else:
                            return False


                    def bishop_possible_move(board, x, y):
                        global protected
                        return_lst = []
                        w = y
                        if board[x][y][0] == "w":
                            for z in range(x + 1, 8):
                                w -= 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "b":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "w":
                                        protected.append((z, w))
                                        break

                            w = y
                            for z in range(x - 1, -1, -1):
                                w += 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "b":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "w":
                                        protected.append((z, w))
                                        break
                            w = y
                            for z in range(x - 1, -1, -1):
                                w -= 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "b":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "w":
                                        protected.append((z, w))
                                        break

                            w = y
                            for z in range(x + 1, 8):
                                w += 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "b":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "w":
                                        protected.append((z, w))
                                        break

                        elif board[x][y][0] == "b":
                            for z in range(x + 1, 8):
                                w -= 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "w":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "b":
                                        protected.append((z, w))
                                        break

                            w = y
                            for z in range(x - 1, -1, -1):
                                w += 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "w":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "b":
                                        protected.append((z, w))
                                        break
                            w = y
                            for z in range(x - 1, -1, -1):
                                w -= 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "w":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "b":
                                        protected.append((z, w))
                                        break

                            w = y
                            for z in range(x + 1, 8):
                                w += 1
                                if existsonboard(z, w):
                                    if board[z][w] == "--":
                                        return_lst.append((z, w))
                                    elif board[z][w][0] == "w":
                                        if existsonboard(z, w):
                                            return_lst.append((z, w))
                                        break
                                    elif board[z][w][0] == "b":
                                        protected.append((z, w))
                                        break

                        return return_lst


                    def king_possible_move(board, x, y):
                        global protected
                        return_lst = []
                        temp = [x + 1, y + 1, x - 1, y - 1, x - 1, y + 1, x + 1, y - 1, x, y - 1, x, y + 1, x - 1, y, x + 1, y]
                        for z in range(0, len(temp), 2):
                            if existsonboard(temp[z], temp[z + 1]):
                                if board[x][y][0] == "w":
                                    if board[temp[z]][temp[z + 1]] == "--" or board[temp[z]][temp[z + 1]][0] == "b":
                                        return_lst.append((temp[z], temp[z + 1]))
                                    elif board[temp[z]][temp[z + 1]][0] == "w":
                                        protected.append((z, z + 1))
                                elif board[x][y][0] == "b":
                                    if board[temp[z]][temp[z + 1]] == "--" or board[temp[z]][temp[z + 1]][0] == "w":
                                        return_lst.append((temp[z], temp[z + 1]))
                                    elif board[temp[z]][temp[z + 1]][0] == "b":
                                        protected.append((z, z + 1))
                        return return_lst


                    def knight_possible_move(board, x, y):
                        global protected
                        return_lst = []
                        temp = [x - 2, y + 1, x - 2, y - 1, x + 2, y + 1, x + 2, y - 1, x + 1, y - 2, x - 1, y - 2, x + 1, y + 2, x - 1,
                                y + 2]
                        for z in range(0, len(temp), 2):
                            if existsonboard(temp[z], temp[z + 1]):
                                if board[x][y][0] == "w":
                                    if board[temp[z]][temp[z + 1]] == "--" or board[temp[z]][temp[z + 1]][0] == "b":
                                        return_lst.append((temp[z], temp[z + 1]))
                                    elif board[temp[z]][temp[z + 1]][0] == "w":
                                        protected.append((z, z + 1))
                                elif board[x][y][0] == "b":
                                    if board[temp[z]][temp[z + 1]] == "--" or board[temp[z]][temp[z + 1]][0] == "w":
                                        return_lst.append((temp[z], temp[z + 1]))
                                    elif board[temp[z]][temp[z + 1]][0] == "b":
                                        protected.append((z, z + 1))
                        return return_lst


                    def rook_possible_move(board, x, y):
                        global protected
                        return_lst = []
                        if board[x][y][0] == "w":
                            for z in range(x + 1, 8):
                                if existsonboard(z, y):
                                    if board[z][y] == "--":
                                        return_lst.append((z, y))
                                    elif board[z][y][0] == "b":
                                        if existsonboard(z, y):
                                            return_lst.append((z, y))
                                        break
                                    elif board[z][y][0] == "w":
                                        protected.append((z, y))
                                        break
                            for z in range(x - 1, -1, -1):
                                if existsonboard(z, y):
                                    if board[z][y] == "--":
                                        return_lst.append((z, y))
                                    elif board[z][y][0] == "b":
                                        if existsonboard(z, y):
                                            return_lst.append((z, y))
                                        break
                                    elif board[z][y][0] == "w":
                                        protected.append((z, y))
                                        break
                            for z in range(y + 1, 8):
                                if existsonboard(x, z):
                                    if board[x][z] == "--":
                                        return_lst.append((x, z))
                                    elif board[x][z][0] == "b":
                                        if existsonboard(x, z):
                                            return_lst.append((x, z))
                                        break
                                    elif board[x][z][0] == "w":
                                        protected.append((x, z))
                                        break
                            for z in range(y - 1, -1, -1):
                                if existsonboard(x, z):
                                    if board[x][z] == "--":
                                        return_lst.append((x, z))
                                    elif board[x][z][0] == "b":
                                        if existsonboard(x, z):
                                            return_lst.append((x, z))
                                        break
                                    elif board[x][z][0] == "w":
                                        protected.append((x, z))
                                        break
                        if board[x][y][0] == "b":
                            for z in range(x + 1, 8):
                                if existsonboard(z, y):
                                    if board[z][y] == "--":
                                        return_lst.append((z, y))
                                    elif board[z][y][0] == "w":
                                        if existsonboard(z, y):
                                            return_lst.append((z, y))
                                        break
                                    elif board[z][y][0] == "b":
                                        protected.append((z, y))
                                        break
                            for z in range(x - 1, -1, -1):
                                if existsonboard(z, y):
                                    if board[z][y] == "--":
                                        return_lst.append((z, y))
                                    elif board[z][y][0] == "w":
                                        if existsonboard(z, y):
                                            return_lst.append((z, y))
                                        break
                                    elif board[z][y][0] == "b":
                                        protected.append((z, y))
                                        break
                            for z in range(y + 1, 8):
                                if existsonboard(x, z):
                                    if board[x][z] == "--":
                                        return_lst.append((x, z))
                                    elif board[x][z][0] == "w":
                                        if existsonboard(x, z):
                                            return_lst.append((x, z))
                                        break
                                    elif board[x][z][0] == "b":
                                        protected.append((x, z))
                                        break
                            for z in range(y - 1, -1, -1):
                                if existsonboard(x, z):
                                    if board[x][z] == "--":
                                        return_lst.append((x, z))
                                    elif board[x][z][0] == "w":
                                        if existsonboard(x, z):
                                            return_lst.append((x, z))
                                        break
                                    elif board[x][z][0] == "b":
                                        protected.append((x, z))
                                        break
                        return return_lst


                    def pawn_possible_move(board, x, y):
                        global protected
                        return_lst = []
                        if board[x][y][0] == "w":
                            if existsonboard(x - 2, y) and x == 6 and board[x - 2][y] == "--" and board[x - 1][y] == "--":
                                return_lst.append((x - 2, y))
                            if existsonboard(x - 1, y) and board[x - 1][y] == "--":
                                return_lst.append((x - 1, y))
                            if existsonboard(x - 1, y - 1) and board[x - 1][y - 1][0] == "b":
                                return_lst.append((x - 1, y - 1))
                            elif existsonboard(x - 1, y - 1) and board[x - 1][y - 1][0] == "w":
                                protected.append((x - 1, y - 1))
                            if existsonboard(x - 1, y + 1) and board[x - 1][y + 1][0] == "b":
                                return_lst.append((x - 1, y + 1))
                            elif existsonboard(x - 1, y + 1) and board[x - 1][y + 1][0] == "w":
                                protected.append((x - 1, y + 1))
                        elif existsonboard(y, x) and board[x][y][0] == "b":
                            if x == 1 and board[x + 2][y] == "--" and existsonboard(x + 2, y) and board[x + 1][y] == "--":
                                return_lst.append((x + 2, y))
                            if existsonboard(x + 1, y) and board[x + 1][y] == "--":
                                return_lst.append((x + 1, y))
                            if existsonboard(x + 1, y + 1) and board[x + 1][y + 1][0] == "w":
                                return_lst.append((x + 1, y + 1))
                            elif existsonboard(x + 1, y + 1) and board[x + 1][y + 1][0] == "b":
                                protected.append((x + 1, y + 1))
                            if existsonboard(x + 1, y - 1) and board[x + 1][y - 1][0] == "w":
                                return_lst.append((x + 1, y - 1))
                            elif existsonboard(x + 1, y - 1) and board[x + 1][y - 1][0] == "b":
                                protected.append((x + 1, y - 1))
                        return return_lst


                    def queen_possible_move(board, x, y):
                        return_lst = []
                        temp_list_a = bishop_possible_move(board, x, y)
                        temp_list_b = rook_possible_move(board, x, y)
                        return_lst = temp_list_a + temp_list_b
                        return return_lst


                    def piece_type_invoker(x, y):
                        if "R" in board[x][y]:
                            return rook_possible_move(board, x, y)
                        elif "N" in board[x][y]:
                            return knight_possible_move(board, x, y)
                        elif "B" in board[x][y]:
                            return bishop_possible_move(board, x, y)
                        elif "Q" in board[x][y]:
                            return queen_possible_move(board, x, y)
                        elif "K" in board[x][y]:
                            return king_possible_move(board, x, y)
                        elif "p" in board[x][y]:
                            return pawn_possible_move(board, x, y)


                    def isEqual(val1, val2):
                        if val1 == val2:
                            return True
                    validmove = True
                    dumbo = 2
                    move_list = []
                    piecefinal = ""
                    movecount = 1
                    def movelog(team):
                        print("The co-ordinates of the move done is:" + str(coord))
                        checker = True
                        global move_list
                        global movecount
                        global dumbo
                        global validmove
                        # coord 1 is the file
                        # coord 0 is the rank
                        global piecefinal
                        prev_move = ""

                        if validmove == True:
                                        if piecetype[1] == "N":
                                            piecefinal = piecefinal + "N"

                                        if piecetype[1] == "K":
                                            piecefinal = piecefinal + "K"

                                        if piecetype[1] == "R":
                                            piecefinal = piecefinal + "R"

                                        if piecetype[1] == "B":
                                            piecefinal = piecefinal + "B"

                                        if piecetype[1] == "Q":
                                            piecefinal = piecefinal + "Q"

                                        if coord[1] == 0:
                                            piecefinal = piecefinal + "a"
                                        elif coord[1] == 1:
                                            piecefinal = piecefinal + "b"
                                        elif coord[1] == 2:
                                            piecefinal = piecefinal + "c"
                                        elif coord[1] == 3:
                                            piecefinal = piecefinal + "d"
                                        elif coord[1] == 4:
                                            piecefinal = piecefinal + "e"
                                        elif coord[1] == 5:
                                            piecefinal = piecefinal + "f"
                                        elif coord[1] == 6:
                                            piecefinal = piecefinal + "g"
                                        elif coord[1] == 7:
                                            piecefinal = piecefinal + "h"

                                        if coord[0] == 0:
                                            piecefinal = piecefinal + "8"

                                        elif coord[0] == 1:
                                            piecefinal = piecefinal + "7"

                                        elif coord[0] == 2:
                                            piecefinal = piecefinal + "6"

                                        elif coord[0] == 3:
                                            piecefinal = piecefinal + "5"

                                        elif coord[0] == 4:
                                            piecefinal = piecefinal + "4"

                                        elif coord[0] == 5:
                                            piecefinal = piecefinal + "3"

                                        elif coord[0] == 6:
                                            piecefinal = piecefinal + "2"

                                        elif coord[0] == 6:
                                            piecefinal = piecefinal + "1"

                                        if is_check == True:
                                            move_list.append(move_list[-1] + "+")
                                            print("The value in question is" + str(move_list[-2]))
                                            del move_list[-2]
                                        if movecount == 1:
                                            move_list.append("1.")
                                        elif movecount % 2 != 0:
                                            move_list.append(str(dumbo) + ".")
                                            dumbo += 1
                                        move_list.append(piecefinal)
                                        print("The move count is" + str(movecount))
                                        print(piecefinal)
                                        if len(move_list)%3 == 0 and len(move_list)>=3:
                                            loader = pygame.transform.scale(pygame.image.load("ChessImage\whitey.jpg"), (400, 600))
                                            screen.blit(loader, (800, 230))
                                            print_log(move_list)
                                        print(move_list)
                                        piecefinal = ""
                                        movecount += 1
                                        board_reference = [
                                            ["0,0", "0,1", "0,2", "0,3", "0,4", "0,5", "0,6", "0,7"],
                                            ["1,0", "1,1", "1,2", "1,3", "1,4", "1,5", "1,6", "1,7"],
                                            ["2,0", "2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7"],
                                            ["3,0", "3,1", "3,2", "3,3", "3,4", "3,5", "3,6", "3,7"],
                                            ["4,0", "4,1", "4,2", "4,3", "4,4", "4,5", "4,6", "4,7"],
                                            ["5,0", "5,1", "5,2", "5,3", "5,4", "5,5", "5,6", "5,7"],
                                            ["6,0", "6,1", "6,2", "6,3", "6,4", "6,5", "6,6", "6,7"],
                                            ["7,0", "7,1", "7,2", "7,3", "7,4", "7,5", "7,6", "7,7"]
                                        ]

                                        print(coord[1])
                    def print_log(move_list):
                        print_list = move_list
                        if len(print_list) >18:
                            for y in range(0,len(print_list)-18):
                                print_list.pop(0)
                        line_1 = "Move Log:"
                        text = font_movelist.render(line_1, True, BLACK)
                        textRect = text.get_rect()
                        textRect.center = (860,250)
                        screen.blit(text, textRect)
                        count = 0
                        for x in reversed(range(len(print_list)//3)):
                            line_1 = str(print_list[(3*(x+1)-3)])+ str(print_list[(3*(x+1)-2)]) + str(print_list[(3*(x+1)-1)])
                            print("testing_2",line_1)
                            print("values",(3*x)-3,(3*x)-2,(3*x)-1)
                            if count == 0:
                                text = font_movelist.render(line_1, True, HIGHLIGHTCOLOR)
                            else:
                                text = font_movelist.render(line_1, True, BLACK)
                            textRect = text.get_rect()
                            print("testing",(300+count))
                            textRect.topleft = (810,300+count)
                            count = count + 50
                            screen.blit(text, textRect)

                    '''def stalemate(turn):# does not work
                        w = is_king_check("w")
                        w_king_coordinates = king_pos("w")
                        w_king_moves = king_possible_move(board,w_king_coordinates[0],w_king_coordinates[1])
                        b = is_king_check("b")
                        b_king_coordinates = king_pos("b")
                        b_king_moves = king_possible_move(board, b_king_coordinates[0], b_king_coordinates[1])
                    
                        if isEqual(w, w_king_moves) == True:
                                print("White is stalemated")
                        if isEqual(b, b_king_moves) == True:
                                print("Black is stalemated")'''


                    def piece_type_check(team):
                        all_possible_moves = []
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                if board[c][r][1] != "K":
                                    temp = piece_type_invoker(c, r)
                                    if temp != None and board[c][r][0] == team:
                                        all_possible_moves = all_possible_moves + piece_type_invoker(c, r)
                        final_possible_moves = list(dict.fromkeys(all_possible_moves))
                        return final_possible_moves


                    def piece_type_checker(team):
                        all_possible_moves = []
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                temp = piece_type_invoker(c, r)
                                if temp != None and board[c][r][0] == team:
                                    all_possible_moves = all_possible_moves + piece_type_invoker(c, r)
                        final_possible_moves = list(dict.fromkeys(all_possible_moves))
                        return final_possible_moves


                    def king_pos(team):
                        temp = team + "K"
                        for r in range(DIMENSION):
                            for c in range(DIMENSION):
                                if board[c][r] == temp:
                                    return (c, r)


                    def is_king_dup_check(team):
                        Bool = False
                        temp = king_pos(team)
                        temp1 = king_pos(turn_inverter(team))  # This is to intersect both king's moves
                        index = piece_type_invoker(temp[0], temp[1])
                        index1 = piece_type_invoker(temp1[0], temp1[1])  # This is array for the opp king
                        for x in index:
                            if x in index1:
                                return True
                        return False


                    def is_king_check(team):
                        return_lst = []
                        temp = king_pos(team)
                        temp1 = king_pos(turn_inverter(team))  # This is to intersect both king's moves
                        index1 = piece_type_invoker(temp1[0], temp1[1])  # This is array for the opp king
                        index_2 = piece_type_checker(turn_inverter(team))
                        index = piece_type_invoker(temp[0], temp[1])
                        index.append(king_pos(team))

                        for x in index:
                            if x in index1:
                                return_lst.append(x)
                        for c in index:
                            if c in index_2:
                                print(c)
                                return_lst.append(c)
                        print(return_lst)
                        return return_lst


                    def piece_in_range(turn, king_moves):
                        temp = piece_type_checker(turn_inverter(turn))
                        for x in king_moves:
                            if board[x[0]][x[1]][0] == turn_inverter(turn):
                                for y in protected_store:
                                    if x == y:
                                        return y
                            if board[x[0]][x[1]][0] == turn_inverter(turn) and x in temp:
                                return x


                    def display_check(turn):
                        global is_check
                        if is_check == True:
                            king_position = king_pos(turn)
                            color = pygame.transform.scale(pygame.image.load("ChessImage/checkbox.jpg"), (100, 100))
                            screen.blit(color,
                                        pygame.Rect(king_position[1] * squaresize, king_position[0] * squaresize, squaresize, squaresize))


                    def checkmate_test(turn):
                        global is_check
                        global piecefinal
                        clear_promo()
                        checkmate = False
                        opponent_moves = piece_type_checker(turn_inverter(turn))
                        king_position = king_pos(turn)
                        king_moves = king_possible_move(board, king_position[0], king_position[1])
                        if king_position in opponent_moves:
                            print("Check")
                            is_check = True
                            mainsound2 = Sound.Audio()
                            mainsound2.playCheck()
                            opponent_moves.append(piece_in_range(turn, king_moves))
                            king_moves.append(king_position)

                            for x in king_moves:
                                if x in opponent_moves:

                                    checkmate = True
                                else:
                                    checkmate = False
                                    break
                        else:
                            is_check = False
                        return checkmate


                    """def checkmate(turn):# doing check rn
                        checkmate = False
                        w = is_king_check("w")
                        w_king_coordinates = king_pos("w")
                        w_king_moves = king_possible_move(board,w_king_coordinates[0],w_king_coordinates[1])
                        w_king_moves.append(w_king_coordinates)
                        w_team_moves = piece_type_check("w")#here
                        b = is_king_check("b")
                        b_king_coordinates = king_pos("b")
                        b_king_moves = king_possible_move(board, b_king_coordinates[0], b_king_coordinates[1])
                        b_king_moves.append(b_king_coordinates)
                        b_team_moves = piece_type_check("b")#here
                        if isEqual(w, w_king_moves) == True:
                    
                            for x in w:
                                if x not in w_team_moves:
                                    print()
                                else:
                                    return("Check!")
                            print("W Checkmated")
                        print(b,"b moves")
                        print(b_king_moves,"king possible moves")
                        if isEqual(b, b_king_moves) == True:
                            print("Black King moves",b)
                            print("Black team moves",b_team_moves)
                            for x in b:
                                if x not in b_team_moves:
                                    print()
                                else:
                                    return("check!")
                            print("B Checkmated")"""




                    def move(click_1, return_lst, click_2):
                        global protected
                        global protected_store
                        global coord
                        global piecetype
                        x1 = click_1[0]
                        y1 = click_1[1]
                        x2 = click_2[0]
                        y2 = click_2[1]
                        if return_lst != None:
                            for z in return_lst:
                                if (x2, y2) == z:
                                    board[x2][y2] = board[x1][y1]
                                    piecetype = board[x1][y1]
                                    coord = (x2, y2)
                                    board[x1][y1] = "--"
                                    protected.clear()
                                    if emptySpaceCount() == True:
                                        emptySpaceCount()
                                        return True
                                    mainsound2 = Sound.Audio()
                                    mainsound2.playMove()

                                    return True


                    def check():
                        return_val = []
                        w = is_king_check("w")
                        b = is_king_check("b")
                        if w != None and w != []:
                            if king_pos("w") in w:
                                return_val = "IW"

                        if b != None and b != []:
                            if king_pos("b") in b:
                                return_val = "IB"
                        if w != None and w != [] and b != None and b != []:
                            if king_pos("b") in b and king_pos("w") in w:
                                return_val = "both"
                        return return_val


                    def turn_inverter(turn):
                        if turn == "w":
                            return "b"
                        if turn == "b":
                            return "w"


                    def prev_move_file(board):
                        file = open("prev_move.txt", "w")
                        for x in board:
                            for y in x:
                                temp = str(y) + "\n"
                                file.write(temp)
                            file.write('reset\n')
                        file.close()


                    '''def checkhighlighter():
                        w = is_king_check("w")
                        b = is_king_check("b")
                        if w != None and w != []:
                            if king_pos("w") in w:
                                return w
                            return w
                        if b != None and b != []:
                            if king_pos("b") in b:
                                return b
                            return b
                        return None'''


                    def castling(turn):
                        global click_motion
                        if turn == "w":
                            if board[7][0] == "wR" and board[7][4] == "wK" and board[7][3] == "--" and board[7][2] == "--" and board[7][
                                1] == "--" and click_motion[0] == (7, 4) and click_motion[1] == (7, 0):
                                board[7][2] = "wK"
                                board[7][3] = "wR"
                                board[7][4] = "--"
                                board[7][0] = "--"
                            elif board[7][7] == "wR" and board[7][4] == "wK" and board[7][6] == "--" and board[7][5] == "--" and \
                                    click_motion[0] == (7, 4) and click_motion[1] == (7, 7):
                                board[7][5] = "wR"
                                board[7][6] = "wK"
                                board[7][4] = "--"
                                board[7][7] = "--"
                        elif turn == "b":
                            if board[0][0] == "bR" and board[0][4] == "bK" and board[0][3] == "--" and board[0][2] == "--" and board[0][
                                1] == "--" and click_motion[0] == (0, 4) and click_motion[1] == (0, 0):
                                board[0][2] = "bK"
                                board[0][3] = "bR"
                                board[0][4] = "--"
                                board[0][0] = "--"
                            elif board[0][7] == "bR" and board[0][4] == "bK" and board[0][6] == "--" and board[0][5] == "--" and \
                                    click_motion[0] == (0, 4) and click_motion[1] == (0, 7):
                                board[0][5] = "bR"
                                board[0][6] = "bK"
                                board[0][4] = "--"
                                board[0][7] = "--"








                    def load(turn):
                        dummy = []
                        temp_dummy = []
                        file = open("prev_move.txt", "r")
                        for x in file:
                            if x == "reset\n":
                                dummy.append(list(temp_dummy))
                                temp_dummy.clear()
                            else:
                                temp_dummy.append(x[0:2])
                        for x in range(DIMENSION):
                            for y in range(DIMENSION):
                                board[x][y] = dummy[x][y]
                        mainsound2 = Sound.Audio()
                        mainsound2.invalidmove()
                        display_check(turn)


                    def promotion():
                        colors = [LIGHT_SQUARE_PNG, DARK_SQUARE_PNG]
                        for x in range(DIMENSION):
                            if board[0][x] == "wp":
                                print("White promotion time")
                                mainsound2 = Sound.Audio()
                                mainsound2.playPromotion()
                                return (0, x)
                        for x in range(DIMENSION):
                            if board[7][x] == "bp":
                                print("Black promotion time")
                                mainsound2 = Sound.Audio()
                                mainsound2.playPromotion()
                                return (7, x)


                    def print_checkmate(turn):
                        if turn == "w":
                            txt = "White"
                        elif turn == "b":
                            txt = "Black"
                        text = font.render(txt, True, BLACK)
                        textRect = text.get_rect()
                        textRect.center = (1000, 50)
                        screen.blit(text, textRect)
                        text = font.render("Checkmated!", True, BLACK)
                        mainsound2 = Sound.Audio()
                        mainsound2.checkMate()
                        textRect = text.get_rect()
                        textRect.center = (1000, 100)
                        screen.blit(text, textRect)


                    def promo_menu(team):
                        global lst
                        text = font.render('Promotion!', True, BLACK)
                        textRect = text.get_rect()
                        textRect.center = (1000, 50)
                        screen.blit(text, textRect)

                        if team == "w":
                            lst = ["wQ", "wB", "wR", "wN"]
                            screen.blit(Graphics["wQ"], (800, 100))
                            screen.blit(Graphics["wB"], (900, 100))
                            screen.blit(Graphics["wR"], (1000, 100))
                            screen.blit(Graphics["wN"], (1100, 100))
                        if team == "b":
                            lst = ["bQ", "bB", "bR", "bN"]
                            screen.blit(Graphics["bQ"], (800, 100))
                            screen.blit(Graphics["bB"], (900, 100))
                            screen.blit(Graphics["bR"], (1000, 100))
                            screen.blit(Graphics["bN"], (1100, 100))


                    def clear_promo():
                        loader = pygame.transform.scale(pygame.image.load("ChessImage\whitey.jpg"), (400, 200))
                        screen.blit(loader, (800, 0))


                    def king_king_exception(turn):
                        temp_king_king_1 = king_pos(turn)
                        temp_king_king_2 = king_pos(turn_inverter(turn))
                        temp_king_moves1 = king_possible_move(board, temp_king_king_2[0], temp_king_king_2[1])
                        temp_king_moves2 = king_possible_move(board, temp_king_king_1[0], temp_king_king_1[1])
                        if temp_king_king_1 in temp_king_moves1 and temp_king_king_2 in temp_king_moves2:
                            load(turn)
                            return True


                    def emptySpaceCount():
                        emptyspacecount = 0
                        maxspacecount = 32
                        for x in range(8):
                            for y in range(8):
                                 if board[x][y] == "--":
                                        emptyspacecount = emptyspacecount + 1
                                        print("The empty space count is:" + str(emptyspacecount))
                        if emptyspacecount > maxspacecount:
                            print("The empty space count is:" + str(emptyspacecount))
                            mainsound = Sound.Audio()
                            mainsound.playMove() #FIX THIS FUNCTION IF IT CAN WORK IF SIR U ARE READING THIS IT WORKS 100%
                            maxspacecount = emptyspacecount + 1
                            print("The max space count is:" + str(maxspacecount))
                            return True
                        return False






                    click_motion = []


                    def randy():
                        global is_check
                        clock = pygame.time.Clock()
                        clock.tick(60)
                        global protected
                        global protected_store
                        global validmove
                        promocheck = False
                        promo = None
                        boardlock = False
                        global click_motion
                        return_lst = []
                        turn = first_move
                        run = True
                        mainsound = Sound.Audio()
                        mainsound.playGameAudio()
                        while run:
                            drawBoard()
                            test()
                            test4(return_lst, click_motion)
                            test()
                            display_check(turn)
                            test()
                            save_button()
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    for x in range(DIMENSION):
                                                for y in range(DIMENSION):
                                                    board[x][y] = preset[x][y]
                                    run = False
                                    screen = pygame.display.set_mode((800, 700))
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    prev_move_file(board)
                                    current_position = pygame.mouse.get_pos()
                                    col = current_position[0] // squaresize
                                    row = current_position[1] // squaresize
                                    if len(protected) > 0 or piece_type_checker(turn):
                                        protected_store = protected
                                        print("Protected Var", protected)
                                        protected.clear()
                                    if row < 8 and col < 8 and boardlock == False:
                                        playersquare = (row, col)
                                        print("coordinates:", playersquare)
                                        # click thingy
                                        click_motion.append(playersquare)
                                        if len(click_motion) == 1 and board[click_motion[0][0]][click_motion[0][1]][0] == turn:
                                            # stalemate(turn)
                                            return_lst = piece_type_invoker(row,
                                                                            col)  # returns possible moves of a piece thius is workking function
                                            # return_lst = piece_type_checker("w") #this is checking shenanigans
                                            if len(return_lst) == 0:
                                                click_motion.clear()
                                        elif board[click_motion[0][0]][click_motion[0][1]] == "--" or \
                                                board[click_motion[0][0]][click_motion[0][1]][0] != turn:
                                            click_motion.clear()

                                        if len(click_motion) == 2:

                                            if click_motion[0] == (7, 4) and click_motion[1] == (7, 0):
                                                castling(turn)
                                                turn = turn_inverter(turn)

                                            elif click_motion[0] == (7, 4) and click_motion[1] == (7, 7):
                                                castling(turn)
                                                turn = turn_inverter(turn)


                                            elif click_motion[0] == (0, 4) and click_motion[1] == (0, 0):
                                                castling(turn)
                                                turn = turn_inverter(turn)

                                            elif click_motion[0] == (0, 4) and click_motion[1] == (0, 7):
                                                castling(turn)
                                                turn = turn_inverter(turn)

                                            if click_motion[0] == click_motion[1]:
                                                click_motion.clear()

                                            elif move(click_motion[0], return_lst, click_motion[1]) == True:
                                                movelog(turn)
                                                promo = promotion()
                                                if promo != None and promo != "" and promo[0] == 0:
                                                    promo_menu("w")
                                                    promocheck = True
                                                    boardlock = True
                                                if promo != None and promo != "" and promo[0] == 7:
                                                    promo_menu("b")
                                                    promocheck = True
                                                    boardlock = True
                                                pygame.display.update()
                                                verdict = check()
                                                if verdict == "both":
                                                    load(turn)
                                                    validmove = False
                                                    turn = turn_inverter(turn)
                                                elif verdict == "IB" and turn == "b":
                                                    load(turn)
                                                    validmove = False
                                                    turn = turn_inverter(turn)
                                                elif verdict == "IW" and turn == "w":
                                                    load(turn)
                                                    validmove = False
                                                    turn = turn_inverter(turn)
                                                elif king_king_exception(turn) == True:
                                                    is_check = False
                                                    validmove = False
                                                    turn = turn_inverter(turn)
                                                elif checkmate_test(turn_inverter(turn)) == True:
                                                    print_checkmate(turn_inverter(turn))
                                                else:
                                                    validmove = True

                                                # elif verdict == "IW" and is_king_dup_check(turn) == True:
                                                #  print("Situation consdiered for W")
                                                #  load()
                                                #  turn = turn_inverter(turn)
                                                pygame.display.update()
                                                turn = turn_inverter(turn)
                                            click_motion.clear()
                                    else:
                                        if promocheck == True:
                                            promo_menu(turn_inverter(turn))
                                        global lst
                                        print(row, col)
                                        if row == 1 and col == 8 and len(lst) == 4:
                                            temp = turn_inverter(turn) + "Q"
                                            board[promo[0]][promo[1]] = temp
                                            clear_promo()
                                            boardlock = False
                                            promocheck = False
                                        if row == 1 and col == 9 and len(lst) == 4:
                                            temp = turn_inverter(turn) + "B"
                                            board[promo[0]][promo[1]] = temp
                                            clear_promo()
                                            boardlock = False
                                            promocheck = False
                                        if row == 1 and col == 10 and len(lst) == 4:
                                            temp = turn_inverter(turn) + "R"
                                            board[promo[0]][promo[1]] = temp
                                            clear_promo()
                                            boardlock = False
                                            promocheck = False
                                        if row == 1 and col == 11 and len(lst) == 4:
                                            temp = turn_inverter(turn) + "N"
                                            board[promo[0]][promo[1]] = temp
                                            clear_promo()
                                            boardlock = False
                                            promocheck = False

                                        if row >= 7 and row <= 8 and row == 7 and col >= 8 and col <= 12:
                                            saved = Save_Load.Save(save(),turn)
                                            saved.run()
                                            for x in range(DIMENSION):
                                                for y in range(DIMENSION):
                                                    board[x][y] = preset[x][y]
                                            run = False

                                            screen = pygame.display.set_mode((800, 700))


                                        lst = []

                            pygame.display.update()


                    '''def test3(return_lst, click_motion): # WORKING FUNCTION
                        if len(click_motion) == 1:
                            for r in range(DIMENSION):
                                for c in range(DIMENSION):
                                 if (r, c) in return_lst:
                                        pygame.draw.rect(screen, HIGHLIGHTCOLOR, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))
                    
                                #ADD-MOVEMENT with DESLECT option AND NEW array which appends TWO player clicks together so that we can transfer to main array
                    '''

                    '''def test5(return_lst, click_motion):
                        colors = [pygame.Color(LIGHT_SQUARE), pygame.Color(DARK_SQUARE)]
                        if len(click_motion) == 1:
                            for r in range(DIMENSION):
                                for c in range(DIMENSION):
                                    if (r, c) in return_lst:
                                        screen.blit(highlight, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))'''
                    ''' WORKING FUNCTION
                    def test4(return_lst, click_motion):
                        colors = [pygame.Color(LIGHT_SQUARE), pygame.Color(DARK_SQUARE)]
                        if len(click_motion) == 1:
                            for r in range(DIMENSION):
                                for c in range(DIMENSION):
                                    if checkhighlighter() != None:
                                        print("mango")
                                        if (r, c) in checkhighlighter():
                                            print("mango 2")
                                            screen.blit(INVALID_MOVE_PNG, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))
                                    if (r, c) in return_lst:
                                        screen.blit(highlight, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))
                    '''


                    def test4(return_lst, click_motion):
                        colors = [pygame.Color(LIGHT_SQUARE), pygame.Color(DARK_SQUARE)]
                        if len(click_motion) == 1:
                            for r in range(DIMENSION):
                                for c in range(DIMENSION):
                                    if (r, c) in return_lst:
                                        screen.blit(highlight, pygame.Rect(c * squaresize, r * squaresize, squaresize, squaresize))




                    randy()




                    class Board:
                        def __init__(self):
                            self.board = self.board = [['  ' for i in range(8)] for i in range(8)]


                    class Piece:
                        def __init__(self, team, type, image):
                            self.team = team  # There can be two teams, they are defined as 'w' for White and 'b' for Black
                            self.type = type
                            self.image = image

                            '''There can be 6 different types of pieces, they are defined as:
                            Pawn = p
                            King = k
                            Queen = q
                            Rook = r
                            Knight = n
                            Bishop = b
                    
                            So, in this case, a black pawn would be: bp (In terms of nomanclature)
                            '''


                    '''
                    white_pawn = Piece('w', 'p', 'wp.png')
                    white_king = Piece('w', 'k', 'wK.png')
                    white_queen = Piece('w', 'q', 'wQ.png')
                    white_rook = Piece('w', 'r', 'wR.png')
                    white_knight = Piece('w', 'n', 'wK.png')
                    white_bishop = Piece('w', 'b', 'wB.png')
                    
                    black_pawn = Piece('b', 'p', 'bp.png')
                    black_king = Piece('b', 'k', 'bK.png')
                    black_queen = Piece('b', 'q', 'bQ.png')
                    black_rook = Piece('b', 'r', 'bR.png')
                    black_knight = Piece('b', 'n', 'bK.png')
                    black_bishop = Piece('b', 'b', 'bB.png')
                    
                    '''










