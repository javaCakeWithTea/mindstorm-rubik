## A virtual nerd to solve the cube. The nerd has learnt the "beginner" algorithm.

import cube
import numpy as np

class Nerd:

    def isFinished(aCube):
        ## Checks cube against the default cube.
        ## If they match then the cube is complete.
        aCube == cube.Cube()

    ## Static methods do not need self as argument.
    @staticmethod
    def whiteCrossComplete(aCube):
        ## Checks if the white cross stage is complete.
        uFace = np.array([["any","white","any"],
            ["white","white","white"],
            ["any","white","any"]])
        fFace = np.array([["any","red","any"],
            ["any","red","any"],
            ["any","any","any"]])
        rFace = np.array([["any","orange","any"],
            ["any","orange","any"],
            ["any","any","any"]])
        lFace = np.array([["any","blue","any"],
            ["any","blue","any"],
            ["any","any","any"]])
        bFace = np.array([["any","black","any"],
            ["any","black","any"],
            ["any","any","any"]])
        dFace = np.array([["any","any","any"],
            ["any","any","any"],
            ["any","any","any"]])
        
        completeWhiteCross = cube.Cube(fFace,uFace,lFace,rFace,bFace,dFace)
        
        if aCube == completeWhiteCross:
            return True
        else:
            return False

    #def solve(cube):
        ## 1. White cross.