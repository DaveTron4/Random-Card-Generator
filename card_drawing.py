import pygame, random

pygame.init()

pygame.mixer.init()


GRAY = (128, 128, 128)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
WIDTH = 600
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cut!")

def chose_suit():
    suits = ['club', 'heart', 'diamond',  'spade']
    suit = random.choice(suits)
    suit_image = {'club' : 'assets/club.png', 'heart' : 'assets/heart.png', 'diamond' : 'assets/diamond.png', 'spade' : 'assets/spade.png'}
    suit_color = {'club' : BLACK, 'heart' : RED, 'diamond' : RED, 'spade' : BLACK}

    suit_image_item = pygame.image.load(suit_image[suit])
    suit_image_item = pygame.transform.scale(suit_image_item, (100, 100))
    
    suit_rect = suit_image_item.get_rect()
    suit_rect.center = (WIDTH//2 + 100,HEIGHT//2)
    
    font = pygame.font.SysFont(None, 130)

    rank_text = font.render(f"{random.randint(1, 10)}", True, suit_color[suit])
    rank_rect = rank_text.get_rect()
    rank_rect.center = (WIDTH//2 - 100,HEIGHT//2)


    return suit_image_item, suit_color, suit_rect, rank_text, rank_rect


sound = pygame.mixer.Sound("assets/coin_sound.mp3")

FPS = 60
clock = pygame.time.Clock()
pressed_space = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pressed_space = True
                suit_image, suit_color, suit_rect, rank_text, rank_rect = chose_suit()
            if event.key == pygame.K_c:
                pressed_space = False 
                display_surface.fill(GRAY)
                sound.play()
                
                
    display_surface.fill(GRAY)

    if pressed_space:
        display_surface.blit(suit_image, suit_rect)
        display_surface.blit(rank_text, rank_rect)
    

    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
