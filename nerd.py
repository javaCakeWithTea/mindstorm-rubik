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
    def whiteBadCrossComplete(aCube):
        ## Checks if the white cross stage is complete.
        uFace = np.array([["any","white","any"],
            ["white","white","white"],
            ["any","white","any"]])
        fFace = np.array([["any","any","any"],
            ["any","red","any"],
            ["any","any","any"]])
        rFace = np.array([["any","any","any"],
            ["any","blue","any"],
            ["any","any","any"]])
        lFace = np.array([["any","any","any"],
            ["any","green","any"],
            ["any","any","any"]])
        bFace = np.array([["any","any","any"],
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
        if Nerd.whiteBadCrossComplete(aCube):
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
        elif not bottomOfCross:
            aCube.centreOnFace("f")
        elif not leftOfCross:
            aCube.centreOnFace("l")
        elif not rightOfCross:
            aCube.centreOnFace("r")
        else:
            ## Move the bottom two layers to original position.
            ## Means that faces remain the same colour.
            for i in range(4-numberOfBottomTwoLayerRotations%4):
                aCube.rotateBottom2Rows()
            return aCube

        frontFace = aCube.__dict__[aCube.labelF]

        if "white" == frontFace[0,1]:
            print("Flipping edge.")
            Nerd.flipEdge(aCube)
        elif "white" == frontFace[1,0]:
            print("From middle-layer left.")
            Nerd.fromMiddleLayerLeft(aCube)
        elif "white" == frontFace[1,2]:
            print("From middle-layer right.")
            Nerd.fromMiddleLayerRight(aCube)
        elif "white" == frontFace[2,1]:
            print("From bottom layer.")
            Nerd.fromBottomLayer(aCube)
        elif "white" in [aCube.d[0,1], aCube.d[1,0], aCube.d[1,2], aCube.d[2,1]]:
            print("From down under.")
            Nerd.fromDFace(aCube)
        else:
            ## Do a double bottom turn. If the white can't be found on this side we need to move it here.
            aCube.rotateBottom2Rows()
            numberOfBottomTwoLayerRotations+=1
        
        aCube.resetLabels()
        topOfCross = (aCube.u[0,1]=="white")
        bottomOfCross = (aCube.u[2,1]=="white")
        leftOfCross = (aCube.u[1,0]=="white")
        rightOfCross = (aCube.u[1,2]=="white")
        print(topOfCross,bottomOfCross,leftOfCross,rightOfCross,numberOfBottomTwoLayerRotations)
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
    
    @staticmethod
    def fromDFace(cube):
        ## Moves the white tile over to the correct orientation.
        ## Then flips it to the top.
        ## Side d is always d for any of the white cross re-labels.
        faceD = cube.d

        if faceD[2,1]=="white":
            cube.rotateLabeledSide("d")
            cube.rotateLabeledSide("d")
        elif faceD[1,0]=="white":
            cube.rotateLabeledSide("d")
        elif faceD[1,2]=="white":
            cube.rotateLabeledSide("d")
            cube.rotateLabeledSide("d")
            cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        return cube
    
    @staticmethod
    def badCrossToGood(cube):
        ## Takes a "bad" white cross and changes it to a "good" one.
        permutation = [cube.l,cube.f,cube.r,cube.b]
        opposites = {
            ["green","orange","red","blue"]:1,
            ["blue","green","orange","red"]:2,
            ["red","blue","green","orange"]:3,
            ["orange","red","blue","green"]:4
        }
        correctOrder = {
            ["green","blue","red","orange"]:1,
            ["blue","red","orange","green"]:2,
            ["red","orange","green","blue"]:3,
            ["orange","green","blue","red"]:4
        }
        if permutation in opposites:
            ## Add method to flip opposite.
            doFlip(cube)
        #elif permutation not in correctOrder:
            ## Swap adjacent.
        
        
        








        
