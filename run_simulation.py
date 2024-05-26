#!/usr/bin/python3 

import argparse

from Cell import Cell
from Agent import Agent
from Policy import BrownianPolicy, VicsekPolicy, LocalInteractionPolicy
from plotter import plot_simulation


def parse_args():
    parser = argparse.ArgumentParser(description='Run a simulation of given type.')
    parser.add_argument(
        '-X',
        type=int,
        default=10,
        help='[Optional] Width of the simulation box. Default is 10.'
    )
    parser.add_argument(
        '-Y',
        type=int,
        default=10,
        help='[Optional] Height of the simulation box. Default is 10.'
    )
    parser.add_argument(
        '-b',
        '--boundary',
        choices=['reflective', 'periodic'],
        default='periodic',
        help='[Optional] Boundary conditions: reflective or periodic. Default is periodic.'
    )
    parser.add_argument(
        '-N',
        '--n_agents',
        type=int,
        default=10,
        help='[Optional] Number of agents in simulation. Default is 10.'
    )
    parser.add_argument(
        '-V0',
        '--init_velocity',
        type=float,
        default=0.3,
        help='[Optional] Initial absolute velocity of agents. Default is 0.3.'
    )
    parser.add_argument(
        '-t',
        '--n_frames',
        type=int,
        default=300,
        help='[Optional] Number of time frames in simulation. Default is 300.'
    )

    
    subparsers = parser.add_subparsers(dest='model', help='Model of simulation.')

    # Brownian policy
    brownian_parser = subparsers.add_parser('brownian', help='Brownian motion model.')
    brownian_parser.add_argument(
        '--eta', 
        type=float, 
        default=2, 
        help='Noise level. Default is 2.'
    )

    # Vicsek policy
    vicsek_parser = subparsers.add_parser('vicsek', help='Vicsek model of collective motion.')
    vicsek_parser.add_argument(
        '--eta', 
        type=float, 
        default=2, 
        help='Noise level. Default is 2.'
    )

    # interaction policy
    interaction_parser = subparsers.add_parser('local_interaction', help='Vicsek-like model with attraction/repulsion within certain radius.')
    interaction_parser.add_argument(
        '--type', 
        choices=['attraction', 'repulsion'], 
        required=True,
        help='Type of interaction: attraction or repulsion.'
    )
    interaction_parser.add_argument(
        '--g', 
        type=float, 
        default=0.1, 
        help='Interaction level. Default is 0.1.'
    )
    interaction_parser.add_argument(
        '--interaction_radius', 
        type=float, 
        default=1.0, 
        help='Interaction radius. Default is 1.0.'
    )
    interaction_parser.add_argument(
        '--eta', 
        type=float, 
        default=2, 
        help='Noise level. Default is 2.'
    )
    args = parser.parse_args()

    if not args.model:
        parser.print_help()
        parser.error('No model of simulation provided.')

    return args


if __name__ == '__main__':
    args = parse_args()

    agents = [Agent.random_itialize(args.X, args.Y, args.init_velocity) for _ in range(args.n_agents)]

    if args.model == 'brownian':
        policy = BrownianPolicy(eta=args.eta)
    elif args.model == 'vicsek':
        policy = VicsekPolicy(eta=args.eta)
    elif args.model == 'local_interaction':
        policy = LocalInteractionPolicy(
            type=args.type, 
            g=args.g, 
            interaction_radius=args.interaction_radius, 
            eta=args.eta
        )

    cell = Cell(args.X, args.Y, agents, policy, args.boundary)

    history, average_speed = cell.simulate(args.n_frames)

    plot_simulation(history, args.X, args.Y)
