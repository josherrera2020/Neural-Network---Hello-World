# Blocks
import pygame
import numpy as np


class block():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = 300
        self.width = 25
        self.color = (255,0,0)
        self.rect_thick = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_position(self, dx, gap, num_blocks):
        self.x += dx; 
        if self.x < -50:
            self.x = self.x + gap*num_blocks ;
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y , self.width, self.height], self.rect_thick)
                
        
class block_collection():
            
    
    def __init__(self, screen):
        self.screen = screen
        self.dx = -4
        

        # STARTING X AND Y POSITIONS
        self.num_blocks = 6
        self.gap = 200
        circle_start = 100
        
        # ORIGINAL VALUES TO RESTART GAME        
        self.xs_start = np.linspace(circle_start + self.gap, circle_start + self.gap + self.gap*self.num_blocks, self.num_blocks+1)
        self.ys_start = [0, 200, 0, 200, 0, 200, 0,200]
        
        # INITIALIZE POSITION OF BLOCKS 
        self.xs = self.xs_start
        self.ys = self.ys_start
        
        
        self.blocks = []
        self.x_pos = []
        self.y_pos = []
        



    def get_blocks(self):
        return self.blocks

    def create_blocks(self):
         
        for i in range(self.num_blocks):
            block_n = block(self.screen, self.xs[i], self.ys[i])
            self.blocks.append(block_n)
        

    def draw_bocks(self):        
        
        for i in range(self.num_blocks):
            self.blocks[i].update_position(self.dx , self.gap, self.num_blocks)
            self.blocks[i].draw()
        
    def get_blocks_pos(self):
        
        for i in range(self.num_blocks):
            self.x_pos.append( self.blocks[i].x )
            self.y_pos.append( self.blocks[i].y )
            
        return self.x_pos, self.y_pos, self.blocks[1].width, self.blocks[1].height
    
    def restart_position(self, blocks):
        for i in range(len(blocks)):
            blocks[i].x = self.xs_start[i]
            
            
            
        