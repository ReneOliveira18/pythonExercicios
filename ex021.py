# importar uma musica e rodar com o Python

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.event.wait()
x = input('Type something to stop the music...')


