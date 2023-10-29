import pygame,sys
from pygame.locals import *
import random

# game screen 
width=1400
height=700

class Snake:
    def __init__(self):
        self.body=[
            (680,360),
            (700,360),
            (720,360)
        ]
        self.direction="left"

    # draws snake body with 2 color pattern
    def draw_body(self):
        color_pattern=[self.brown,self.green]
        for i,block in enumerate(self.body):
            pygame.draw.rect(self.screen,color_pattern[i%2],(block[0],block[1],20,20))
    
    # changes coordinate of snakes body according to key pressed
    def movement(self,food_pos):
        x,y=self.body[0]
        if self.direction=="right":
            first_block=(x+20,y)
        if self.direction=="left":
            first_block=(x-20,y)
        if self.direction=="up":
            first_block=(x,y-20)
        if self.direction=="down":
            first_block=(x,y+20)
        self.body.insert(0,first_block)

        # if food is eaten it Snake length increases
        if not (self.food_collision(food_pos)):
            self.body.pop()

    # checks if snake colided with its own body
    def self_collision(self):
        return self.body[0] in self.body[1:]
    
    # checks if snake ate food
    def food_collision(self,food_position):
        if self.body[0]==food_position:
            return True
        
    # checks if snake colided with wall
    def wall_collision(self):
        first_block=self.body[0]
        if first_block[0]<0 or first_block[0]>1400:
            return True
        if first_block[1]<0 or first_block[1]>700:
            return True
        

class Game(Snake):
    screen=pygame.display.set_mode((width,height))

    def __init__(self):
        super().__init__()
        # colors used in game
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.brown=(196, 164, 132)
        self.cyan=(0,139,139)
        self.green=(53, 94, 59)
        self.rect=Rect(0,0,100,100)
        self.color=(255,255,255)

        self.score=0
        self.speed=10

        self.food_position=(780,380)

        self.end=False

    # shows score
    def show_score(self):
        font=pygame.font.Font('04B_19.ttf', 32)
        self.score_render = font.render(f"Score: {self.score}",True,(255,255,255))
        self.screen.blit(self.score_render,(10,10))
    # shows screen when game is over
    def game_over_screen(self):
        font=pygame.font.Font('04B_19.ttf', 32)
        self.text_render = font.render(f"Score: {self.score}",True,(255,255,255))
        self.screen.blit(self.text_render,(600,300))
        self.text_render = font.render("Game over",True,(255,255,255))
        self.screen.blit(self.text_render,(600,350))
        pygame.display.update()
        pygame.time.wait(1000)  

    # sets direction according to key pressed
    def set_direction(self,key):
        if key[pygame.K_RIGHT] and self.direction!="left":
            self.direction="right"
        if key[pygame.K_LEFT] and self.direction!="right":
            self.direction="left"
        if key[pygame.K_UP] and self.direction!="down":
            self.direction="up"
        if key[pygame.K_DOWN] and self.direction!="up":
            self.direction="down"
    # ends game
    def end_game(self):
        self.game_over_screen()
        pygame.quit()
        exit()
    # calculate new position for food 
    def new_food_position(self):
        x=(random.randint(40,width-40))
        x=round(x/20)*20
        y=(random.randint(80,height-40))
        y=round(y/20)*20
        self.food_position=(x,y)
    # draws food on screen
    def draw_food(self):
        pygame.draw.rect(self.screen,self.cyan,(self.food_position[0],self.food_position[1],20,20))
    # handels collison with wall ,body ,food
    def handel_colliosion(self):
        if  self.self_collision() or self.wall_collision():
            self.end_game()
        if self.food_collision(self.food_position):
            self.score+=1
            if self.speed<17 :self.speed+=0.5
            self.new_food_position()
    # game loop
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
     
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            key=pygame.key.get_pressed()
            self.set_direction(key)
            self.movement(self.food_position)
            self.handel_colliosion()
            self.screen.fill(self.black)
            self.show_score()
            self.draw_food()
            self.draw_body()
            pygame.display.update()
            clock.tick(self.speed)
            


#main
g=Game()
g.run()