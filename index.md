This is a one day project aimed at understanding the basics of neural networks. 

## THE GAME 
In this project, I have created a very simple game using Pygame. The objective of the games is to ovoid colliding with the blocks running across the screen by using the up and down keys. Once the game was up and running, I replaced the key controls with outputs from the neural network. The possible outputs are moving up, moving down, or staying in place. 

## THE NEURAL NETWORK
Given that for a game is difficult to provide existing data to train our neural network, the neural network best suited for this project is a Generic neural network. Each instance of the player is given its own decision making neural network. The players that perform the best are chosen to form the base of the next generation of players. The base code or neural network of the players chosen is then mutated/changed to allow for different behavior in order to prevent future players from performing the exact movements. In this analogy, the genes that are passed on from one generation to the next are the neural network weights. 

### Concrete Details On The Neural Network
The neural network consist of two inputs. The distance from the player to the nearest incoming obstacle and the distance from the player to the center of the path that to avoid collision. It has one hidden layer consisting of five nodes. The final layer is the outputs layer and it has three nodes which correspond to the probability of moving up, moving down, or staying in place. 


## GAME SCREENSHOT 
The following a screenshot of the neural network learning to play the game. In this instance, the zeroth generation was able to play the game without colliding with any of the obstacles. Different settings resulted in different number of iterations for the player to learn to play the game, but in average it took the neural network about 8 iterations to avoid all collisions. 


![Image of neural net game](https://raw.githubusercontent.com/josherrera2020/hello_world_of_neural_network/master/working_neural_net_game_1.png)
