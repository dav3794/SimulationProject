import numpy as np

class Agent:
    """Class to represent an agent."""
    def __init__(self, 
                 x: float, 
                 y: float, 
                 v_0: float, 
                 theta_0: float, 
                 a_0: float = 0.0, 
                 psi_0: float = 0.0, 
                 alpha_0: float = 0.0):
        """Initialize the agent.

        Args:
            x (float): X-coordinate of the agent.
            y (float): Y-coordinate of the agent.
            v_0 (float): Initial velocity of the agent.
            theta_0 (float): Initial angle of the agent's velocity.
            a_0 (float): Initial acceleration of the agent.
            psi_0 (float): Initial angle of the agent's acceleration.
            alpha_0 (float): Initial angular velocity of the agent.
        """
        self.x = x
        self.y = y
        self.v_0 = v_0
        self.theta_0 = theta_0
        self.a_0 = a_0
        self.psi_0 = psi_0
        self.alpha_0 = alpha_0

    @classmethod
    def random_itialize(cls, 
                        X: float, 
                        Y: float, 
                        v_0: float|None = None, 
                        theta_0: float|None = None,
                        a_0: float|None = None,
                        psi_0: float|None = None,
                        alpha_0: float|None = None):
        """Initialize the agent with random coordinates and velocity.

        Args:
            X (float): Width of the simulation box.
            Y (float): Height of the simulation box.
            v_0 (float): Initial velocity of the agent. If None, a random velocity is chosen.
            theta_0 (float): Initial angle of the agent's velocity. If None, a random angle is chosen.
            a_0 (float): Initial acceleration of the agent. If None, a random acceleration is chosen.
            psi_0 (float): Initial angle of the agent's acceleration. If None, a random angle is chosen.
            alpha_0 (float): Initial angular velocity of the agent. If None, a random angular velocity is chosen.

        Returns:
            Agent: An agent with random coordinates and velocity.
        """
        x = np.random.rand() * X
        y = np.random.rand() * Y
        if v_0 is None:
            v_0 = np.random.rand() * 0.3
        if theta_0 is None:
            theta_0 = np.random.rand() * 2 * np.pi
        if a_0 is None:
            a_0 = np.random.rand() * 0.01
        if psi_0 is None:
            psi_0 = np.random.rand() * 2 * np.pi
        if alpha_0 is None:
            alpha_0 = np.random.rand() * 0.1
        return cls(x, y, v_0, theta_0)
