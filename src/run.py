import sys

from simulation import MarriagesSimulation

def start_simulation(size):
    simulation = MarriagesSimulation(size)
    simulation.populate()
    simulation.set_preferences()
    simulation.match()

def main():
    if len(sys.argv) != 2:
        raise RuntimeError('Insufficient arguments')
    size = int(sys.argv[1])
    start_simulation(size)

if __name__ == '__main__': main()
