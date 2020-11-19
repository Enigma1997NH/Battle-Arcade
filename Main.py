#...........................................NAWAJ HUSSAIN.................................................
import pygame
import os
pygame.init()

win = pygame.display.set_mode((800, 400))

pygame.display.set_caption("multiplayer game")

os.chdir("Path...\\char")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

walkRight1 = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
             pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
             pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]

walkLeft1 = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
            pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
            pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]

bg = pygame.image.load('bg.jpg')

char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)
playerscore = 0
player1score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 10
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 5, 29, 52)
        self.health = 10
        self. visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if not (self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 20, self.y + 5, 29, 52)
        

    def hit(self):
        if self.health > 0:
            self.health -=1
        else:
            self.visible = False
        print('player two HIT')

    def hit2(self):
        if self.health < 2:
            self.health += self.health + 5
            print('player2 health is filled')
#x= 700
#y = 340
#width = 64
#height = 64
#vel = 5  # speed of char
#isJump = False
#jumpCount = 10
#left = False
#right = False
#walkCount = 0

class player1(object):
    def __init__(self, x1, y1, width1, height1):
        self.x1 = x1
        self.y1 = y1
        self.width1 = width1
        self.height1 = height1
        self.vel1 = 10
        self.isJump1 = False
        self.jumpCount1 = 10
        self.left1 = False
        self.right1 = False
        self.walkCount1 = 10
        self.standing1 = True
        self.hitbox1 = (self.x1 + 20, self.y1 + 5, 29, 52)
        self.health1 = 10
        self.visible1 = True

    def draw1(self, win):
        if self.visible1:
            if self.walkCount1 + 1 >= 27:
                self.walkCount1 = 0
            if not (self.standing1):
                if self.left1:
                    win.blit(walkLeft1[self.walkCount1 // 3], (self.x1, self.y1))
                    self.walkCount1 += 1
                elif self.right1:
                    win.blit(walkRight1[self.walkCount1 // 3], (self.x1, self.y1))
                    self.walkCount1 += 1
            else:
                
                if self.right1:
                    win.blit(walkRight1[0], (self.x1, self.y1))
                else:
                    win.blit(walkLeft1[0], (self.x1, self.y1))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox1[0], self.hitbox1[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox1[0] , self.hitbox1[1]  - 20, 50 - (5 * (10 - self.health1 )), 10))
            self.hitbox1 = (self.x1 + 20, self.y1 + 5, 29, 52)


    def hit1(self):
        if self.health1 > 0:
            self.health1 -=1
            print("health "+str(self.health1))
        else:
            self.visible1 = False
        print('player no.1 HIT')

        pass
    def hit2(self):
        if self.health1 < 2:
            self.health1 += self.health1 + 5
            print('player1 health is filled')
#x1 = 50
#y1 = 340
#width1 = 64
#height1 = 64
#vel1 = 10
#isJump1 = False
#jumpCount1 = 10
#left1 = False
#right1 = False
#walkCount1 = 0

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class projectile1(object):
    def __init__(self, x1, y1, radius1, color1, facing1):
        self.x1 = x1
        self.y1 = y1
        self.radius1 = radius1
        self.color1 = color1
        self.facing1 = facing1
        self.vel1 = 8 * facing1

    def draw1(self, win):
        pygame.draw.circle(win, self.color1, (int(self.x1), int(self.y1)), self.radius1)

class pro(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        #self.facing = facing
        self.vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = playerfont.render('PLAYER-1: ' + str(playerscore), 1, (255, 255, 255))
    text1 = player1font.render('PLAYER-2: ' + str(player1score), 1, (255, 255, 255))
    win.blit(text,(40, 10))
    win.blit(text1,(600,10))
    man.draw(win)
    man1.draw1(win)
    for bullet in bullets:
        bullet.draw(win)

    for bullet1 in bullets1:
        bullet1.draw1(win)

    for health in healths:
        health.draw(win)

    pygame.display.update()

#mainloop
playerfont = pygame.font.SysFont('comicsans', 30, True, True)
player1font = pygame.font.SysFont('comicsans', 30, True)
man = player(750, 340, 64, 64)
man1 = player1(50, 340, 64, 64)
shootLoop = 0
shootLoop1 = 0
bullets = []
bullets1 = []
healths = []
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for health in healths:
        if health.y - health.radius < man1.hitbox1[1] + man1.hitbox1[3] and health.y + health.radius > man1.hitbox1[1]:
            if health.x + health.radius > man1.hitbox1[0] and health.x - health.radius < man1.hitbox1[0] + man1.hitbox1[2]:
                hitSound.play()
                man1.hit2()
                healths.pop(healths.index(health))
        if health.x < 500 and health.x > 0:
            health.x += health.vel
        else:
            healths.pop(healths.index(health))

    if man1.visible1:
        for bullet in bullets:
            if bullet.y - bullet.radius < man1.hitbox1[1] + man1.hitbox1[3] and bullet.y + bullet.radius > man1.hitbox1[1] :
                 if bullet.x + bullet.radius > man1.hitbox1[0]  and bullet.x - bullet.radius < man1.hitbox1[0] + man1.hitbox1[2]:
                        hitSound.play(1)
                        man1.hit1()
                        player1score += 10
                        bullets.pop(bullets.index(bullet))
            if bullet.x < 800 and bullet.x > 0:
                    bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    if not man1.visible1:
        man1 = player1(-100, -100, 64, 64)





    keys = pygame.key.get_pressed()
    keys1 = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(healths) < 5:
            healths.append(pro(round(400), round(200), 20, (255, 0, 0)))
    if keys[pygame.K_DOWN] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), 6, (0, 0, 100), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump =  True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    for health in healths:
        if health.y - health.radius < man.hitbox[1] + man.hitbox[3] and health.y + health.radius > man.hitbox[1]:
            if health.x + health.radius > man.hitbox[0] and health.x - health.radius < man.hitbox[0] + man.hitbox[2]:
                man.hit2()
                healths.pop(healths.index(health))
        if health.x < 500 and health.x > 0:
            health.x += health.vel
        else:
            healths.pop(healths.index(health))

    if man.visible:
        for bullet1 in bullets1:
            if bullet1.y1 - bullet1.radius1 < man.hitbox[1] + man.hitbox[3] and bullet1.y1 + bullet1.radius1 > man.hitbox[1]:
                if bullet1.x1 + bullet1.radius1 > man.hitbox[0] and bullet1.x1 - bullet1.radius1 < man.hitbox[0] + man.hitbox[2]:
                    hitSound.play()
                    man.hit()
                    playerscore += 10
                    bullets1.pop(bullets1.index(bullet1))

            if bullet1.x1 < 800 and bullet1.x1 > 0:
                bullet1.x1 += bullet1.vel1
            else:
                bullets1.pop(bullets1.index(bullet1))
    if not man.visible:
        man = player(-750, -340, 64, 64)

    if keys1[pygame.K_s] and shootLoop == 0:
        bulletSound.play()
        if man1.left1:
            facing1 = -1
        else:
            facing1 = 1
        if len(bullets1) < 10:
            bullets1.append(projectile1(round(man1.x1 + man1.width1 //2), (man1.y1 + man1.height1 //2), 6, (255, 100, 180), facing1))
        shootLoop = 1
    if keys1[pygame.K_a] and man1.x1 > man1.vel1:
        man1.x1 -= man1.vel1
        man1.left1 = True
        man1.right1 = False
        man1.standing1 = False
    elif keys1[pygame.K_d] and man1.x1 < 800 - man1.width1 - man1.vel1:
        man1.x1 += man1.vel1
        man1.right1 = True
        man1.left1 = False
        man1.standing1 = False
    else:
        man1.standing1 = True
        man1.walkCount1 = 0
    if not (man1.isJump1):
        if keys1[pygame.K_w]:
            man1.isJump1 = True
            man1.left1 = False
            man1.right1 = False
            man1.walkCount1 = 0
    else:
        if man1.jumpCount1 >= -10:
            neg1 = 1
            if man1.jumpCount1 < 0:
                neg1 = -1
            man1.y1 -= (man1.jumpCount1 ** 2) * 0.5 * neg1
            man1.jumpCount1 -= 1
        else:
            man1.isJump1 = False
            man1.jumpCount1 = 10


    redrawGameWindow()

pygame.quit()
