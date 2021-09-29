from aeronave import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)
server = ModularServer(Aeronave,
                       [grid],
                       "Money Model",
                       {"N":100, "width":10, "height":10})

chart = ChartModule([{"Label": "Gráfico",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = ModularServer(Aeronave,
                       [grid, chart],
                       "Money Model",
                       {"N":100, "width":50, "height":50})

server.port = 8521 # The default
server.launch()
