import numpy as np
import cube

class second_layer:
    ## This nerd has learnt to go from a white corners solution to complete second layer.


    @staticmethod
    def solve(cube:cube.Cube):
        second_layer.popOutEdgesThatAreCorrect(cube)
        second_layer.addThemIn(cube)
        return cube
    
    @staticmethod
    def secondLayerComplete(aCube:cube.Cube):
        ##Checks if the second layer stage is complete.
        completeSecondLayer = cube.Cube()
        completeSecondLayer.u = np.array([["white","white","white"],
            ["white","white","white"],
            ["white","white","white"]])
        completeSecondLayer.f = np.array([["red","red","red"],
            ["red","red","red"],
            ["any","any","any"]])
        completeSecondLayer.r = np.array([["blue","blue","blue"],
            ["blue","blue","blue"],
            ["any","any","any"]])
        completeSecondLayer.l = np.array([["green","green","green"],
            ["green","green","green"],
            ["any","any","any"]])
        completeSecondLayer.b = np.array([["orange","orange","orange"],
            ["orange","orange","orange"],
            ["any","any","any"]])
        completeSecondLayer.d = np.array([["any","any","any"],
            ["any","yellow","any"],
            ["any","any","any"]])
        
        
        if aCube == completeSecondLayer:
            return True
        else:
            return False
    
    @staticmethod
    def rightAlgorithm(cube:cube.Cube):

        ## |0|0|0|
        ## |X|0|_|
        ## |_|Y|_|
    
        ##DLD'L'D'F'DF
        ##DLDDDLLLDDDFFFDF
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("l")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("f")
        return
    
    @staticmethod
    def leftAlgorithm(cube:cube.Cube):

        ## |0|0|0|
        ## |_|0|X|
        ## |_|Y|_|

        ##D'R'DRDFD'F'
        ##DDDRRRDRDFDDDFFF
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("r")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("d")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        cube.rotateLabeledSide("f")
        return
    
    @staticmethod
    def popOutEdgesThatAreCorrect(cube:cube.Cube):
        ## Checks all the edges and pops them out if they are the right colours.
        ## Should result in all the colours being wrong in the middle.
        ## Now thye shold be ready to be put back in.
        
        for face in ["f","r","b","l"]:
            cube.centreOnFace(face)
            print("Checking face:" + face)
            print(cube.__dict__[cube.labelF])
            LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)
        
            if "yellow" not in [LSideOfF,FSideOfL]:
                print("Left side is a correct edge, get it out!")
                print("Edge is:" + LSideOfF + " " + FSideOfL)
                ## Edge should be popped out.
                for i in range(4):
                    if "yellow" in [bottomSideD,bottomSideF]:
                        print("Right algo.")
                        second_layer.rightAlgorithm(cube)
                        LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)
                        print("Edge now:" + LSideOfF + " " + FSideOfL)
                        break
                    else:
                        cube.rotateSide("d")
                        print("Rotating d!")
                        LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)
            if "yellow" not in [RSideOfF,FSideOfR]:
                print("Right side is a correct edge, get it out!")
                print("Edge is:" + RSideOfF + " " + FSideOfR)
                ## Edge should be popped out.
                for i in range(4):
                    if "yellow" in [bottomSideD,bottomSideF]:
                        print("Left algo.")
                        second_layer.leftAlgorithm(cube)
                        LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)
                        print("Edge is:" + RSideOfF + " " + FSideOfR)
                        break
                    else:
                        cube.rotateSide("d")
                        print("Rotating d!")
                        LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)

    @staticmethod
    def addThemIn(cube:cube.Cube):
        ## Checks all the faces and adds the corners in on this face if there is a match.

        while not second_layer.secondLayerComplete(cube):
            for face in ["f","r","b","l"]:
                cube.centreOnFace(face)
                print("Checking face:" + face)
                print(cube.__dict__[cube.labelF])
                desiredColourF = cube.__dict__[cube.labelF][1,1]
                desiredColourL = cube.__dict__[cube.labelL][1,1]
                desiredColourR = cube.__dict__[cube.labelR][1,1]
                LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.setValues(cube)

            
                if bottomSideF == desiredColourF:
                    
                    if (bottomSideD == desiredColourL):
                        ## Use right algorithm to insert the edge.
                        second_layer.rightAlgorithm(cube)
                    if (bottomSideD == desiredColourR):
                        ## Use left algorithm to insert the edge.
                        second_layer.leftAlgorithm(cube)

                if bottomSideD == desiredColourF:
                    if (bottomSideF == desiredColourL):
                        ## Use right algorithm to orientate then insert the edge.
                        second_layer.rightAlgorithm(cube)
                        second_layer.rightAlgorithm(cube)
                        cube.rotateSide("d")
                        cube.rotateSide("d")
                        second_layer.rightAlgorithm(cube)
                    if (bottomSideF == desiredColourR):
                        ## Use left algorithm to orientate then insert the edge.
                        second_layer.leftAlgorithm(cube)
                        second_layer.leftAlgorithm(cube)
                        cube.rotateSide("d")
                        cube.rotateSide("d")
                        second_layer.leftAlgorithm(cube)

            cube.rotateSide("d")
                    



    @staticmethod
    def setValues(cube:cube.Cube):
        LSideOfF = cube.__dict__[cube.labelF][1,0]
        FSideOfL = cube.__dict__[cube.labelL][1,2]
        RSideOfF = cube.__dict__[cube.labelF][1,2]
        FSideOfR = cube.__dict__[cube.labelR][1,0]

        bottomSideF = cube.__dict__[cube.labelF][2,1]
        if cube.labelF == "f":
            bottomSideD = cube.d[0,1]
        elif cube.labelF == "r":
            bottomSideD = cube.d[1,2]
        elif cube.labelF == "b":
            bottomSideD = cube.d[2,1]
        elif cube.labelF == "l":
            bottomSideD = cube.d[1,0]

        return LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD
        
        