"""
@author Jeremiah Marquez and Ryan Cadalin
 Pygame base template for opening a window
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame

# Define some colors and PI
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

PI = 3.14159265358979323846264338327950288419716939937510582

#def score_Counter():
    

#class to represent enemies
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # --- Alien Behaviours ---
        #Alien's position
        
        self.x = 0
        self.y = 0
        
        #Alien's vector
        self.change_x = 0
        self.change_y = 0

        #Alien colour
        self.colour = (0, 255, 0)

    # --- Alien Behaviours ---
    def draw( self, screen):
        pygame.draw.line(screen, BLACK, [15, 15], [0, 40], 1)
        pygame.draw.line(screen, BLACK, [15, 15], [10, 40], 1)
        pygame.draw.line(screen, BLACK, [15, 15], [20, 40], 1)
        pygame.draw.line(screen, BLACK, [15, 15], [30, 40], 1)
        pygame.draw.ellipse(screen, GREEN, [0, 0, 30, 30], 0)
        pygame.draw.ellipse(screen, BLACK, [0, 0, 30, 30], 1)
        pygame.draw.ellipse(screen, BLACK, [8, 8, 5, 5], 0)
        pygame.draw.ellipse(screen, BLACK, [18, 8, 5, 5], 0)

#class to represent player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # --- Player's Behaviours ---

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(RED)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        

        #Player's vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    
      
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([5, 10])
        self.image.fill(CYAN)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 10
        
        
pygame.init()
        
# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
# List of each bullet
bullet_list = pygame.sprite.Group()

# Create the player paddle object
player = Player(400, 400)
all_sprite_list.add(player)

'''
my_Alien = Alien()
my_Alien.draw(screen)
all_sprite_list.add(my_Alien)
'''
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_d:
                player.changespeed(5, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -5)
            elif event.key == pygame.K_s:
                player.changespeed(0, 5)

            elif event.key == pygame.K_UP:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+5
                bullet.rect.y = player.rect.y+5
                # Add the bullet to the lists
                all_sprite_list.add(bullet)
                bullet_list.add(bullet)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(5, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 5)
            elif event.key == pygame.K_s:
                player.changespeed(0, -5)

        
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    all_sprite_list.update()
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    all_sprite_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
