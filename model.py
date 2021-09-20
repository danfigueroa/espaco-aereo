from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa_geo import GeoSpace, GeoAgent, AgentCreator
from mesa import Model
import requests
url = 'http://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_20m.json'
r = requests.get(url)
geojson_states = r.json()

class State(GeoAgent):
    def __init__(self, unique_id, model, shape):
        super().__init__(unique_id, model, shape)

class GeoModel(Model):
    def __init__(self):
        self.grid = GeoSpace()
        
        state_agent_kwargs = dict(model=self)
        AC = AgentCreator(agent_class=State, agent_kwargs=state_agent_kwargs)
        agents = AC.from_GeoJSON(GeoJSON=geojson_states, unique_id="NAME")
        self.grid.add_agents(agents)

    def step(self):
        self.schedule.step()