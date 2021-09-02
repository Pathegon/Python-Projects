WHITE = (255, 255, 255)  # Color Codes
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
DARK_SQUARE = (126, 217, 87)
LIGHT_SQUARE = (255, 255, 255)
HIGHLIGHTCOLOR = (186, 202, 68)
import game
import docs
import sys
import pygame
import Save_Load
import Sound
pygame.init()
class menu():
    def __init__(self):
        self.default = 0.3
        self.screen = pygame.display.set_mode((800, 700))
        self.prev_call = False
        self.SOUND_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/sound.png"), (40, 40))
        self.DOC_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/doc.png"), (40, 40))
        self.preset = [
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                    ]


    def display(self):
        MAIN_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/menu_2.png"), (800, 800))
        LOGO_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/logo.png"), (300, 300))
        PLAYBUTTON_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/playbutton.png"), (200, 100))
        LOADBUTTON_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/loadbutton.png"), (200, 100))
        QUITBUTTON_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/quitbutton.png"), (200, 100))
        RATE_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/rate.png"), (100, 40))
        SOUND_PLUS_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/plus.png"), (40, 40))
        SOUND_MINUS_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/minus.png"), (40, 40))
        pygame.display.set_caption("Desi Chess (Don't know how we managed to do this)")
        self.button(MAIN_MENU_PNG,400,400)
        self.button(LOGO_MENU_PNG,400,100)
        self.button(PLAYBUTTON_MENU_PNG,400,300)
        self.button(LOADBUTTON_MENU_PNG,400,420)
        self.button(QUITBUTTON_MENU_PNG,400,540)
        self.button(self.SOUND_MENU_PNG,320,620)
        self.button(self.DOC_MENU_PNG,370,620)
        self.button(RATE_MENU_PNG,450,620)
        self.button(SOUND_PLUS_MENU_PNG,320,660)
        self.button(SOUND_MINUS_MENU_PNG,370,660)

        pygame.display.update()
    def button(self,img,row,col):
        button = img.get_rect()
        button.center = (row,col)
        self.screen.blit(img,button)
    def run(self):
        runs = True
        obj1 = volumeslider()
        obj1.playBGAudio()
        while runs:
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runs = False
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_position = pygame.mouse.get_pos()
                    col_1 = current_position[0]
                    row_1 = current_position[1]
                    print(col_1,row_1)
                    if col_1 >= 300 and col_1 <= 500 and row_1 >= 250 and row_1 <= 350: #play
                        Chess = game.GameEngine("w",self.preset)
                        obj = Sound.Audio()
                        obj.playBGAudio()
                    if col_1 >= 300 and col_1 <= 500 and row_1 >= 370 and row_1 <= 470: #load
                            loading = Save_Load.Load()
                            dummy = loading.run()
                            file1 = open("Save_turn.txt","r")
                            turn = file1.read()
                            Chess = game.GameEngine(turn,dummy)
                            obj = Sound.Audio()
                            obj.playBGAudio()
                    if col_1 >= 300 and col_1 <= 500 and row_1 >= 490 and row_1 <= 590: #quit
                        runs = False
                        sys.exit(0)
                    if col_1 >= 300 and col_1 <= 340 and row_1 >= 600 and row_1 <= 640: #audio off/on
                        if self.prev_call == False:
                            self.prev_call = True
                            self.SOUND_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/soundoff.png"), (40, 40))
                            obj1.Mute()
                        elif self.prev_call == True:
                            self.prev_call = False
                            self.SOUND_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/sound.png"), (40, 40))
                            obj1.unMute()
                    if col_1 >= 350 and col_1 <= 390 and row_1 >= 600 and row_1 <= 640:
                            doc = docs.documentation()
                            doc.run()
                    if col_1 >= 400 and col_1 <= 500 and row_1 >= 600 and row_1 <= 640:
                            plis = docs.rate_us()
                            plis.run()
                    if col_1 >= 300 and col_1 <= 340 and row_1 >= 640 and row_1 <= 680:
                        self.default +=0.2
                        obj1.volume_change(self.default)
                    if col_1 >= 350 and col_1 <= 390 and row_1 >= 640 and row_1 <= 680:
                        self.default -=0.2
                        obj1.volume_change(self.default)


class volumeslider(Sound.Audio,menu):
    def __init__(self):
        super().__init__()
    def volume_change(self,defa):
        pygame.mixer.Channel(0).set_volume(defa)
        pygame.mixer.Channel(1).set_volume(defa)



menu_test = menu()
menu_test.run()



