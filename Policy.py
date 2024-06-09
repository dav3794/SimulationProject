import numpy as np
from abc import ABC
from typing import List, Literal
from Agent import Agent

class Policy(ABC):
    """Abstract class to represent a policy."""
    def update(self, agents):
        """Update the state of an agent."""
        pass


class BrownianPolicy(Policy):
    """Class to represent a Brownian policy - the direction of 
    an agent changes only due to random noise."""

    def __init__(self, eta: float = 2):
        """Initialize the Brownian policy.

        Args:
            eta (float): Noise level.
        """
        self.eta = eta

    def update(self, agents: List[Agent]) -> List[Agent]:
        """Update the state of agents."""
        new_agents = []
        for agent in agents:
            noise = np.random.uniform(-self.eta/2, self.eta/2)
            agent.theta_0 += noise
            new_x = agent.x + agent.v_0 * np.cos(agent.theta_0)
            new_y = agent.y + agent.v_0 * np.sin(agent.theta_0)
            new_agent = Agent(new_x, new_y, agent.v_0, agent.theta_0)
            new_agents.append(new_agent)
        return new_agents
    
class VicsekPolicy(Policy):
    """Class to represent a Vicsek model of collective motion."""

    def __init__(self, eta: float = 0.1):
        """Initialize the Vicsek policy.

        Args:
            eta (float): Noise level.
        """
        self.eta = eta

    def update(self, agents: List[Agent]) -> List[Agent]:
        """Update the state of agents."""
        new_agents = []
        average_theta = np.mean([agent.theta_0 for agent in agents])
        for agent in agents:
            noise = np.random.uniform(-self.eta/2, self.eta/2)
            new_theta = average_theta + noise
            new_x = agent.x + agent.v_0 * np.cos(new_theta)
            new_y = agent.y + agent.v_0 * np.sin(new_theta)
            new_agent = Agent(new_x, new_y, agent.v_0, new_theta)
            new_agents.append(new_agent)
        return new_agents
    
class LocalInteractionPolicy(Policy):
    """Class to represent a policy with attraction or repulsion."""

    def __init__(self, 
                 type: Literal['attraction', 'repulsion'], 
                 g: float = 0.1, 
                 interaction_radius: float = 1.0, 
                 eta: float = 1):
        """Initialize the local interaction policy.

        Args:
            type (Literal['attraction', 'repulsion']): Type of interaction.
            g (float): Interaction level.
            interaction_radius (float): Interaction radius.
            eta (float): Noise level.
        """
        self.type = type
        self.g = g
        self.interaction_radius = interaction_radius
        self.eta = eta

    def update(self, agents: List[Agent]) -> List[Agent]:
        """Update the state of agents."""
        new_agents = []
        for agent in agents:
            x, y = agent.x, agent.y
            v_x = agent.v_0 * np.cos(agent.theta_0)
            v_y = agent.v_0 * np.sin(agent.theta_0)

            tmp_v_x, tmp_v_y = v_x, v_y
            for other_agent in agents:
                if other_agent is not agent:
                    distance = np.sqrt((x - other_agent.x)**2 + (y - other_agent.y)**2)
                    if distance < self.interaction_radius:
                        if self.type == 'attraction':
                            tmp_v_x += self.g / (other_agent.x - x)
                            tmp_v_y += self.g / (other_agent.y - y)
                        else:   
                            tmp_v_x -= self.g / (other_agent.x - x)
                            tmp_v_y -= self.g / (other_agent.y - y) 

            noise = np.random.uniform(-self.eta/2, self.eta/2)
            new_theta = np.arctan2(tmp_v_y, tmp_v_x) + noise
            new_v = agent.v_0

            v_x = new_v * np.cos(new_theta)
            v_y = new_v * np.sin(new_theta)

            new_x = x + v_x
            new_y = y + v_y
            new_agent = Agent(new_x, new_y, new_v, new_theta)
            new_agents.append(new_agent)
        return new_agents
