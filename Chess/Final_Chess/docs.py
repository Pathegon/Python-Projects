WHITE = (255, 255, 255)  # Color Codes
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
DARK_SQUARE = (126, 217, 87)
LIGHT_SQUARE = (255, 255, 255)
HIGHLIGHTCOLOR = (186, 202, 68)
import Sound
import pygame
pygame.init()
class documentation():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess (Don't know how we managed to do this)")
        self.MAIN_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/Credits.png"), (800, 800))
        self.BACK_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/back.png"), (100, 100))
        mainsound2 = Sound.Audio()
        mainsound2.credit()
    def run(self):
        runs = True
        while runs:
            button = self.MAIN_MENU_PNG.get_rect()
            button.center = (400,400)
            self.screen.blit(self.MAIN_MENU_PNG,button)
            back = self.BACK_MENU_PNG.get_rect()
            back.center = (50,50)
            self.screen.blit(self.BACK_MENU_PNG,button)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runs = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_position = pygame.mouse.get_pos()
                    col_1 = current_position[0]
                    row_1 = current_position[1]
                    if col_1 >= 0 and col_1 <= 100 and row_1 >= 0 and row_1 <= 100:
                        runs = False
        mainsound2 = Sound.Audio()
        mainsound2.playBGAudio()
class rate_us():
    def __init__(self):
        self.screen = pygame.display.set_mode((474, 800))
        pygame.display.set_caption("Chess (Don't know how we managed to do this)")
        self.MAIN_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/rate.jpg"), (474, 800))
        self.BACK_MENU_PNG = pygame.transform.scale(pygame.image.load("ChessImage/back.png"), (50, 50))
        mainsound2 = Sound.Audio()
        mainsound2.docs()
    def run(self):
        runs = True
        while runs:
            button = self.MAIN_MENU_PNG.get_rect()
            button.center = (237,400)
            self.screen.blit(self.MAIN_MENU_PNG,button)
            back = self.BACK_MENU_PNG.get_rect()
            back.center = (449,25)
            self.screen.blit(self.BACK_MENU_PNG,back)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runs = False
                    self.screen = pygame.display.set_mode((800, 700))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_position = pygame.mouse.get_pos()
                    col_1 = current_position[0]
                    row_1 = current_position[1]
                    if col_1 >= 424 and col_1 <= 474 and row_1 >= 0 and row_1 <= 50:
                        runs = False
                        self.screen = pygame.display.set_mode((800, 700))
        mainsound2 = Sound.Audio()
        mainsound2.playBGAudio()






