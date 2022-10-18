
from pickle import NONE
import pygame
import os
import random

WIDTH, HEIGHT = 800, 800
pygame.mixer.init()
# Loading Animation/Art Assets

PLAYER_IMG = [[
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s1.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s2.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s3.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s4.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s5.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_s6.png")), (35,56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l1.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l2.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l3.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l4.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l5.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_l6.png")), (35,56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r1.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r2.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r3.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r4.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r5.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_r6.png")), (35,56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u1.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u2.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u3.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u4.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u5.png")), (35,56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_u6.png")), (35,56)),
]]
SKELLY_IMG = [[
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s1.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s2.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s3.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s4.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s5.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_s6.png")), (25,40)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l1.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l2.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l3.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l4.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l5.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_l6.png")), (25,40)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r1.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r2.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r3.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r4.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r5.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_r6.png")), (25,40)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u1.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u2.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u3.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u4.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u5.png")), (25,40)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "skelly_u6.png")), (25,40)),
]]

NPC_IMG = [[
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s1.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s2.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s3.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s4.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s5.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_s6.png")), (35, 56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l1.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l2.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l3.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l4.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l5.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_l6.png")), (35, 56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r1.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r2.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r3.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r4.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r5.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_r6.png")), (35, 56)),
], [
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u1.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u2.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u3.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u4.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u5.png")), (35, 56)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets", "npc_u6.png")), (35, 56)),
]]

ARROW_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "arrow.png")), (15,24))

STRUCTURE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "structure1.png")), (150,150))

# Sound Files

shoot1_sound = pygame.mixer.Sound(os.path.join("assets", "shoot1.mp3"))
shoot2_sound = pygame.mixer.Sound(os.path.join("assets", "shoot2.mp3"))
shoot3_sound = pygame.mixer.Sound(os.path.join("assets", "shoot3.mp3"))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = PLAYER_IMG
        self.mask = pygame.mask.from_surface(self.img[0][0])
        self.arrows = []
        self.cooldown = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0
        self.hitpoints = 100

    def shoot(self):
        if self.left:
            arrow = Arrows(self.x, self.y, "left")
        elif self.right:
            arrow = Arrows(self.x, self.y, "right")
        elif self.down:    
            arrow = Arrows(self.x, self.y, "down")
        else:
            arrow = Arrows(self.x, self.y, "up")
        self.arrows.append(arrow)
        playsound = random.choice([shoot1_sound, shoot2_sound, shoot3_sound])
        playsound.play()


class Arrows():
    def __init__(self, x, y, direction):
        if direction == "left":
            self.direction = "left"
            self.img = pygame.transform.rotate(ARROW_IMG, 90)
        elif direction ==  "right":
            self.direction = "right"
            self.img = pygame.transform.rotate(ARROW_IMG, 270)
        elif direction == "up":
            self.direction = "up"
            self.img = ARROW_IMG
        else:
            self.direction = "down"
            self.img = pygame.transform.rotate(ARROW_IMG, 180)
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.img)
        self.speed = 500/60

    def off_screen(self):
        return self.y > HEIGHT or self.y < 0 or self.x < 0 or self.x > WIDTH

    def move(self):
        if self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
        elif self.direction == "up":
            self.y -= self.speed
        else:
            self.y += self.speed


class Skeleton():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = SKELLY_IMG
        self.walk_count = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.direction = "down"
        self.speed = 120/60
        self.mask = pygame.mask.from_surface(self.img[0][0])

class Helpful(Skeleton):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = NPC_IMG
        self.arrows = []
        self.cooldown = 0
        self.hitpoints = 100
        self.mask = pygame.mask.from_surface(self.img[0][0])
    
    def shoot(self):
        if self.left:
            arrow = Arrows(self.x, self.y, "left")
        elif self.right:
            arrow = Arrows(self.x, self.y, "right")
        elif self.down:    
            arrow = Arrows(self.x, self.y, "down")
        else:
            arrow = Arrows(self.x, self.y, "up")
        self.arrows.append(arrow)
    
    
class Structure():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = STRUCTURE_IMG
        self.mask = pygame.mask.from_surface(self.img)
