import pygame
import random
import sys

c = 0
pygame.init()

# 視窗設定
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("小恐龍遊戲")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 小恐龍
dino = pygame.Rect(80, 300, 50, 50)
dino_y_velocity = 0
gravity = 1


# 跳躍蓄力系統
is_jumping = False
jump_time = 0
max_jump_time = 30  # 按越久可跳越高（可調高低）

# 障礙物
obstacles = []
spawn_timer = 0

score = 0


def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, dino)  # 小恐龍

    for obs in obstacles:
        pygame.draw.rect(screen, (200, 0, 0), obs)

    score_text = font.render(f"分數: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()


while True:
    draw()
    clock.tick(60)
    c = +1
    if c < 160:
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # 開始跳躍
    if keys[pygame.K_UP] and dino.bottom >= 350 and not is_jumping:
        is_jumping = True
        jump_time = 0

    # 長按 → 跳越高
    if is_jumping and keys[pygame.K_UP]:
        if jump_time < max_jump_time:
            dino_y_velocity = -15  # 每幀往上推一次（跳的力量，可調）
            jump_time += 1

    # 放開鍵 → 結束跳躍
    if not keys[pygame.K_UP]:
        is_jumping = False

    # 重力
    dino_y_velocity += gravity
    dino.y += dino_y_velocity

    if dino.bottom > 350:
        dino.bottom = 350
        dino_y_velocity = 0

    # 生成障礙物
    spawn_timer += 1
    if spawn_timer > 50:
        spawn_timer = 0
        obstacle = pygame.Rect(WIDTH, 320, 40, 40)
        obstacles.append(obstacle)

    # 移動障礙物
    for obs in obstacles[:]:
        obs.x -= 10
        if obs.x < -50:
            obstacles.remove(obs)
            score += 1

        # 碰撞判定
        if dino.colliderect(obs):
            print("遊戲結束! 分數:", score)
            pygame.quit()
            sys.exit()
