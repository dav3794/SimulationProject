# Simulations of collective behaviour

The aim of this project is to implement simulations of collective behaviours according to selected physical models. It was made for the Introduction to physics of complexity - Statistical physics of complex networks course.

## Installation

All scripts require `Python >= 3.8`. To install required packages, simply run:

```
pip install -r requirements.txt
```

## Usage

All simulations can be run by `run_simulation.py` script.

```
usage: run_simulation.py [-h] [-X X] [-Y Y] [-b {reflective,periodic}] [-N N_AGENTS] [-t N_FRAMES] {continuous,vicsek,local_interaction} ...

Run a simulation of given type.

positional arguments:
  {continuous,vicsek,local_interaction}
                        Model of simulation.
    brownian            Brownian motion model.
    vicsek              Vicsek model of collective motion.
    local_interaction   Vicsek-like model with attraction/repulsion within certain radius.

options:
  -h, --help            show this help message and exit
  -X X                  [Optional] Width of the simulation box. Default is 10.
  -Y Y                  [Optional] Height of the simulation box. Default is 10.
  -b {reflective,periodic}, --boundary {reflective,periodic}
                        [Optional] Boundary conditions: reflective or periodic. Default is periodic.
  -N N_AGENTS, --n_agents N_AGENTS
                        [Optional] Number of agents in simulation. Default is 10.
  -V0 INIT_VELOCITY, --init_velocity INIT_VELOCITY
                        [Optional] Initial absolute velocity of agents. Default is 0.3.
  -t N_FRAMES, --n_frames N_FRAMES
                        [Optional] Number of time frames in simulation. Default is 300.
```

Currently, there are three models of group behaviour simulations:

1. **Brownian** - Brownian motion model, assuming no interactions between agents. Their direction of movement changes only due to random noise. Usage:

   ```
   usage: run_simulation.py brownian [-h] [--eta ETA]

   options:
     -h, --help  show this help message and exit
     --eta ETA   Noise level. Default is 2.
   ```
2. **Vicsek** - Vicsek motion model proposed in [[Vicsek T. et all, 1995]](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.75.1226). Usage:

   ```
   usage: run_simulation.py vicsek [-h] [--eta ETA]

   options:
     -h, --help  show this help message and exit
     --eta ETA   Noise level. Default is 2.
   ```
3. **Local interaction** - Vicsek-like motion model, where the changes in movement direction are described by either attraction or repulsion of agents within a given radius. Usage:

   ```
   usage: run_simulation.py local_interaction [-h] --type {attraction,repulsion} [--g G] [--interaction_radius INTERACTION_RADIUS] [--eta ETA]

   options:
     -h, --help            show this help message and exit
     --type {attraction,repulsion}
                           Type of interaction: attraction or repulsion.
     --g G                 Interaction level. Default is 0.1.
     --interaction_radius INTERACTION_RADIUS
                           Interaction radius. Default is 1.0.
     --eta ETA             Noise level. Default is 2.
   ```

Running simulation will open browser tab with two plots - simulation of agents movements and their mass centre trajectory. To see the simulation, simply click on 'Play' button at the bottom of the page.

## Examples

* If you would like to simulate Brownian motion of `N = 30` particles with `V0 = 1` in a `25x25` box with `reflective` boundary conditions and `eta = 4` for `t = 500` time frames, you can run:

  ```
  python3 run_simulation.py -X 25 -Y 25 -b reflective -N 30 -V0 1 -t 500 brownian --eta 4
  ```
* To run simulation of local `attraction` interaction with default parameters of the cell with `N = 20` agents, and `interaction_radius = 2`, simply run:

  ```
  python3 run_simulation.py -N 20 local_interaction --type attraction --interaction_radius 2
  ```
