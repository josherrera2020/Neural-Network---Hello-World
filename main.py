# Main function 
import numpy as numpy
import scipy
import pygame
#from defs import *
from blocks import *
from displayText import *
from player import *
from neural_net import *

#4, 6, 11, 10,  mutation 02. 

# mutation 0.5 : 1, 0, 26, 7, 1, 8, 10, 13, 0, 2, 

def run_game():
    
    # Simple pygame program
    
    # Import and initialize the pygame library
    import pygame
    pygame.init()
    
    # Set up the drawing window
    screen = pygame.display.set_mode([800, 500])

        
    #BLOCKS
    blocks = block_collection(screen)
    blocks.create_blocks()
    blocks_arr = blocks.get_blocks()
    
    
    # PLAYER
    players = player_cluster(screen)
    
    
    #NEURAL NETWORK
    n_net = neural_net(2,5,1)
    
    
    #CLOCK MANAGEMENT
    FPS = 30
    clock = pygame.time.Clock()
    dt = 0 
    game_time = 0 
    num_iterations = 0
    
    # Run until the user asks to quit
    running = True
    while running:
        
        # CLOCK MANAGEMENT 
        dt = clock.tick(FPS)
        game_time += dt
        
        
        # SCREEN TO WHITE
        screen.fill((255, 255, 255))
        
          
        # STOPPING THE GAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # DRAW BLOCKS 
        blocks.draw_bocks()


        # CREATE PLAYERS
        players.draw_players(blocks_arr, game_time)
        players.detect_collision(blocks_arr, game_time)
        

        
        # SCREEN TEXT
        game_time_text = "Time: " + str(game_time/1000)
        message_display(screen, game_time_text, 20)
        iterations_text = "Iterations: " + str(num_iterations)
        message_display(screen, iterations_text, 40)
        
        
        
        #RESTART GAME 
        if(players.restart_game() == False):
            players.evolve_population(blocks_arr)            
            blocks.restart_position(blocks_arr)
            game_time = 0;
            num_iterations += 1
  
      
        # UPDATE SCREEN        
        pygame.display.update()


if __name__ == "__main__":
    run_game()
    
# Done! Time to quit.
pygame.quit()
