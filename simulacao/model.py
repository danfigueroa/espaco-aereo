from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from random import *
from .agent import *

def compute_gini(model):
    #detectada = random.uniform(0,1)

    agent_positions = [agent.position for agent in model.schedule.agents]
    x = sorted(agent_positions)
    numeroAeronaves = model.numeroAeronaves
    B = 10
    return (numeroAeronaves*B)

# Definição do modelo da simulação
class EspacoAereo(Model):

    """Modelo de simulação de detecção de aeronaves invasoras."""
    def __init__(self, numeroAeronaves, width, height):

        self.numeroAeronaves = numeroAeronaves

        # Requisitos para a renderização do Mesa
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Criando os agentes de aeronaves
        for i in range(self.numeroAeronaves):
            aeronave = Aeronave(i, self) 
            self.schedule.add(aeronave)
            global posicaoAtual
            #posicaoAtual = (0, random.randint(0, 49))
            self.grid.place_agent(aeronave, posicaoAtual)

        """
        # Criando os agentes de radar
        radar = Radar(i, self)
        self.schedule.add(radar)
        self.grid.place_agent(radar, posicaoAtual)

        # Add the Radar locations
        radar = Radar(self)
        self.grid.place_agent(radar, (20,20))
        self.schedule.add(radar)
        """
        
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Position": "position"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()