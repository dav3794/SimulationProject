import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Tuple
import numpy as np

def calculate_mass_center_trajectory(x_data, y_data):
    # Calculate mass center coordinates for each frame
    mass_center_x = np.mean(x_data, axis=0)
    mass_center_y = np.mean(y_data, axis=0)
    return mass_center_x, mass_center_y


def plot_simulation(history: List[Tuple[List[float], List[float]]], X: int = 1, Y: int = 1, delay: int = 70):
    T = len(history)
    x_data, y_data = zip(*history)
    scatter_trace = go.Scatter(
        x=x_data[0], 
        y=y_data[0], 
        mode='markers',
        marker=dict(color='blue', size=10),
        showlegend=False,
        )

    mass_centres_x, mass_centres_y = zip(*[calculate_mass_center_trajectory(x_data[i], y_data[i]) for i in range(T)])
    mass_trace = go.Scatter(
        x=[mass_centres_x[0]], 
        y=[mass_centres_y[0]], 
        mode='markers',
        marker=dict(color='red', size=10),
        showlegend=False,
        )

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True, subplot_titles=['Simulation', 'Mass center trajectory'])
    fig.add_trace(scatter_trace, row=1, col=1)
    fig.add_trace(mass_trace, row=1, col=2)

    frames = [dict(
        name = k,
        data = [go.Scatter(
                    x=x_data[k],
                    y=y_data[k],
                    mode="markers",
                    marker=dict(color="blue", size=10)),
                go.Scatter(
                    x=mass_centres_x[:k],
                    y=mass_centres_y[:k],
                    mode="lines",
                    line=dict(color="red"))
                ],
        traces = [0, 1],
    ) for k in range(T)]

    updatemenus = [dict(type='buttons',
                        buttons=[dict(label='Play',
                                    method='animate',
                                    args=[[f'{k}' for k in range(T)], 
                                            dict(frame=dict(duration=delay, redraw=False), 
                                                transition=dict(duration=delay),
                                                easing='cubic',
                                                fromcurrent=True,
                                                #   mode='immediate'
                                                                    )])],
                        direction= 'left', 
                        pad=dict(r= 10, t=85), 
                        showactive =True, x= 0.1, y= 0, xanchor= 'right', yanchor= 'top')
                ]

    sliders = [{'yanchor': 'top',
                'xanchor': 'left', 
                'currentvalue': {'font': {'size': 16}, 'prefix': 'Timestep: ', 'visible': True, 'xanchor': 'right'},
                'transition': {'duration': delay, 'easing': 'linear'},
                'pad': {'b': 10, 't': 50}, 
                'len': 0.9, 'x': 0.1, 'y': 0, 
                'steps': [{'args': [[k], {'frame': {'duration': delay, 'easing': 'linear', 'redraw': False},
                                        'transition': {'duration': 0, 'easing': 'linear'}}], 
                        'label': k, 'method': 'animate'} for k in range(T)       
                        ]}]


    fig.update(frames=frames)
    fig.update_layout(
        updatemenus=updatemenus, 
        sliders=sliders,
        # template='plotly_white',
        xaxis = {'range': [0, X]},
        yaxis = {'range': [0, Y]},
        xaxis2 = {'range': [0, X]},
        yaxis2 = {'range': [0, Y]},
        )

    fig.show()
