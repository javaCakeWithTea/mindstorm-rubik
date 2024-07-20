## A virtual nerd to solve the cube. The nerd has learnt the "beginner" algorithm.

import cube
import numpy as np

class Nerd:

    rotationsFromStart = 0

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
        rFace = np.array([["any","blue","any"],
            ["any","blue","any"],
            ["any","any","any"]])
        lFace = np.array([["any","green","any"],
            ["any","green","any"],
            ["any","any","any"]])
        bFace = np.array([["any","orange","any"],
            ["any","orange","any"],
            ["any","any","any"]])
        dFace = np.array([["any","any","any"],
            ["any","yellow","any"],
            ["any","any","any"]])
        
        completeWhiteCross = cube.Cube(fFace,uFace,lFace,rFace,bFace,dFace)
        
        if aCube == completeWhiteCross:
            return True
        else:
            return False

    @staticmethod
    def solve(cube):
        ## 1. White cross.
        ## Locate whites that aren't corners.
        ## U is the white side.
        if Nerd.whiteCrossComplete(cube):
            return True
        else:
            ## Check which bits of the cross are complete.
            topOfCross = (cube.u[0,1]=="white")
            bottomOfCross = (cube.u[2,1]=="white")
            leftOfCross = (cube.u[1,0]=="white")
            rightOfCross = (cube.u[1,2]=="white")
            Nerd.solveBadCross(cube,topOfCross,bottomOfCross,leftOfCross,rightOfCross)
            return False

    @staticmethod 
    def solveBadCross(cube,topOfCross,bottomOfCross,leftOfCross,rightOfCross):

        if not topOfCross:
            cube.centreOnFace("b")
            topOfCross == True
        elif not bottomOfCross:
            cube.centreOnFace("f")
            bottomOfCross == True
        elif not leftOfCross:
            cube.centreOnFace("l")
            leftOfCross == True
        elif not rightOfCross:
            cube.centreOnFace("r")
            rightOfCross == True
        else:
            return cube

        frontFace = cube.__dict__[cube.labelF]

        if "white" == frontFace[0,1]:
            cube = Nerd.flipEdge(cube)
        elif "white" == frontFace[1,0]:
            cube = Nerd.fromMiddleLayerLeft(cube)
        elif "white" == frontFace[1,2]:
            cube = Nerd.fromMiddleLayerRight(cube)
        elif "white" == frontFace[2,1]:
            cube = Nerd.fromBottomLayer(cube)
        else:
            ## Do a double bottom turn?
            print("Well something 'aint right..?")
            
        return Nerd.solveBadCross(cube,topOfCross,bottomOfCross,leftOfCross,rightOfCross)

    @staticmethod
    def flipEdge(cube):
        ## F U' R U
        cube = cube.rotateLabeledSide("f")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("r")
        cube = cube.rotateLabeledSide("u")
        return cube
    
    @staticmethod
    def fromBottomLayer(cube):
        ## F' U' R U
        cube = cube.rotateLabeledSide("f")
        cube = cube.rotateLabeledSide("f")
        cube = cube.rotateLabeledSide("f")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("r")
        cube = cube.rotateLabeledSide("u")
        return cube

    @staticmethod
    def fromMiddleLayerRight(cube):
        ## U' R U
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("r")
        cube = cube.rotateLabeledSide("u")
        return cube

    @staticmethod
    def fromMiddleLayerLeft(cube):
        ## U L' U'
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("l")
        cube = cube.rotateLabeledSide("l")
        cube = cube.rotateLabeledSide("l")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        cube = cube.rotateLabeledSide("u")
        return cube








        
