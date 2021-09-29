from aeronave import *
from model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.7,
                 "Color": "blue",
                 "Layer": "0"
                 }

    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 50, 800, 500)
server = ModularServer(EspacoAereo,
                       [grid],
                       "Espaço Aéreo",
                       {"N":100, "width":50, "height":50})

chart = ChartModule([{"Label": "Gráfico",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server.port = 8521 # The default
server.launch()
