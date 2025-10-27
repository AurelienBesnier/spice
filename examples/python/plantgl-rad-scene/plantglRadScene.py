from openalea.spice.simulator import *

if __name__ == "__main__":
    simulator = Simulator(config_file="simulation.ini")
    simulator.setup()
    simulator.run()
    calibrated_res = simulator.calibrateResults("spectrum/chambre1_spectrum",
                                                "points_calibration.csv")
    simulator.results.writeResults()

    simulator.visualizeResults()



# command visualiser Environnement PlantGL
# ipython
# %gui qt
# run planglRadScene.py