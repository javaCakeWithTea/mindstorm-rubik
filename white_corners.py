import numpy as np
import cube

class white_corners:
    ## This nerd has learnt to go from a white cross to a complete white face.

    ## There are three possibilities.
    ## 1. Correct corner is in place and in correct orientation.
    ## 2. Correct corner is in place and in wrong orientation.
    ## 3. Wrong white corner is in place.
    ## 4. Non-white corner is in place.
    @staticmethod
    def solve(cube:cube.Cube):
        ## First start by getting all the white corners on the non-white side of the cube. 
        ## Once they are here, the algorithm will not move these corners to the other side.
        white_corners.removeWhiteCornersFromU(cube)

        ## Then orientate the correct corner over the position it needs to be and swap it in.
        white_corners.putCornersInPlace(cube)
        return cube
    
    @staticmethod
    def removeWhiteCornersFromU(cube:cube.Cube):
        ## R' D' R D
        if cube.f[0,2] == "white" or cube.r[0,0] == "white" or cube.u[2,2] == "white":
            while cube.f[2,2] == "white" or cube.r[2,0] == "white" or cube.d[0,2] == "white":
                cube.rotateSide("d")
            white_corners.swapAlgo(cube)
        if cube.r[0,2] == "white" or cube.b[0,0] == "white" or cube.u[0,2] == "white":
            while cube.r[2,2] == "white" or cube.b[2,0] == "white" or cube.d[2,2] == "white":
                cube.rotateSide("d")
            cube.centreOnFace("r")    
            white_corners.swapAlgo(cube)
        if cube.b[0,2] == "white" or cube.l[0,0] == "white" or cube.u[0,0] == "white":
            while cube.b[2,2] == "white" or cube.l[2,0] == "white" or cube.d[2,0] == "white":
                cube.rotateSide("d")
            cube.centreOnFace("b") 
            white_corners.swapAlgo(cube)
        if cube.l[0,2] == "white" or cube.f[0,0] == "white" or cube.u[2,0] == "white":
            while cube.l[2,2] == "white" or cube.f[2,0] == "white" or cube.d[0,0] == "white":
                cube.rotateSide("d")
            cube.centreOnFace("l") 
            white_corners.swapAlgo(cube)
        return

    @staticmethod
    def swapAlgo(cube:cube.Cube):  
        ## Swaps the corner in the top and the bottom. 
        ## Keeps all bottom corners in bottom and top corners in top.
        ## Keeps all top corners in position.
        ## R' F R F' 
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("d")
        return

    @staticmethod
    def putCornersInPlace(cube:cube.Cube):
        cube.centreOnFace("f")
        while sorted([cube.f[2,2],cube.r[2,0],cube.d[0,2]]) != sorted(["blue","red","white"]):
            cube.rotateSide("d")
            print(1)
        cube.centreOnFace("r")
        while sorted([cube.r[2,2],cube.b[2,0],cube.d[2,2]]) != sorted(["blue","orange","white"]): 
            cube.rotateSide("d")
            print(2)
        cube.centreOnFace("b")
        while sorted([cube.b[2,2],cube.l[2,0],cube.d[2,0]]) != ["green","orange","white"]:
            cube.rotateSide("d")
            print(3)
        cube.centreOnFace("l")
        while sorted([cube.l[2,2],cube.f[2,0],cube.d[0,0]]) != ["green","red","white"]:
            cube.rotateSide("d")
            print(4)
        return    

    @staticmethod
    def whiteCornersComplete(aCube:cube.Cube):
        ##Checks if the white corners stage is complete.
        uFace = np.array([["white","white","white"],
            ["white","white","white"],
            ["white","white","white"]])
        fFace = np.array([["red","red","red"],
            ["any","red","any"],
            ["any","any","any"]])
        rFace = np.array([["blue","blue","blue"],
            ["any","blue","any"],
            ["any","any","any"]])
        lFace = np.array([["green","green","green"],
            ["any","green","any"],
            ["any","any","any"]])
        bFace = np.array([["orange","orange","orange"],
            ["any","orange","any"],
            ["any","any","any"]])
        dFace = np.array([["any","any","any"],
            ["any","yellow","any"],
            ["any","any","any"]])
        
        completeWhiteCorners = cube.Cube(fFace,uFace,lFace,rFace,bFace,dFace)
        
        if aCube == completeWhiteCorners:
            return True
        else:
            return False

    

        







    