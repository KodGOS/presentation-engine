import pygame   #importing pygame
from pygame import *
pygame.init()

window_width = 0    #variables
window_height = 0
current_slide = 1
slides_filenames_list = list()

slide_filename = "0"    #settings variables
settings = open("settings.txt", "r")
window_width = int(settings.readline())
window_height = int(settings.readline())
amount_of_slides = int(settings.readline())

okno = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)   #window settings
pygame.display.set_caption('Presentation engine')

for i in range(amount_of_slides): #importing slides pictures
    slide_filename = f"slides/{i+1}.png"   #i wasted 30 minutes on this line of code
    slides_filenames_list.append(slide_filename)


clock = time.Clock()
game = True

while game:    #the loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_slide += 1
                if current_slide > amount_of_slides:
                    game = False
                    current_slide = amount_of_slides
            if event.key == pygame.K_LEFT:
                current_slide -= 1
                if current_slide < 1:
                    current_slide = 1
    current_slide_image = pygame.image.load(slides_filenames_list[current_slide - 1])
    current_slide_image = pygame.transform.scale(current_slide_image, (window_width, window_height))
    okno.fill((0,0,0))
    okno.blit(current_slide_image, [0, 0])
    display.update()
    clock.tick(60)
