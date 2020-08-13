# PLAYER 
import pygame
import numpy as np
import random
from defs import *
from neural_net import *

class player():
    
    def __init__(self, screen):
        self.screen = screen
        self.speed = 8
        self.x = 100
        self.y = 350
        self.color = (0,0,255)
        self.rad = 10
        self.rect = pygame.Rect(self.x - self.rad, self.y - self.rad, 2*self.rad, 2*self.rad )
        
        self.nnet = neural_net(NNET_INPUTS, NNET_HIDDEN, NNET_OUTPUTS)
        self.timeAlive = 0; 
        self.dis_pole = 0;  
        self.dis_middle = 0
        self.time_alive = 0; 
        self.fitness = 0; 
        self.alive = True; 

        
    def draw(self, blocks, time): # SIMILAR TO UPDATE
        
        if(self.alive == True):
            self.time_alive = time
            self.control_player(blocks)
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)
            self.rect = pygame.Rect(self.x - self.rad/2, self.y - self.rad/2, self.rad, self.rad )
            
        
    def distance_inputs(self, blocks):
        x_dist = 200; 
        mid_dist = 200; 
        
        for i in blocks:
            dist_to_i_block = i.rect[0] - self.x
            
            if (dist_to_i_block < x_dist) and (dist_to_i_block > 0):
                x_dist = dist_to_i_block;
                
                if i.rect[1]  == 0:
                    mid_dist = 400 - self.y
                elif i.rect[1] == 200:
                    mid_dist = 100 - self.y
                
                mid_dist += 400
        
        
         
        x_dist = ((x_dist/700)*.99)+0.01;
        mid_dist = ((mid_dist/800)*.99)+0.01
        
        if(mid_dist < 0):
            print("mid_dist: ", mid_dist)
        
        
        inputs = [x_dist, mid_dist]
                        
        return inputs
    

    def control_player(self, blocks):
        inputs = self.distance_inputs(blocks)
        val = self.nnet.get_max_value(inputs)
        
        UP = val[0]
        DOWN = val[1]
        STAY = val[2]
        
        if (UP > DOWN) & (UP > STAY):
            self.y += self.speed;
        elif (DOWN > UP) & (DOWN > STAY):
            self.y -= self.speed;
        else:
            self.y += 0; 
        
        
    def detect_collision(self, blocks, time):
        for p in blocks:
            if p.rect.colliderect(self.rect) or (self.y < 0) or (self.y > 500):
                #self.time_alive = time
                #self.dis_middle = self.distance_inputs(blocks)[1]
                self.fitness = self.distance_inputs(blocks)[1]
                self.alive = False; 
                
                
    def create_offspring(p1, p2, screen):
        new_player = player(screen)
        new_player.nnet.create_mixed_weights(p1.nnet, p2.nnet)
        return new_player
    
    
    def restart_player(self):
        self.y = 250;
        self.time_alive = 0; 
        self.fitness = 0; 
        self.alive = True; 



class player_cluster():
    
    def __init__(self, screen):
        self.screen = screen
        self.num_players = 200
        self.players = []
        self.create_players()
        
        
    def create_players(self):
        for i in range(self.num_players):
            self.players.append(player(self.screen))
        
        return self.players
        
    def draw_players(self, blocks, time): # SIMILAR TO UPDATE FUNCTION
        
        num_alive = 0; 
        for i in self.players:
            i.draw(blocks, time)
            if i.alive == True:
                num_alive += 1; 
                
        print("Num_alive: ", num_alive)
        
                
            
    def detect_collision(self, blocks, game_time):
        for i in self.players:
            i.detect_collision(blocks,game_time)

    def restart_game(self):
        all_players_alive = False;
            
        for i in self.players:
            all_players_alive = i.alive or all_players_alive
        
        if all_players_alive == True:
            return True
        else:
            return False
        
            
    def evolve_population(self, blocks):
        for i in self.players:
            #x_dist, mid_dist = i.distance_inputs(blocks)
            i.fitness += i.time_alive*i.fitness 

            
        self.players.sort(key=lambda x: x.fitness, reverse=True)
        
        cut_off = int(len(self.players)*MUTATION_CUT_OFF)
        good_players = self.players[0:cut_off]
        bad_players = self.players[cut_off:]
        num_bad_to_take = int(len(self.players)*MUTATION_BAD_TO_KEEP)
        
        for p in bad_players:
            p.nnet.modify_weights()
            
        new_players = []
        
        idx_bad_to_take = np.random.choice(np.arange(len(bad_players)), num_bad_to_take, replace=False)
        
        for index in idx_bad_to_take:
            new_players.append(bad_players[index])
            
        new_players.extend(good_players)
        
        children_needed = len(self.players)-len(new_players)
        
        while len(new_players) < len(self.players):
            idx_to_breed = np.random.choice(np.arange(len(good_players)), 2, replace = False)
            if idx_to_breed[0] != idx_to_breed[1]:
                new_player =  player.create_offspring(good_players[idx_to_breed[0]], good_players[idx_to_breed[1]], self.screen)
                if random.random() < MUTATION_MODIFY_CHANCE_LIMIT:
                    new_player.nnet.modify_weights()
                new_players.append(new_player)
                
        for p in self.players:
            p.restart_player();
            
        self.players = new_players
        
        
        
        
        
    #def get_inputs(self, players, blocks):
    
        #inputs = []
        #for i in range(len(players)):
        #    x_dist, mid_dist = players[i].distance_inputs(blocks)
         #   
          #  inputs.append(x_dist)
           # inputs.append(mid_dist)
            
        #return(inputs)
            
            
        
    