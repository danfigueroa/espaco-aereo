from mesa import Agent
from random import *

posicaoAtual = (20,20) #(0,random.randrange(0,49)) 

#Função que controla as coordenadas da movimentação
def alterarPosicao(changePosition, change):
    return (changePosition[0] + change[0]), (changePosition[1] + change[1])

# Definição dos agentes que representam as aeronaves na simulação
class Aeronave(Agent):
    
    def __init__(self, id, model):
        super().__init__(id, model)
        self.position = posicaoAtual
        self.pontoCego = 0.33

    # Função que controla o movimento da aeronave no grid
    def move(self):
        global posicaoAtual
        posicaoAtual = alterarPosicao(posicaoAtual, [1,0])
        self.model.grid.move_agent(self, posicaoAtual)
    
    # Função que define o comportamento aeronave cada passo da simulação
    def step(self):
        self.move()

# Definição do agente que representa um radar
class Radar(Agent):
    def __init__(self, model):
        super().__init__(id, model)

    def deteccao(self):
        pass

    

