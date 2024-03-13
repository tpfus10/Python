import pygame

import setting


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
    # elif event.key == pygame.K_UP:
    #ship_rect.top -= setting.SHIP_SPEED
    # elif event.key == pygame.K_DOWN:
    #ship_rect.top += setting.SHIP_SPEED
    #if ship_rect.top + ship_rect.height <= screen_rect.top:
    #ship_rect.top += setting.SHIP_SPEED
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