import pygame
import sys
import setting

FRAME_PER_SECOND = 60
HEIGHT = 720
WIDTH= 1280
BULLET_COLOR = (255, 0, 0)
SPACE_IMAGE = './ch12/ship.bmp'
SHIP_SPEED = 5

def init():
    pygame.init() #초기화
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
    clock = pygame.time.Clock()
    image = pygame.image.load(setting.SPACE_IMAGE) #이미지 로드\
    screen_rect = screen.get_rect()
#pygame.Rect 객체를 이용해 위치 조정(get_rect 호출로 Rect 객체 생성)
    ship_rect = image.get_rect() 
#이미지의 위치를 화면 하단 중앙으로 설정
    ship_rect.midbottom = screen.get_rect().midbottom
    bullets = []
    return screen, clock, image, screen_rect, ship_rect, bullets, ship_rect.midbottom

def create_bullet(ship_rect):
    bullet = pygame.Rect(0, 0, 5, 50)
    bullet.midtop = ship_rect.midtop 
    bullet.top -= ship_rect.height
    return bullet

def render(screen, image, ship_rect, new_bullets):
    screen.blit(image, ship_rect) #렌더(이미지)
    for bullet in new_bullets:
        pygame.draw.rect(screen, setting.BULLET_COLOR, bullet)

def handle_key_event(ship_rect, bullets, event):
    if event.key == pygame.K_LEFT:
        ship_rect.left -= setting.SHIP_SPEED
    elif event.key == pygame.K_RIGHT:
        ship_rect.left += setting.SHIP_SPEED
    elif event.key == pygame.K_UP:
        ship_rect.top -= setting.SHIP_SPEED
    elif event.key == pygame.K_DOWN:
        ship_rect.top += setting.SHIP_SPEED
    if ship_rect.top + ship_rect.height <= screen_rect.top:
        ship_rect.top += setting.SHIP_SPEED
    elif event.key == pygame.K_SPACE:
        b = create_bullet(ship_rect) #리스트 만들기
        bullets.append(b) # append로 집어넣기

def update_bullets(screen_rect, bullets):
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -=1 #쏘면 앞으로 나가도록 하기
            new_bullets.append(bullet)
    return new_bullets

screen, clock, image, screen_rect, ship_rect, bullets, ship_rect.midbottom = init()

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
  