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
        if isWhiteTileOnThisCorner()

    @staticmethod
    def ifOnCornerMove(cube):
        ## Moves the corner tile to correct position if there otherwise returns None.
        case1 = cube.getattr(cube.labelF)[2,2] == "white"
        case2 = cube.getattr(cube.labelR)[2,0] == "white"
        if cube.labelF == "f":
            case3 = cube.d[0,2] == "white"
        elif cube.labelF == "r":
            case3 = cube.d[2,2] == "white"
        elif cube.labelF == "b":
            case3 = cube.d[2,0] == "white"
        elif cube.labelF == "l":
            case3 = cube.d[0,0] == "white"

        if case1:
            return algo1(cube)
        elif case2:
            return algo2(cube)
        elif case3:
            return algo3(cube)
        else:
            return None




    