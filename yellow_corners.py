import numpy as np
import cube

class yellow_corners:
    ## This nerd has learnt to go from a yellow cross solution to yellow edges solution.

    @staticmethod
    def cornerLF(aCube:cube.Cube):
        colours = [aCube.l[2,2],aCube.f[2,0],aCube.d[0,0]]
        return ("green" in colours) and ("red" in colours) and ("yellow" in colours)
    
    @staticmethod
    def cornerFR(aCube:cube.Cube):
        colours = [aCube.f[2,2],aCube.r[2,0],aCube.d[0,2]]
        return ("red" in colours) and ("blue" in colours) and ("yellow" in colours)
    
    @staticmethod
    def cornerRB(aCube:cube.Cube):
        colours = [aCube.r[2,2],aCube.b[2,0],aCube.d[2,2]]
        return ("blue" in colours) and ("orange" in colours) and ("yellow" in colours)
    
    @staticmethod
    def cornerBL(aCube:cube.Cube):
        colours = [aCube.b[2,2],aCube.l[2,0],aCube.d[2,0]]
        return ("orange" in colours) and ("green" in colours) and ("yellow" in colours)
    
    @staticmethod
    def yellowCornersComplete(aCube:cube.Cube):
        ##Checks if the yellow cross stage is complete.
        completeYellowEdges = cube.Cube()
        completeYellowEdges.u = np.array([["white","white","white"],
            ["white","white","white"],
            ["white","white","white"]])
        completeYellowEdges.f = np.array([["red","red","red"],
            ["red","red","red"],
            ["any","red","any"]])
        completeYellowEdges.r = np.array([["blue","blue","blue"],
            ["blue","blue","blue"],
            ["any","blue","any"]])
        completeYellowEdges.l = np.array([["green","green","green"],
            ["green","green","green"],
            ["any","green","any"]])
        completeYellowEdges.b = np.array([["orange","orange","orange"],
            ["orange","orange","orange"],
            ["any","orange","any"]])
        completeYellowEdges.d = np.array([
            ["any","yellow","any"],
            ["yellow","yellow","yellow"],
            ["any","yellow","any"]])
        
        if (aCube == completeYellowEdges) and yellow_corners.cornerLF(aCube) and yellow_corners.cornerFR(aCube) and yellow_corners.cornerRB(aCube) and yellow_corners.cornerBL(aCube):
            return True
        else:
            return False
        
    @staticmethod
    def algo(aCube:cube.Cube):
        ## The algorithm that is repeated.
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("l")
        return

    @staticmethod
    def solve(aCube:cube.Cube):
        if yellow_corners.cornerLF(aCube) and yellow_corners.cornerFR(aCube) and yellow_corners.cornerRB(aCube) and yellow_corners.cornerBL(aCube):
            ## Edges in correct places.
            print("All corners in place.")
            return
        elif yellow_corners.cornerLF(aCube):
            print("LF is in place.")
            aCube.centreOnFace("b")
            yellow_corners.itterate(aCube)
        elif yellow_corners.cornerFR(aCube):
            print("FR is in place.")
            aCube.centreOnFace("l")
            yellow_corners.itterate(aCube)
        elif yellow_corners.cornerRB(aCube):
            print("RB is in place.")
            aCube.centreOnFace("f")
            yellow_corners.itterate(aCube)
        elif yellow_corners.cornerBL(aCube):
            print("BL is in place.")
            aCube.centreOnFace("r")
            yellow_corners.itterate(aCube)
        else:
            ## No corners correct.
            print("No corners in place.")
            yellow_corners.algo(aCube)
            yellow_corners.solve(aCube)

    def itterate(aCube:cube.Cube):
        ## Repeats the algorithm until the corners are in right place.
        while not yellow_corners.yellowCornersComplete(aCube):
            yellow_corners.algo(aCube)
        return