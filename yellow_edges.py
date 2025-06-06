import numpy as np
import cube

class yellow_edges:
    ## This nerd has learnt to go from a yellow cross solution to yellow edges solution.
    
    @staticmethod
    def yellowEdgesComplete(aCube:cube.Cube):
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
        
        if aCube == completeYellowEdges:
            return True
        else:
            return False
        
    @staticmethod
    def algo(aCube:cube.Cube):
        ## The algorithm that is repeated to gain the yellow cross on face 'd'.
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("d")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("r")
        aCube.rotateLabeledSide("d")
        return

    @staticmethod
    def solve(aCube:cube.Cube):
        ## Rotate d until the red edge lines up.
        while aCube.f[2,1] != "red":
            print("Rotating d to match up yellow edge with red face.")
            aCube.rotateSide("d")
        
        print("Red edge matched.")
        print(aCube.f)

        orderOfYellowEdges = [aCube.l[2,1],aCube.b[2,1],aCube.r[2,1]]
        print(orderOfYellowEdges)

        if orderOfYellowEdges == ["green","orange","blue"]:
            ## Already in correct order.
            print("Already correct.")
            return
        if orderOfYellowEdges[0] == "green":
            ## Swap r and b adjacent faces. Green is in place.
            print("Swapping 1: "+orderOfYellowEdges[1]+orderOfYellowEdges[2])
            aCube.centreOnFace("l")
            yellow_edges.algo(aCube)
            return
        if orderOfYellowEdges[1] == "orange":
            ## Swap opposite faces l and r.
            print("Swapping l and r only.")
            aCube.centreOnFace("f")
            aCube.rotateSide("d")
            yellow_edges.algo(aCube)
            aCube.centreOnFace("b")
            yellow_edges.algo(aCube)
            print(aCube.l, aCube.b, aCube.r)
            return
        if orderOfYellowEdges[2] == "blue":
            ## Swap l and b adjacent faces. Blue is in place.
            print("Swapping l and b only.")
            aCube.centreOnFace("f")
            yellow_edges.algo(aCube)
            return
        
        ## None of the other faces match up. 2 possibilities?!
        if orderOfYellowEdges == ["blue","green","orange"]:
            ## Swap l and b, then swap r and b. 
            print("Swap l and b then r and b")
            aCube.centreOnFace("f")
            yellow_edges.algo(aCube)
            aCube.centreOnFace("l")
            yellow_edges.algo(aCube)
            return
        if orderOfYellowEdges == ["orange","blue","green"]:
            ## Swap r and b, then swap l and b.
            print("Swap r and b then l and b.")
            aCube.centreOnFace("l")
            yellow_edges.algo(aCube)
            aCube.centreOnFace("f")
            yellow_edges.algo(aCube)
            return