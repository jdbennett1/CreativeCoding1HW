import pygame
import sys
import random
import asyncio
from spritesheet import Spritesheet


#set up variables. 
WIDTH, HEIGHT = 800, 600
LEVEL_WIDTH = 2000
MOVE_SPEED = 5

# I had ChatGPT help me with some of the physics for jumping. These are constants used for the jumps
JUMP_STRENGTH = -15
GRAVITY = 0.8
MAX_JUMPS = 2

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
GOLD = (255, 215, 0)
GRAY = (100, 100, 100)
BG = (50, 50, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# these are sprite chains that the game loop runs through. These create an animation when iterated through. 
# my inital idea was to use 1 sprite sheet and jsut iterativly repostion the frame and add to the corrisponding
# list but the sprite sheet I chose to use made tha difficult. The sprite sheet sprites are not all the same dimensions 
# and not evenly spaced. This led me to manually finding the dimensions and location of each sprite. I made my life easier 
# by spliting the sprite sheet into multiple sheets.  
idle_sheet = Spritesheet('idle.PNG')
idle = [
    idle_sheet.get_sprite(0,0,40,75),
    idle_sheet.get_sprite(40,0,40,75),
    idle_sheet.get_sprite(75,0,40,75),
    idle_sheet.get_sprite(115,0,40,75),
    idle_sheet.get_sprite(150,0,40,75),
    idle_sheet.get_sprite(189,0,40,75),
]

my_running_sheet = Spritesheet('running.PNG')
run = [
    my_running_sheet.get_sprite(-5,0,55,75),
    my_running_sheet.get_sprite(50,0,55,75),
    my_running_sheet.get_sprite(100,0,55,75),
    my_running_sheet.get_sprite(150,0,55,75),
    my_running_sheet.get_sprite(200,0,55,75),
    my_running_sheet.get_sprite(260,0,55,75),
    my_running_sheet.get_sprite(315,5,55,75),
    my_running_sheet.get_sprite(370,5,55,75),
    my_running_sheet.get_sprite(425,0,55,75),
    my_running_sheet.get_sprite(480,0,55,75),
]

my_spritesheet = Spritesheet('punch.png')
spider = [
    my_spritesheet.get_sprite(0, 0, 55, 75),
    my_spritesheet.get_sprite(55, 0, 55, 75),
    my_spritesheet.get_sprite(120, 0, 55, 75),
    my_spritesheet.get_sprite(190, 0, 55, 75),
    my_spritesheet.get_sprite(250, 0, 75, 75)  # punch
]

jump_sheet = Spritesheet('jump.png')
jump = [
    jump_sheet.get_sprite(0,10,54,75),
    jump_sheet.get_sprite(46,10,55,75),
    jump_sheet.get_sprite(98,0,55,75),
    jump_sheet.get_sprite(213,5,65,85),
    jump_sheet.get_sprite(275,5,65,115)
]

def animations():
    return {
        "idle": idle,
        "run": run,
        "punch": spider,
        "jump" : jump
    }

# this is a platform class called later to create multiple platforms that can be jumped on. 
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h=20):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect(topleft=(x, y))

# this is a class that draws a gold circle imitating a coin that can be collected. 
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GOLD, (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))


# This is the player. All of the sprite movement, positioning, eventhandling relating
# to the player are stored here. 
class Player(pygame.sprite.Sprite):
    def __init__(self, platforms, animations):
        super().__init__()
        self.animations = animations
        self.current_animation = "idle"
        self.frame_index = 0
        self.image = self.animations[self.current_animation][self.frame_index]
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 100))

        # this is one of the steps ChatGPT helped me employ physics for jumping to platforms 
        self.pos = pygame.Vector2(self.rect.topleft)
        self.vel = pygame.Vector2(0, 0)
        self.jump_count = 0
        self.platforms = platforms
        self.frame_timer = 0

    def update(self, keys):
        self.vel.x = 0
        if keys[pygame.K_LEFT]:
            self.vel.x = -MOVE_SPEED
            self.current_animation = "run"
        elif keys[pygame.K_RIGHT]:
            self.vel.x = MOVE_SPEED
            self.current_animation = "run"
        else:
            self.current_animation = "idle"

        if keys[pygame.K_SPACE] and self.jump_count < MAX_JUMPS:
            self.vel.y = JUMP_STRENGTH
            self.jump_count += 1
            self.current_animation = "jump"

        # this is one of the steps ChatGPT helped me employ physics for jumping to platforms 
        self.vel.y += GRAVITY
        self.pos.x += self.vel.x
        self.rect.x = int(self.pos.x)
        self.pos.x = max(0, min(self.pos.x, LEVEL_WIDTH - self.rect.width))

        self.pos.y += self.vel.y
        self.rect.y = int(self.pos.y)

        # loop to check if character is colliding with platform 
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel.y > 0 and self.rect.bottom <= platform.rect.bottom:
                    self.rect.bottom = platform.rect.top
                    self.pos.y = self.rect.y
                    self.vel.y = 0
                    self.jump_count = 0

        self.animate()

    def animate(self):
        self.frame_timer += 1
        if self.frame_timer >= 10:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.frame_index]

animations = animations()

async def main():
    

    # this again relates to the physics of the platforms. pygame.sprite.Group() is function that can 
    # group sprites and draw them all at once. I then used it to draw all of the coins
    platforms = pygame.sprite.Group()
    platform_list = [
        Platform(0, HEIGHT - 40, LEVEL_WIDTH),
        Platform(200, 450, 200),
        Platform(600, 350, 150),
        Platform(950, 250, 200),
        Platform(1400, 200, 200),
    ]
    platforms.add(platform_list)

    coins = pygame.sprite.Group()
    for _ in range(10):
        x = random.randint(100, LEVEL_WIDTH - 100)
        y = random.choice([430, 330, 230, 180])
        coins.add(Coin(x, y))

    player = Player(platform_list, animations)
    all_sprites = pygame.sprite.Group(player, *platform_list, *coins)

    # Game state
    score = 0
    game_over = False

    # Game loop
    while True:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            player.update(keys)

            cam_x = max(0, min(player.rect.centerx - WIDTH // 2, LEVEL_WIDTH - WIDTH))

            collected = pygame.sprite.spritecollide(player, coins, dokill=True)
            score += len(collected)

        screen.fill(BG)

        for sprite in all_sprites:
            offset = sprite.rect.move(-cam_x, 0)
            screen.blit(sprite.image, offset)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())