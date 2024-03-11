def init():
    screen = pygame.display.set_mode((setting.HEIGHT,setting.WIDTH))
    clock = pygame.time.Clock()
    image = pygame.image.load(setting.SPACE_IMAGE) #이미지 로드

    screen_rect = screen.get_rect()
#pygame.Rect 객체를 이용해 위치 조정(get_rect 호출로 Rect 객체 생성)
    ship_rect = image.get_rect() 
#이미지의 위치를 화면 하단 중앙으로 설정
    ship_rect.midbottom = screen.get_rect().midbottom
    bullet = []
    return screen,clock,image,screen_rect,ship_rect


def render(screen, image, ship_rect, bullet_color, new_bullets):
    screen.blit(image, ship_rect) #렌더(이미지)
    for bullet in new_bullets:
        pygame.draw.rect(screen, bullet_color, bullet)