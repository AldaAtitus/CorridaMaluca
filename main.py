import pygame
import random
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
movXcar1 = 0
movXcar2 = 0
posYcar1 = 50
posYcar2 = 180
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) #looping
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    
    tela.fill(branco)
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXcar1,posYcar1))
    tela.blit(carro2, (movXcar2,posYcar2))
    movXcar1 = movXcar1 + random.randint(0,5)
    movXcar2 = movXcar2 + random.randint(0,5)
    

    
    if movXcar1 > 1000:
        movXcar1 = 0
        posYcar1 = 350
    if movXcar2 > 1000:
        movXcar2 = 0
        posYcar2 = 480
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()