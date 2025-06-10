import numpy as np
import cube

class yellow_cross:
    ## This nerd has learnt to go from a white corners solution to complete second layer.
    
    @staticmethod
    def yellowCrossComplete(aCube:cube.Cube):
        ##Checks if the yellow cross stage is complete.
        completeYellowCross = cube.Cube()
        completeYellowCross.u = np.full([3,3],"any",dtype="U6")
        completeYellowCross.f = np.full([3,3],"any",dtype="U6")
        completeYellowCross.r = np.full([3,3],"any",dtype="U6")
        completeYellowCross.l = np.full([3,3],"any",dtype="U6")
        completeYellowCross.b = np.full([3,3],"any",dtype="U6")
        completeYellowCross.d = np.array([
            ["any","yellow","any"],
            ["yellow","yellow","yellow"],
            ["any","yellow","any"]])
        
        if aCube == completeYellowCross:
            return True
        else:
            return False
        
    @staticmethod
    def algo(aCube:cube.Cube):
        ## The algorithm that is repeated to gain the yellow cross on face 'd'.
        aCube.rotateLabeledSide("f")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("l")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("f")
        aCube.rotateLabeledSide("f")
        aCube.rotateLabeledSide("f")

    @staticmethod
    def solve(aCube:cube.Cube):
        if (aCube.d[0,1] != "yellow") and (aCube.d[1,0] != "yellow") and (aCube.d[1,2] !="yellow") and (aCube.d[2,1] !="yellow"):
            print("dot")
            print(aCube.d)
            ## Yellow dot. Three times the algo.
            aCube.centreOnFace("f")
            yellow_cross.algo(aCube)
            aCube.centreOnFace("b")
            yellow_cross.algo(aCube)
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[0,1] != "yellow") and (aCube.d[2,1] != "yellow"):
            print("line 1")
            print(aCube.d)
            ## Permutation 1 of yellow line.
            aCube.centreOnFace("f")
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[1,0] != "yellow") and (aCube.d[1,2] != "yellow"):
            print("line 2")
            print(aCube.d)
            ## Permutation 2 of yellow line.
            aCube.centreOnFace("l")
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[1,0] != "yellow") and (aCube.d[0,1] != "yellow"):
            print("l1")
            print(aCube.d)
            ## Permutation 1 of yellow L. Two times.
            aCube.centreOnFace("f")
            yellow_cross.algo(aCube)
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[0,1] != "yellow") and (aCube.d[1,2] != "yellow"):
            print("l2")
            print(aCube.d)
            ## Permutation 2 of yellow L. Two times.
            aCube.centreOnFace("r")
            yellow_cross.algo(aCube)
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[1,2] != "yellow") and (aCube.d[2,1] != "yellow"):
            print("l3")
            print(aCube.d)
            ## Permutation 3 of yellow L. Two times.
            aCube.centreOnFace("b")
            yellow_cross.algo(aCube)
            yellow_cross.algo(aCube)
            print(aCube.d)
            return
        if (aCube.d[1,0] != "yellow") and (aCube.d[2,1] != "yellow"):
            print("l4")
            print(aCube.d)
            ## Permutation 4 of yellow L. Two times.
            aCube.centreOnFace("l")
            yellow_cross.algo(aCube)
            yellow_cross.algo(aCube)
            print(aCube.d)
            return