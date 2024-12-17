import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def _init_(self,groups):
        super()._init_(groups)
        self.image = pygame.image.load('5games-main/space shooter/images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center = (window_width/2, window_height/2))

    def update(self):
        print('ship is being updated')



pygame.init() #initialising pygame, just a general set-up

window_width,window_height = 1280,720
display_surface = pygame.display.set_mode((window_width,window_height)) #this is how you make a display for ur game
pygame.display.set_caption('space shooter') # to change the title of the window
running = True
clock = pygame.time.Clock() # clock functon of python, helps in mutating the frame rate. 

#plain orange colored surface
surf = pygame.Surface((100,100))
surf.fill('orange')
x =100

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)




#import images
# player_surf = pygame.image.load('5games-main/space shooter/images/player.png').convert_alpha() #'convert' or 'convert_alpha' makes the image lighter for the game to run it faster.
# player_rect = player_surf.get_frect(center = (window_width/2, window_height/2))
# player_direction = pygame.math.Vector2(1,1) #intial part of making the player move. vector(x,y); x: right, y:down

# player_speed = 150

star_surf = pygame.image.load('5games-main/space shooter/images/star.png').convert_alpha()
starcopy = pygame.Surface.copy(star_surf)
star_position = [(randint(0,window_width),randint(0,window_height)) for i in range(20)]

meteor_surf = pygame.image.load('5games-main/space shooter/images/meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (window_width/2, window_height/2))

laser_surf = pygame.image.load('5games-main/space shooter/images/laser.png')
laser_rect = laser_surf.get_frect(bottomleft = (20,window_height-20)) #the task was to put it on 20 pixels bottom and left. I subtracted 20 form 720px which is my windows height.



while running: # event loop, as without this, the window would just open and close instantly.
    dt = clock.tick()/1000  # delta time function is awesome for a common frame rate speed among all users of the game.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This enables me to close the widow upon pressing the close icon.
            running = False
            #input codes - if done within the event loop, we can d like this also.
        # if event.type ==pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        #     print('awesome')
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos #the player moves along with mouse motion

   #Input - more better inut method.
    # print(pygame.mouse.get_pos())
    # player_rect.center = pygame.mouse.get_pos() # here the player follows the mouse
    # keys = pygame.key.get_pressed() #this is how we use input from keyboard outside event loop
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # player_direction = player_direction.normalize() if player_direction else player_direction

    all_sprites.update()

    # recent_keys = pygame.key.get_just_pressed() #it is sued to find the recent key we pressed, and via this...
    # if recent_keys[pygame.K_SPACE]:             #...we can print 'fire laser' just once upon pressing space bar 
    #     print('fire laser')
   
   #drawing in the game
    display_surface.fill('darkgrey') # display colour

    display_surface.blit(meteor_surf,meteor_rect)
    # display_surface.blit(player_surf,player_rect)
    display_surface.blit(laser_surf,laser_rect)
    
    all_sprites.draw(display_surface)
##Thank you so much for your help. one day, when I too will have the competence - I will give back the value which I recieved from you.    

#player movement left to right to left to right...
    # player_rect.center += player_direction * player_speed *dt #multiplyling player speed with delta time all the users of the game get the same frame speed influneced by a common player speed - irrespective of the computer.
    # if player_rect.bottom>window_height or player_rect.top<0: #makes the player image go around like a dvd symbol lol.
    #     player_direction.y *=-1
    # if player_rect.right>window_width or player_rect.left<0:
    #     player_direction.x *=-1
   
   