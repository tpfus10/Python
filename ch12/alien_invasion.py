import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./ch12/ship.bmp') #로드
rect = image.get_rect()

while True:
    # Process player inputs.(게임의 실행과 종료)
    for event in pygame.event.get(): # 1)키보드/마우스의 이벤트
        if event.type == pygame.QUIT:
            pygame.quit()
            # raise SystemExit
            sys.exit()

    # Do logical updates here. # 2)이벤트에 따른 변화를 업데이트
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here. # 3)Render(그래픽)
    screen.blit(image, rect) #렌더
    

    pygame.display.flip()  # Refresh on-screen display 4) 화면1에서 화면2로 포인터를 이동(화면 전환)
    clock.tick(60)         # wait until next frame (at 60 FPS) 5) 4번을 60번 바꾸는 걸 반복하게 함
    