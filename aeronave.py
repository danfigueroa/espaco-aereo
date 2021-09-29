from mesa import Agent
from random import *

class Aeronave(Agent):
    
    def __init__(self, position, pontoCego, model):
        super().__init__(position, model)
        self.position = position
        self.pontoCego = pontoCego

    # Função que controla o movimento da aeronave no grid
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.position,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    # Função que define o comportamento da aeronave em cada step da simulação
    def step(self):
        self.move()

    def deteccao(self, pontoCego):
        pontoCego = randint(0, 1)
        return pontoCego

    def advance(self):
        pass

    def get_position(self):
        pass

