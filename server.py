from model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.7,
                 "Color": "blue",
                 "Layer": "1"
                 }
                
    return portrayal

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
