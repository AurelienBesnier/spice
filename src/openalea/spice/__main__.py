import argparse
from openalea.spice.simulator import Simulator

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-c', '--config', type=str, default="", help="The configuration file for the simulation.")
    args = parser.parse_args()

    sim = Simulator(args.config)

    sim.run()

if __name__ == "__main__":
    main()
