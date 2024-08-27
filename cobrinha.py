import pygame, random
from pygame.locals import *

pygame.init()
tela = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Cobrinha")

def margem():
    x = random.randint(0,29)
    y = random.randint(0,29)
    return (x * 10, y * 10)

def colisao(c1,c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

cobra = [(100,100), (100,110), (100,120)]
cobra_corpo = pygame.Surface((10,10))
cobra_corpo.fill((98,240,209))

ponto = pygame.Surface((10,10))
ponto.fill((255,0,0))
ponto_pos = margem()

direcao = LEFT

tempo = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 8)
score = 0

game_over = False
while not game_over:
    tempo.tick(10)
    for move in pygame.event.get():
        if move.type == QUIT:
            pygame.quit()
            exit()

        if move.type == KEYDOWN:
            if move.key == K_UP and direcao != DOWN:
                direcao = UP

            if move.key == K_DOWN and direcao != UP:
                direcao = DOWN

            if move.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT

            if move.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT

    if colisao(cobra[0], ponto_pos):
        ponto_pos = margem()
        cobra.append((0,0))
        score = score + 1

    #cobra bate na parede
    if cobra[0][0] == 300 or cobra[0][1] == 300 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break

    #cobra se bate
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over: break

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    #movimentando
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    tela.fill((0,0,0))
    tela.blit(ponto,ponto_pos)
        
    score_font = font.render('Pontuação: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (300 - 120, 10)
    tela.blit(score_font, score_rect)

    for pos in cobra:
        tela.blit(cobra_corpo,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 18)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (300 / 2, 10)
    tela.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        for move in pygame.event.get():
            if move.type == QUIT:
                pygame.quit()
                exit()

    


