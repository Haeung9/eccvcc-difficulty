import os
import numpy as np
from src import simulation, parameters

import logging

def main():
    logLevel = logging.INFO
    useOriginal= True
    blockLength = 16
    colDegree = 3
    rowDegree = 4 
    hammingWeigthLow = 0
    hammingWeigtHigh = 16
    decisionStep = 2
    numSim = 1000

    dir = os.path.join(os.getcwd(), "data")
    directoryMaker(dir)
    logdir = os.path.join(os.getcwd(), "log")
    directoryMaker(logdir)
    logfile = os.path.join(logdir, "debug.log")
    logging.basicConfig(filename=logfile, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logLevel)

    simSetting = np.array([blockLength, colDegree, rowDegree, hammingWeigthLow, hammingWeigtHigh, decisionStep, numSim], dtype=int)
    simSetting.tofile(os.path.join(dir, "settings.csv"), sep=",")

    param = parameters.codeParameters(blockLength, rowDegree, colDegree, hammingWeigthLow, hammingWeigtHigh, decisionStep)
    (solutionFound, decoderSuccess) = simulation.runMonteCarlo(param, dir=dir, numSim=numSim, printStamp = True, useOriginal= useOriginal)
    print("# of solution found = ", solutionFound, ", Solving probability = ", float(solutionFound)/float(numSim))
    print("# of decoder success = ", decoderSuccess, ", Decoding probability = ", float(decoderSuccess)/float(numSim))


def directoryMaker(dir: os.path):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("Error: Failed to create the directory.")

if __name__ == "__main__":
    main()