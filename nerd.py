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
    def solve(aCube):
        ## 1. White cross.
        ## Locate whites that aren't corners.
        ## U is the white side.
        if Nerd.whiteCrossComplete(aCube):
            print("Bad white cross is complete.")
            return aCube
        else:
            ## Check which bits of the cross are complete.
            topOfCross = (aCube.u[0,1]=="white")
            bottomOfCross = (aCube.u[2,1]=="white")
            leftOfCross = (aCube.u[1,0]=="white")
            rightOfCross = (aCube.u[1,2]=="white")
            aCube = Nerd.solveBadCross(aCube,topOfCross,bottomOfCross,leftOfCross,rightOfCross,0)
            return aCube

    @staticmethod 
    def solveBadCross(aCube:cube.Cube,topOfCross,bottomOfCross,leftOfCross,rightOfCross,numberOfBottomTwoLayerRotations):

        if not topOfCross:
            aCube.centreOnFace("b")
            topOfCross == True
        elif not bottomOfCross:
            aCube.centreOnFace("f")
            bottomOfCross == True
        elif not leftOfCross:
            aCube.centreOnFace("l")
            leftOfCross == True
        elif not rightOfCross:
            aCube.centreOnFace("r")
            rightOfCross == True
        else:
            ## Move the bottom two layers to original position.
            ## Means that faces remain the same colour.
            for i in (4-numberOfBottomTwoLayerRotations):
                aCube.rotateBottom2Rows()
            return aCube

        frontFace = aCube.__dict__[aCube.labelF]

        if "white" == frontFace[0,1]:
            aCube = Nerd.flipEdge(aCube)
        elif "white" == frontFace[1,0]:
            aCube = Nerd.fromMiddleLayerLeft(aCube)
        elif "white" == frontFace[1,2]:
            aCube = Nerd.fromMiddleLayerRight(aCube)
        elif "white" == frontFace[2,1]:
            aCube = Nerd.fromBottomLayer(aCube)
        else:
            ## Do a double bottom turn. If the white can't be found on this side we need to move it here.
            print("Well something 'aint right..?")
            aCube.rotateBottom2Rows()
            numberOfBottomTwoLayerRotations+=1


            
        return Nerd.solveBadCross(aCube,topOfCross,bottomOfCross,leftOfCross,rightOfCross,numberOfBottomTwoLayerRotations)

    @staticmethod
    def flipEdge(cube):
        ## F U' R U
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("u")
        return cube
    
    @staticmethod
    def fromBottomLayer(cube):
        ## F' U' R U
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("u")
        return cube

    @staticmethod
    def fromMiddleLayerRight(cube):
        ## U' R U
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("u")
        return cube

    @staticmethod
    def fromMiddleLayerLeft(cube):
        ## U L' U'
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        cube.rotateLabeledSide("u")
        return cube








        
