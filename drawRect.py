import pygame
from pygame.color import THECOLORS

# initialize pygame
pygame.init()

# create a pygame screen
screen = pygame.display.set_mode([600, 400])

# 将蓝色铺满整个窗口
# screen.fill(THECOLORS['blue'])

# 添加白色与红色区域
# pygame.draw.rect(screen, THECOLORS['white'],[0,150,600,100],0)
# pygame.draw.rect(screen, THECOLORS['white'],[150,0,100,400],0)
# pygame.draw.rect(screen, THECOLORS['red'],[0,170,600,60],0)
# pygame.draw.rect(screen, THECOLORS['red'],[170,0,60,400],0)
screen.fill(THECOLORS['red'])
pygame.draw.rect(screen, THECOLORS['blue'], [0, 100, 600, 200], 0)
pygame.draw.circle(screen, THECOLORS['white'], [300, 200], 90, 0)

# 翻转
pygame.display.flip()

# LOOP: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            pygame.quit()
