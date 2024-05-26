import numpy as np
from dataclasses import dataclass
from typing import List, Literal
from Agent import Agent
from Policy import Policy

@dataclass
class Cell:
    """Class to represent a periodic cell in a simulation box."""
    X: float
    Y: float
    agents: List[Agent]
    policy: Policy

    def __init__(self, 
                 X: float, 
                 Y: float, 
                 agents: List[Agent], 
                 policy: Policy, 
                 boundary_conditions: str = Literal['periodic', 'reflective']):
        self.X = X
        self.Y = Y
        self.agents = agents
        self.policy = policy
        self.boundary_conditions = boundary_conditions

    def update(self):
        """Update the state of the cell."""
        new_agents = self.policy.update(self.agents)
        for agent in new_agents:
            if self.boundary_conditions == 'reflective':
                if agent.x < 0 or agent.x > self.X:
                    agent.theta_0 = np.pi - agent.theta_0
                if agent.y < 0 or agent.y > self.Y:
                    agent.theta_0 = -agent.theta_0
                    
            elif self.boundary_conditions == 'periodic':
                agent.x = agent.x % self.X
                agent.y = agent.y % self.Y
        self.agents = new_agents

    def return_state(self):
        """Return the state of the cell."""
        x, y = [], []
        v_avg = np.zeros(2)
        for agent in self.agents:
            x.append(agent.x)
            y.append(agent.y)
            v_avg[0] += agent.v_0 * np.cos(agent.theta_0)
            v_avg[1] += agent.v_0 * np.sin(agent.theta_0)

        v_avg = np.linalg.norm(v_avg) / len(self.agents)
        return x, y, v_avg
    
    def simulate(self, T: int):
        """Simulate the cell for T frames."""
        history = []
        average_speed = []
        for _ in range(T):
            self.update()
            x, y, v_avg = self.return_state()
            history.append((x, y))
            average_speed.append(v_avg)
        return history, average_speed
