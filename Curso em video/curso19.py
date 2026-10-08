import pygame

pygame.init()

print("Tocando um MP3\n")

pygame.mixer.music.load("jjkopening.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10) 