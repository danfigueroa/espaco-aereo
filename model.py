from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner
import random

# Definindo variáveis globais
posicaoAtual = (0,random.randrange(0,49)) 

#Função que controla as coordenadas da movimentação
def alterarPosicao(changePosition, change):
    return (changePosition[0] + change[0]), (changePosition[1] + change[1])

def compute_gini(model):
    agent_positions = [agent.position for agent in model.schedule.agents]
    x = sorted(agent_positions)
    N = model.num_agents
    B = 10
    return (N * B)

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
    def __init__(self, id, model):
        super().__init__(id, model)

    def deteccao(self):
        pass

# Definição do modelo da simulação
class EspacoAereo(Model):

    """Modelo de simulação de detecção de aeronaves invasoras."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Create agents
        for i in range(self.num_agents):
            aeronave = Aeronave(i, self) 
            self.schedule.add(aeronave)
            global posicaoAtual
            #posicaoAtual = (0, random.randint(0, 49))
            self.grid.place_agent(aeronave, posicaoAtual)
        
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Position": "position"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()