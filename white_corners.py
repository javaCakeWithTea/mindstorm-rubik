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
    def solve(cube):
        ## First start by getting all the white corners an the non-white side of the cube. 
        ## Once they are here, the algorithm will not move these corners to the other side.

        cube.centreOnFace("f")
        white_corners.popCorner(cube)
        cube.centreOnFace("r")
        white_corners.popCorner(cube)
        cube.centreOnFace("b")
        white_corners.popCorner(cube)
        cube.centreOnFace("l")
        white_corners.popCorner(cube)

        ## Then orientate the correct corner over the position it needs to be and swap it in.
        cube.centreOnFace("f")
        white_corners.putCornerInPlace(cube)
        cube.centreOnFace("r")
        white_corners.putCornerInPlace(cube)
        cube.centreOnFace("b")
        white_corners.putCornerInPlace(cube)
        cube.centreOnFace("l")
        white_corners.putCornerInPlace(cube)

        return cube
    
    @staticmethod
    def isTopCornerWhite(cube):
        currentFront = cube.labelF
        if currentFront == "f":
            return cube.f[0,2] == "white" or cube.r[0,0] == "white" or cube.u[2,2] == "white"
        elif currentFront == "r":
            return cube.r[0,2] == "white" or cube.b[0,0] == "white" or cube.u[0,2] == "white"
        elif currentFront == "b":
            return cube.b[0,2] == "white" or cube.l[0,0] == "white" or cube.u[0,0] == "white"
        elif currentFront == "l":
            return cube.l[0,2] == "white" or cube.f[0,0] == "white" or cube.u[2,0] == "white"
        else:
            print("Something wrong!")
            return
    
    @staticmethod
    def isBottomCornerWhite(cube):
        currentFront = cube.labelF
        if currentFront == "f":
            return cube.f[2,2] == "white" or cube.r[2,0] == "white" or cube.d[0,2] == "white"
        elif currentFront == "r":
            return cube.r[2,2] == "white" or cube.b[2,0] == "white" or cube.d[2,2] == "white"
        elif currentFront == "b":
            return cube.b[2,2] == "white" or cube.l[2,0] == "white" or cube.d[2,0] == "white"
        elif currentFront == "l":
            return cube.l[2,2] == "white" or cube.f[2,0] == "white" or cube.d[0,0] == "white"
        else:
            print("Something wrong!")
            return
        
    @staticmethod
    def popCorner(cube):
        if white_corners.isTopCornerWhite(cube) and white_corners.isBottomCornerWhite(cube):
            while white_corners.isBottomCornerWhite(cube):
                cube.rotateSide("d")
        elif not white_corners.isTopCornerWhite(cube) and not white_corners.isBottomCornerWhite(cube):
            return
        white_corners.swapAlgo(cube) 

    @staticmethod
    def swapAlgo(cube):  
        ## Swaps the corner in the top and the bottom. 
        ## Keeps all bottom corners in bottom and top corners in top.
        ## Keeps all top corners in position.
        ## R' F R F' 
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("f")

    @staticmethod
    def putCornerInPlace(cube):
        currentFront = cube.labelF
        if currentFront == "f":
            while {cube.f[2,2],cube.r[2,0],cube.d[0,2]} != {"white","red","blue"}:
                cube.rotateSide("d")
            while cube.u[2,2] != "white" or cube.f[0,2] != "red" or cube.r[0,0] != "blue":
                white_corners.swapAlgo(cube)
        elif currentFront == "r":
            while {cube.r[2,2],cube.b[2,0],cube.d[2,2]} != {"white","blue","orange"}:
                cube.rotateSide("d")
            while cube.u[0,2] != "white" or cube.r[0,2] != "blue" or cube.b[0,0] != "orange":
                white_corners.swapAlgo(cube)
        elif currentFront == "b":
            while {cube.b[2,2],cube.l[2,0],cube.d[2,0]} != {"white","green","orange"}:
                cube.rotateSide("d")
            while cube.u[0,0] != "white" or cube.l[0,0] != "green" or cube.b[0,2] != "orange":
                white_corners.swapAlgo(cube)
        elif currentFront == "l":
            while {cube.l[2,2],cube.f[2,0],cube.d[0,0]} != {"white","green","red"}:
                cube.rotateSide("d")
            while cube.u[2,0] != "white" or cube.f[0,0] != "red" or cube.l[0,2] != "green":
                white_corners.swapAlgo(cube)
        else:
            print("Something wrong!")
            return
        

    @staticmethod
    def whiteCornersComplete(aCube):
        ##Checks if the white corners stage is complete.
        uFace = np.array([["any","white","any"],
            ["white","white","white"],
            ["any","white","any"]])
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

    

        







    