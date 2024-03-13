import sys
import pygame
import setting

from util import init, create_bullet, handle_key_event, update_bullets, render

screen, clock, image, screen_rect, ship_rect, bullets, ship_rect.midbottom = init()

#image_rect = pygame.Rect(500, 500, 100, 100) 
#image_rect = screen.get_rect()  =  pygame.Rect(0, 0, 1280, 720) 
#image_rect.left = 1280/2
#image_rect.top = 6005

# Do logical updates here. # 2)이벤트에 따른 변화를 업데이트
new_bullets = update_bullets(screen_rect, bullets)
screen.fill("grey")  # Fill the display with a solid color

# Render the graphics here.
render(screen, image, ship_rect, new_bullets)

pygame.display.flip()  # Refresh on-screen display 4) 화면1에서 화면2로 포인터를 이동(화면 전환)
clock.tick(setting.FRAME_PER_SECOND)  # wait until next frame (at 60 FPS) 5) 4번을 60번 바꾸는 걸 반복하게 함

while True:
    # Process player inputs.(게임의 실행과 종료)
    for event in pygame.event.get(): # 1)키보드/마우스의 이벤트
        if event.type == pygame.QUIT:
            pygame.quit()
            # raise SystemExit
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_key_event(screen_rect, bullets, event)
  