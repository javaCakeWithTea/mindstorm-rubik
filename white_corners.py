class white_corners:
    ## This nerd has learnt to go from a white cross to a complete white face.
    @staticmethod
    def solve(cube):
        topLeft = cube.u[0,0] == "white"
        topRight = cube.u[0,2] == "white"
        bottomLeft = cube.u[2,0] == "white"
        bottomRight = cube.u[2,2] == "white"
        if not topLeft:
            cube.resetLabels()
            cube.centreOnFace("b")
            algo()
        elif not topRight:
            cube.resetLabels()
            cube.centreOnFace("r")
            algo()
        elif not bottomLeft:
            cube.resetLabels()
            cube.centreOnFace("l")
            algo()
        elif not bottomRight:
            cube.resetLabels()
            cube.centreOnFace("f")
            algo()

    def algo(cube):

    def isWhiteTileOnThisCorner(self,cube):
        
        case1 = cube.getattr(cube.labelF)[2,2] == "white"
        case2 = cube.getattr(cube.labelR)[2,0] == "white"
        case3 =



    