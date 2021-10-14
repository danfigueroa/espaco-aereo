from mesa import Model
from mesa.time import RandomActivation
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from random import *
from .agent import *

def compute_gini(model):

    agent_positions = [agent.position for agent in model.schedule.agents]
    x = sorted(agent_positions)
    numeroAeronaves = model.numeroAeronaves
    B = 10
    return (numeroAeronaves*B)

# Definição do modelo da simulação
class EspacoAereo(Model):

    """Modelo de simulação de detecção de aeronaves invasoras."""
    def __init__(self, numeroAeronaves, posicao, width, height):

        self.numeroAeronaves = numeroAeronaves
        self.posicao = posicao

        # Requisitos para a renderização do Mesa
        self.grid = MultiGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)
        #self.schedule = RandomActivation(self)
        self.running = True

        # Criando os agentes de aeronaves
        for i in range(self.numeroAeronaves):
            aeronave = Aeronave(i, self, posicao) 
            self.schedule.add(aeronave)
            posicao = aeronave.posicaoAtual
            #posicaoAtual = (randint(0, 49), randint(0, 49))
            self.grid.place_agent(aeronave, posicao)

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