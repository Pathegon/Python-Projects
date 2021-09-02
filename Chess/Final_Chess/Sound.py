import game
import docs
import sys
import pygame
import os


#Channel 1 is for sound effects
#Channel 0 is for general music
class Audio:
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=4)
        self.chan1 = pygame.mixer.find_channel(True)
    def playGameAudio(self):
        self.randomMusic = pygame.mixer.music.load('ChessImage/audio/mainGameMusic.mp3')
        pygame.mixer.Channel(0).fadeout(3000)
        pygame.mixer.Channel(0).set_volume(0.2)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('ChessImage/audio/mainGameMusic.mp3'))
    def playBGAudio(self):
        self.bgMusic = pygame.mixer.music.load('ChessImage/audio/mainBGMusic.mp3')
        pygame.mixer.Channel(0).fadeout(3000)
        pygame.mixer.Channel(0).set_volume(0.2)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('ChessImage/audio/mainBGMusic.mp3'), maxtime=300000)

    def playCaputre(self):
        self.Capture = pygame.mixer.music.load('ChessImage/audio/Capture.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/Capture.mp3'), maxtime=600)

    def playMove(self):
            pygame.mixer.music.set_volume(1)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/Move.mp3'), maxtime=600)
            pygame.mixer.music.set_volume(0.3)
    def playCheck(self):
            pygame.mixer.music.set_volume(1)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/Check.mp3'), maxtime=6000)
            pygame.mixer.music.set_volume(0.3)
    def Mute (self):
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.Channel(1).set_volume(0)
    def unMute (self):
        pygame.mixer.Channel(0).set_volume(0.2)
        pygame.mixer.Channel(1).set_volume(10)
    def checkMate(self):
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/checkmate.mp3'), maxtime=300000)
    def playPromotion(self):
        pygame.mixer.music.set_volume(1)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/promotion.mp3'), maxtime=6000)
        pygame.mixer.music.set_volume(0.3)
    def invalidmove(self):
        pygame.mixer.music.set_volume(1)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('ChessImage/audio/invalidmove.mp3'), maxtime=6000)
        pygame.mixer.music.set_volume(0.3)

    def credit(self):
        pygame.mixer.Channel(0).set_volume(0.2)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('ChessImage/audio/credit.mp3'))
    def docs(self):
        pygame.mixer.Channel(0).set_volume(0.2)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('ChessImage/audio/doclist.mp3'))
