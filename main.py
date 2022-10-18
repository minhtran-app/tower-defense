
import pygame
import os
from objects import *
import random

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("assets", "09 - Xenomorph (Switch-Bored).mp3"))
pygame.mixer.music.set_volume(.3)
pygame.mixer.music.play(-1)

# Fonts
title_font = pygame.font.SysFont("arial", 50)
ui_font = pygame.font.SysFont("arial", 20)

def main_menu():
    run = True
    while run:
        pygame.draw.rect(WIN, (109, 170, 44), ((0, 0), (WIDTH, HEIGHT)))
        title_label = title_font.render("TOWER DEFENSE", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT/3))
        sub_title_label = title_font.render("Push Enter to start...", 1, (255, 255, 255))
        WIN.blit(sub_title_label, (WIDTH/2 - sub_title_label.get_width()/2, HEIGHT/1.2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = True
                        main()

# Determining Collision
def collide(targ1, targ2):
    offset_x = targ2.x - targ1.x
    offset_y = targ2.y - targ1.y
    return targ1.mask.overlap(targ2.mask, (offset_x, offset_y)) != None

def predictive_collide(targ1, targ2, new_x, new_y): # Altering function to allow predicting collides
    offset_x = targ2.x - new_x
    offset_y = targ2.y - new_y
    return targ1.mask.overlap(targ2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    # Set Object Movement Speeds
    player_speed = 300/FPS
    
    active_enemies = []
    active_helpful = []
    active_structures = []
    player = Player(100, 700)
    test_structure = Structure(random.randint(0,270),random.randint(400,500))
    active_structures.append(test_structure)
    test_structure1 = Structure(random.randint(270,540),random.randint(400,500))
    active_structures.append(test_structure1)
    test_structure2 = Structure((WIDTH - test_structure1.img.get_width()),random.randint(400,500))
    active_structures.append(test_structure2)

    wave = 0
    wave_amount = 5
    player_score = 0


    def redraw_window():
        nonlocal player

        # Background
        pygame.draw.rect(WIN, (109, 170, 44), ((0, 0), (WIDTH, HEIGHT)))
       
        # Non-Moving Structures
        for structure in active_structures:
            WIN.blit(structure.img, (structure.x, structure.y))

        # Projectiles and Arrows
        for helpful in active_helpful:
            for arrow in helpful.arrows:
                WIN.blit(arrow.img, (arrow.x, arrow.y))
             
        for arrow in player.arrows:
            WIN.blit(arrow.img, (arrow.x, arrow.y))
            
        # Friendly NPC Animations
        for helpful in active_helpful:
            if helpful.walk_count + 1 >= 60:
                helpful.walk_count = 0
            
            if helpful.left:
                WIN.blit(helpful.img[1][helpful.walk_count//10], (helpful.x, helpful.y))
                helpful.walk_count += 1
            elif helpful.right:
                WIN.blit(helpful.img[2][helpful.walk_count//10], (helpful.x, helpful.y))
                helpful.walk_count += 1
            elif helpful.up:
                WIN.blit(helpful.img[3][helpful.walk_count//10], (helpful.x, helpful.y))
                helpful.walk_count += 1
            else:
                WIN.blit(helpful.img[0][helpful.walk_count//10], (helpful.x, helpful.y))
                helpful.walk_count += 1

        # Enemy Animations
        for enemy in active_enemies:
            if enemy.walk_count + 1 >= 60:
                enemy.walk_count = 0
            
            if enemy.left:
                WIN.blit(enemy.img[1][enemy.walk_count//10], (enemy.x, enemy.y))
                enemy.walk_count += 1
            elif enemy.right:
                WIN.blit(enemy.img[2][enemy.walk_count//10], (enemy.x, enemy.y))
                enemy.walk_count += 1
            elif enemy.up:
                WIN.blit(enemy.img[3][enemy.walk_count//10], (enemy.x, enemy.y))
                enemy.walk_count += 1
            else:
                WIN.blit(enemy.img[0][enemy.walk_count//10], (enemy.x, enemy.y))
                enemy.walk_count += 1

         # Player animation
        if player.walk_count + 1 >= 60:
            player.walk_count = 0
        if player.left:
            WIN.blit(player.img[1][player.walk_count//10], (player.x, player.y))
            player.walk_count += 1
        elif player.right:
            WIN.blit(player.img[2][player.walk_count//10], (player.x, player.y))
            player.walk_count += 1
        elif player.up:
            WIN.blit(player.img[3][player.walk_count//10], (player.x, player.y))
            player.walk_count += 1
        else:
            WIN.blit(player.img[0][player.walk_count//10], (player.x, player.y))
            player.walk_count += 1
         
        # UI Display
        player_health_label = ui_font.render(f"Health: {player.hitpoints}", 1, (255,255,255))
        WIN.blit(player_health_label, (10, 10))
        score_label = ui_font.render(f"Score: {player_score}", 1, (255, 255, 255))
        WIN.blit(score_label, (10, 40))
        wave_label = ui_font.render(f"Wave: {wave}", 1, (255, 255, 255))
        WIN.blit(wave_label, (10, 70))
        pygame.display.update()
    
    def spawn_skellies(wave_amount):
        for i in range(wave_amount):
            skelly = Skeleton(random.randint(50, WIDTH-50), random.randint(0, 100))
            active_enemies.append(skelly)
    
    def spawn_npc(level_amount):
        for i in range(level_amount):
            npc = Helpful(random.randint(100, WIDTH-50), random.randint(650, 700))
            active_helpful.append(npc)
    
    # Handling AI movement

    def npc_movement(enemy):  
        random_choice = random.randint(1, 80)
        if random_choice == 1:
            enemy.direction = random.choice(["down", "up", "left", "right"])
        else:
            if enemy.direction == "down":
                blocked = False
                for structure in active_structures:
                    if predictive_collide(enemy, structure, enemy.x, enemy.y + enemy.speed):
                        blocked = True
                if blocked:
                    enemy.direction = random.choice(["left", "right", "up", "down"])
                else:
                    if enemy.y + enemy.speed + enemy.img[0][0].get_height() < HEIGHT:
                        enemy.y += enemy.speed
                        enemy.left = False
                        enemy.right = False
                        enemy.up = False
                        enemy.down = True
                    else:
                        enemy.direction = random.choice(["left", "right", "up", "down"])
            elif enemy.direction == "left":
                blocked = False
                for structure in active_structures:
                    if predictive_collide(enemy, structure, enemy.x - enemy.speed, enemy.y):
                        blocked = True
                if blocked:
                    enemy.direction = random.choice(["left", "right", "up", "down"])
                else:
                    if enemy.x - enemy.speed > 0:
                        enemy.x -= enemy.speed
                        enemy.left = True
                        enemy.right = False
                        enemy.up = False
                        enemy.down = False
                    else:
                        enemy.direction = random.choice(["left", "right", "up", "down"])
            elif enemy.direction == "right":
                blocked = False
                for structure in active_structures:
                    if predictive_collide(enemy, structure, enemy.x + enemy.speed, enemy.y):
                        blocked = True
                if blocked:
                    enemy.direction = random.choice(["left", "right", "up", "down"])
                else:
                    if enemy.x + enemy.speed + enemy.img[0][0].get_width() < WIDTH:
                        enemy.x += enemy.speed
                        enemy.left = False
                        enemy.right = True
                        enemy.up = False
                        enemy.down = False
                    else:
                        enemy.direction = random.choice(["left", "right", "up", "down"])
            elif enemy.direction == "up":
                blocked = False
                for structure in active_structures:
                    if predictive_collide(enemy, structure, enemy.x, enemy.y - enemy.speed):
                        blocked = True
                if blocked:
                    enemy.direction = random.choice(["left", "right", "up", "down"])
                else:
                    if enemy.y - enemy.speed > 0:
                        enemy.y -= enemy.speed
                        enemy.left = False
                        enemy.right = False
                        enemy.up = True
                        enemy.down = False
                    else:
                        enemy.direction = random.choice(["left", "right", "up", "down"])

    def npc_shoot(helpful):
        roll = random.randint(1, 120)
        if roll == 1:
            if helpful.cooldown >= 60:
                helpful.shoot()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        if player.hitpoints <= 0:
            run = False
            break

        # Checking if enemies are dead / spawning new wave
        if len(active_enemies) == 0:
            wave += 1
            wave_amount *= 2
            spawn_skellies(wave_amount)
            spawn_npc(wave)

        # Controlling Friendlies
        for helpful in active_helpful:
            if helpful.hitpoints <= 0:
                active_helpful.remove(helpful)
            npc_movement(helpful)

        # Controlling Mob Movement and Collision
        for enemy in active_enemies:
            npc_movement(enemy)
            if collide(enemy, player):
                active_enemies.remove(enemy)
                player.hitpoints -= 10
            for helpful in active_helpful:
                if collide(enemy, helpful):
                    try:
                        active_enemies.remove(enemy)
                        player_score += 1
                        helpful.hitpoints -= 10
                    except:
                        print("Arrow error")
        
        # Controlling Arrow/Projectile Movement
        player.cooldown += 1
        if player.cooldown > 70:
            player.cooldown = 60
        for helpful in active_helpful:
            npc_shoot(helpful)
            helpful.cooldown += 1
            if helpful.cooldown > 70:
                helpful.cooldown = 60
            for arrow in helpful.arrows:
                for structure in active_structures:
                    if collide(arrow, structure):
                        helpful.arrows.remove(arrow)
                if arrow.off_screen():
                    helpful.arrows.remove(arrow)
                else:
                    for enemy in active_enemies:
                        if collide(arrow, enemy):
                            active_enemies.remove(enemy)
                            try:
                                helpful.arrows.remove(arrow)
                                player_score += 1
                            except:
                                print("Arrow error)")
                arrow.move()
        for arrow in player.arrows:
            for structure in active_structures:
                if collide(arrow, structure):
                    player.arrows.remove(arrow)
            if arrow.off_screen():
                player.arrows.remove(arrow)
            else:
                for enemy in active_enemies:
                    if collide(arrow, enemy):
                        active_enemies.remove(enemy)
                        try:
                            player.arrows.remove(arrow)
                            player_score += 1
                        except:
                            print("Arrow error)")
                arrow.move()

       

        # Allowing Quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.cooldown >= 60:
                    player.shoot()
                    player.coodown = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.cooldown >= 60:
                        player.shoot()
                        player.coodown = 0
                if event.key == pygame.K_p:
                    active_enemies = []

        # Getting a Dictionary of the state of all keys (True if pressed down, False if not). Continour movement rather than single steps.
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] and player.x - player_speed > 0:
            player_blocked = False
            for structure in active_structures:
                if predictive_collide(player, structure, player.x - player_speed, player.y):
                    player_blocked = True
            if player_blocked:
                pass
            else:
                player.x -= player_speed
                player.left = True
                player.right = False
                player.up = False
                player.down = False
        elif keys[pygame.K_d] and player.x + player_speed + player.img[0][0].get_width() < WIDTH:
            player_blocked = False
            for structure in active_structures:
                if predictive_collide(player, structure, player.x + player_speed, player.y):
                    player_blocked = True
            if player_blocked:
                pass
            else:
                player.x += player_speed
                player.left = False
                player.right = True
                player.up = False
                player.down = False
        else:
            player.left = False
            player.right = False
            player.up = False
            player.down = False
      
        if keys[pygame.K_w] and player.y - player_speed > 0:
            player_blocked = False
            for structure in active_structures:
                if predictive_collide(player, structure, player.x, player.y - player_speed):
                    player_blocked = True
            if player_blocked:
                pass
            else:
                player.y -= player_speed
                player.left = False
                player.right = False
                player.up = True
                player.down = False
        elif keys[pygame.K_s] and player.y + player_speed + player.img[0][0].get_height() < HEIGHT:
            player_blocked = False
            for structure in active_structures:
                if predictive_collide(player, structure, player.x, player.y + player_speed):
                    player_blocked = True
            if player_blocked:
                pass
            else:
                player.y += player_speed
                player.left = False
                player.right = False
                player.up = False
                player.down = True


main_menu()