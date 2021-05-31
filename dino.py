# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import sys
from pygame_functions import *
import os
import pygame

# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree

pygame.init()
pygame.display.set_caption('Jumping dino')
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nado Pang")
fps = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

dino = pygame.image.load(os.path.join(image_path, "dino1.png"))
character_size = dino.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:

    fps.tick(30)

    # dino

    imgDino1 = pygame.image.load('images/dino1.png')
    imgDino2 = pygame.image.load('images/dino2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = screen_height - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = screen_width
    tree_y = screen_height - tree_height

    while True:

        screen.blit(background, (0, 0))

        screen.blit(stage, (0, screen_height - stage_height))
        screen.blit(dino, (character_x_pos, character_y_pos))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # dino move
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0

        # dino top and bottom check
        if is_go_up and dino_y <= jump_top:
            is_go_up = False

        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = screen_width

        # draw tree
        stage.blit(imgTree, (tree_x, tree_y))

        # # draw dino
        # if leg_swap:
        #     screen.blit(imgDino1, (dino_x, dino_y))
        #     leg_swap = False
        # else:
        #     screen.blit(imgDino2, (dino_x, dino_y))
        #     leg_swap = True

        # update
#        pygame.display.update()

