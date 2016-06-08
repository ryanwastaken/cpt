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

PI = 3.14159265358979323846264338327950288419716939937510582

def score_Counter():
    

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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # --- Player's Behaviours ---
        #Players's position
        self.x = 500
        self.y = 500

        self.change_x = 
        
        
        
pygame.init()
        
# Set the width and height of the screen [width, height]
size = (1000, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    my_Alien = Alien()
    my_Alien.draw(screen) 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


