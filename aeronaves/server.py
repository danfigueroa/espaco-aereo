from .model import *
from .agent import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.7,
                 "Color": "blue",
                 "Layer": "1"
                 }
    """
    portrayal = {}
    if type(agent) is Aeronave:
        portrayal["Shape"] = "circle",
        portrayal["r"] = 0.7,
        portrayal["Layer"] = 1,
        portrayal["Color"] = "blue"
    elif type(agent) is Radar:
        portrayal["Shape"] = "circle",
        portrayal["r"] = 2.0,
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["Color"] = "#00FF00BB"
    """
                
    return portrayal

model_params = {
    "height": 50,
    "width": 50,
    #"evaporate": UserSettableParameter("slider", "Evaporation Rate", 0.50, 0.01, 0.50, 0.01),
    #"diffusion": UserSettableParameter("slider", "Diffusion Rate", 1.0, 0.0, 1.0, 0.1),
    #"initdrop": UserSettableParameter("slider", "Initial Drop", 100, 100, 1000, 50),
    #"prob_random": UserSettableParameter("slider", "Random Move Probability", 0.1, 0.0, 1.0, 0.1),
    "drop_rate": UserSettableParameter("slider", "Drop Decay Rate", 0.9, 0, 1, 0.01),
}

# Definição de atributos do grid
grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

chart = ChartModule([{"Label": "Naves fora do radar",
                      "Color": "Red"}],
                    data_collector_name='datacollector')

server = ModularServer(EspacoAereo,
                       [grid, chart],
                       "Espaço Aéreo",
                       {"N":10, "width":50, "height":50})

server.port = 8521 # The default
server.launch()
