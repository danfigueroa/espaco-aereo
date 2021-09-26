from mesa import Agent

class Aeronave(Agent):
    
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos
        self.amount = 0
        self.pos = [0,0]

    def step(self):
        all_p = self.amount
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        for n in neighbors:
            all_p += n.amount
        average_p = all_p/(len(neighbors)+1)

        self._nextAmount += self.model.difusion * average_p - self.amount

    def advance(self):
        pass

    def get_position(self):
        pass

    def move(self, forward, angle):
         # Aeronave apontando para o norte
        self.new_pos = [self.pos[0]+np.sin(angle)*forward, self.pos[1]+np.cos(angle)*forward]
        self.model.grid.move_agent(self, next_point)
