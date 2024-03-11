import sys

import pygame

import setting

pygame.init() #초기화

from util import init
screen, clock, image, screen_rect, ship_rect = init()

from util import render
# Render the graphics here. # 3)Render(그래픽)
render(screen, image, ship_rect, bullet_color, new_bullets)#렌더(rect)



#image_rect = pygame.Rect(500, 500, 100, 100) 
#image_rect = screen.get_rect()  =  pygame.Rect(0, 0, 1280, 720) 

# image_rect.left = 1280/2
# image_rect.top = 600


#bullet 함수(만들고 위치조정)
def create_bullet(ship_rect):
    bullet = pygame.Rect(0, 0, 5, 50)
    bullet.midtop = ship_rect.midtop 
    bullet.top -= ship_rect.height
    return bullet

#bullet list
bullets = []
# bullet = create_bullet(ship_rect)
bullets.append(create_bullet(ship_rect))
bullet_color = setting.BULLET_COLOR 

while True:
    # Process player inputs.(게임의 실행과 종료)
    for event in pygame.event.get(): # 1)키보드/마우스의 이벤트
        if event.type == pygame.QUIT:
            pygame.quit()
            # raise SystemExit
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_rect.left -= setting.SHIP_SPEED
            elif event.key == pygame.K_RIGHT:
                ship_rect.left += setting.SHIP_SPEED
            # elif event.key == pygame.K_UP:
            #     ship_rect.top -= setting.SHIP_SPEED
            # elif event.key == pygame.K_DOWN:
            #     ship_rect.top += setting.SHIP_SPEED
                if ship_rect.top + ship_rect.height <= screen_rect.top:
                    ship_rect.top += setting.SHIP_SPEED
            elif event.key == pygame.K_SPACE:
                b = create_bullet(ship_rect) #리스트 만들기
                bullets.append(b) # append로 집어넣기
    
        


    # Do logical updates here. # 2)이벤트에 따른 변화를 업데이트
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -=1 #쏘면 앞으로 나가도록 하기
            new_bullets.append(bullet)
 

    screen.fill("grey")  # Fill the display with a solid color

 

    pygame.display.flip()  # Refresh on-screen display 4) 화면1에서 화면2로 포인터를 이동(화면 전환)
    clock.tick(setting.FRAME_PER_SECOND)         # wait until next frame (at 60 FPS) 5) 4번을 60번 바꾸는 걸 반복하게 함
    