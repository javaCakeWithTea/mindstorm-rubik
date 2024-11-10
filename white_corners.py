
class white_corners:
    ## This nerd has learnt to go from a white cross to a complete white face.

    ## There are three possibilities.
    ## 1. Correct corner is in place and in correct orientation.
    ## 2. Correct corner is in place and in wrong orientation.
    ## 3. Wrong white corner is in place.
    ## 4. Non-white corner is in place.

    ## Algo R'FRF' swaps the corners.
    @staticmethod
    def solve(cube):
        topLeftNeeded = {"white","green","orange"}
        topRightNeeded = {"white","blue","orange"}
        bottomLeftNeeded = {"white","green","red"}
        bottomRightNeeded = {"white","red","blue"}
        topLeftCorner = {cube.u[0,0],cube.l[0,0],cube.b[0,2]}
        topRightCorner = {cube.u[0,2],cube.r[0,2],cube.b[0,0]}
        bottomLeftCorner = {cube.u[2,0],cube.f[0,0],cube.l[0,2]}
        bottomRightCorner = {cube.u[2,2],cube.f[0,2],cube.r[0,0]}

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
        ## R' F R F' 
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("r")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("f")
        cube.rotateLabelledSide("f")
    

        







    