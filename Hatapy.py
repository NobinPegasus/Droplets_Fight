import pygame
import random
import time
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

pygame.mixer.music.load('Mountain.mp3')
pygame.mixer.music.play(-1)

pot = pygame.image.load('pot1.png')


drop = pygame.mixer.Sound('Drop.wav')
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (0,2,0)
BACKGROUND_COLOR = (255,255,255)
black = (255,255,255)

#back = pygame.image.load('backHI.jpg')

player_size = 50
player_pos = [WIDTH/2, HEIGHT-player_size]

enemy_size = 30
"""
hak = random.randint(0,WIDTH-enemy_size)%5
print(hak)
"""
enemy_pos = [random.randint(30,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

back = pygame.image.load('backHI.jpg')

game_over = False

score = 0
dodged = 0
temp = 0
clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
        if score < 20:
                SPEED = 5
        elif score < 40:
                SPEED = 8
        elif score < 60:
                SPEED = 12
        else:
                SPEED = 15
        return SPEED

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
        
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    #time.sleep(2)

def drop_enemies(enemy_list):
        delay = random.random()
        if len(enemy_list) < 10 and delay < 0.1:
                x_pos = random.randint(30,WIDTH-enemy_size)
                y_pos = 0
                if(enem_list
                enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
        for enemy_pos in enemy_list:
                
                        
                   pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def crash():
    #pygame.mixer.music.stop()
    message_display('You Crashed')
    #drop.play()
    #game_over = True
    pygame.mixer.music.stop()

def update_enemy_positions(enemy_list,score):
        for idx, enemy_pos in enumerate(enemy_list):
                if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                        enemy_pos[1] += SPEED
                else:
                        enemy_list.pop(idx)
                        score += 1
        return score

def collision_check(enemy_list, player_pos):
        global dodged
        for enemy_pos in enemy_list:
                if detect_collision(enemy_pos, player_pos):
                        #dodged += 1
                        
                        #drop.play()
                        #return tap 
                        return True
                
        return False


def things_dodged(dodged):

    font = pygame.font.SysFont(None, 25)
    text = font.render("Raindrops: "+str(dodged), True, black)
    screen.blit(text,(0,0))


def detect_collision(player_pos, enemy_pos):
        global dodged
        #global temp
        p_x = player_pos[0]
        p_y = player_pos[1]

        e_x = enemy_pos[0]
        e_y = enemy_pos[1]

        #if (e_x > p_x and e_x < p_x + player_size): #20 >= 552):#and e_x + player_size <= p_x):
               # if(e_y > p_y and e_y + player_size < p_y):
            #if(e_y >= p_y):
        if(e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+player_size)):
                if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+player_size)):
                        #temp = temp + dodged# + 1
                        #print (temp)
                        dodged += 1
                        player_pos[1] = 0
                        #(temp + 20==dodged):
                                #drop.play()        
                        return True
                        #print (dodged)
                        #if(dodged > temp + 1):
                           #     dodged = temp + 1
                        #continue
                        

        return False


start_ticks=pygame.time.get_ticks() #starter tick
 # mainloop
"""seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds>10: # if more than 10 seconds close the game
        break
    print (seconds)
"""



while not game_over:


        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds>50: 
                pygame.mixer.music.stop()
                break
        #print (seconds)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()

                if event.type == pygame.KEYDOWN:

                        x = player_pos[0]
                        y = player_pos[1]

                        if event.key == pygame.K_LEFT:
                                x -= player_size
                        elif event.key == pygame.K_RIGHT:
                                x += player_size

                        player_pos = [x,y]

        screen.blit(back, (0,0))


        if(player_pos[0] > WIDTH - 2 or player_pos[0] < 2):
                        crash()
                        break

        things_dodged(dodged)
        
        drop_enemies(enemy_list)
        score = update_enemy_positions(enemy_list, score)
        SPEED = set_level(score, SPEED)

        #text = "Score:" + str(score)
        #label = myFont.render(text, 1, YELLOW)
        #screen.blit(label, (WIDTH-200, HEIGHT-40))



        if(collision_check(enemy_list, player_pos)):
                #dodged += 1
                
                drop.play()
                #crash()

        draw_enemies(enemy_list)

        screen.blit(pot, (player_pos[0],player_pos[1]))
        #pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

        clock.tick(30)

        pygame.display.update()


import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score = 0

dodgy = dodged//5

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.visible = True
        self.health = 10
        
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 50
        self.y = 410
        self.walkCount = 0
        #font1 = pygame.font.SysFont('comicsans', 100)
        #text = font1.render('-5', 1, (255,0,0))
        #win.blit(text, (250 - (text.get_width()/2),200))
        #pygame.display.update()
        i = 0
        if self.health > 0:
            self.health -= 5
        else:
            self.visible = False
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('You Lost', 1, (255,0,0))
            win.blit(text, (250 - (text.get_width()/2),200))
            pygame.display.update()
            pygame.quit()
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 101
                    pygame.quit()
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('You Won', 1, (255,0,0))
            win.blit(text, (250 - (text.get_width()/2),200))
            pygame.display.update()
            pygame.quit()    
    
        pass

        

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    text1 = font.render('Bullets: ' + str(dodgy), 1, (0,0,0))
    win.blit(text, (350, 10))
    win.blit(text1, (50, 10))
    
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                #score -= 5
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                      
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        dodgy -= 1
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
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
    if(dodgy == 0):
                  
            font5 = pygame.font.SysFont('comicsans', 100)
            text5 = font5.render('You Lost', 1, (255,0,0))
            win.blit(text5, (250 - (text5.get_width()/2),200))
            pygame.display.update()
            pygame.quit()


    redrawGameWindow()

pygame.quit()


