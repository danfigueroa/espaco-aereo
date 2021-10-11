from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

from .agent import Aeronave, Radar

# Definindo variáveis globais
posicaoAtual = (0,random.randrange(0,49)) 

#Função que controla as coordenadas da movimentação
def alterarPosicao(changePosition, change):
    return (changePosition[0] + change[0]), (changePosition[1] + change[1])

def compute_gini(model):
    detectada = random.uniform(0,1)

    agent_positions = [agent.position for agent in model.schedule.agents]
    x = sorted(agent_positions)
    N = model.num_agents
    B = 10
    return (detectada)

# Definição do modelo da simulação
class EspacoAereo(Model):

    """Modelo de simulação de detecção de aeronaves invasoras."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Criando os agentes de aeronaves
        for i in range(self.num_agents):
            aeronave = Aeronave(i, self) 
            self.schedule.add(aeronave)
            global posicaoAtual
            #posicaoAtual = (0, random.randint(0, 49))
            self.grid.place_agent(aeronave, posicaoAtual)

        # Criando os agentes de radar
        radar = Radar(i, self)
        self.schedule.add(radar)
        self.grid.place_agent(radar, (20,20))
        
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Position": "position"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()