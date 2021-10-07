from mesa import Agent
from random import *

class Aeronave(Agent):
    
    def __init__(self, position, pontoCego, model):
        super().__init__(position, model)
        self.position = position
        self.pontoCego = pontoCego

    # Definir um target para o movimento dos agentes
    def startingPosition(self):
        x_origin = 0
        y_origin = 0
        position = (x_origin, y_origin)
        origin = self.grid.place_agent(position)
        return origin

    # Função que controla o movimento da aeronave no grid
    def move(self):
        x = 0
        y = 0
        position = (x, y)
        #while True:
        #    x = x+1
         #   y = y+1
          #  new_position = (x,y)
           # self.model.grid.move_agent(self, new_position)
            #print(new_position)
        
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

        #origin = self.startingPosition()
        #y = self.random.startingPosition()
        #self.model.grid.move_agent(self, (x,y))
        #new_position = self.random.choice(x, y)
        #new_position = origin + (1,1)
        #self.model.grid.move_agent(self, new_position)
        #print(new_position)

    # Função que define o comportamento da aeronave em cada step da simulação
    def step(self):
        self.move()

    # Função para dizer se a aeronave voa dentro ou fora do campo de detecção do radar
    def deteccao(self, pontoCego):
        return pontoCego

    def advance(self):
        pass

    def get_position(self):
        pass

