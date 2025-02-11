import numpy as np
import cube

class second_layer:
    ## This nerd has learnt to go from a white corners solution to complete second layer.

    @staticmethod
    def solve(cube:cube.Cube):
        
        return cube
    
    @staticmethod
    def leftAlgorithm(cube:cube.Cube):

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
    def rightAlgorithm(cube:cube.Cube):

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
    def matchFace(cube:cube.Cube):
        desiredColourF = cube.__dict__(cube.labelF)[1,1]
        desiredColourL = cube.__dict__(cube.labelL)[1,2]
        desiredColourR = cube.__dict__(cube.labelR)[1,0]
        leftSideF = cube.__dict__(cube.labelF)[1,0]
        leftSideL = cube.__dict__(cube.labelL)[1,2]
        rightSideF = cube.__dict__(cube.labelF)[1,2]
        rightSideR = cube.__dict__(cube.labelR)[1,0]

        bottomSideF = cube.__dict__(cube.labelF)[2,1]
        if cube.labelF == "f":
            bottomSideD = cube.d[0,1]
        elif cube.labelF == "r":
            bottomSideD = cube.d[1,2]
        elif cube.labelF == "b":
            bottomSideD = cube.d[2,1]
        elif cube.labelF == "l":
            bottomSideD = cube.d[1,0]
        
        for face in ["f","r","b","l"]:
            ## Check if any edges can be inserted on this face.
            cube.centreOnFace(face)
        
            ## First chack if the pieces are in place but in wrong orientation.
            if leftSideF == desiredColourL and leftSideL == desiredColourF:
                ## Left algo, incorrect position. Already in place.
                second_layer.leftAlgorithm(cube)
                second_layer.leftAlgorithm(cube)
            if rightSideF == desiredColourR and rightSideR == desiredColourF:
                ## Right algo, incorrect position. Already in place.
                second_layer.rightAlgorithm(cube)
                second_layer.rightAlgorithm(cube)

            for i in range(4):
                ## Check each of the bottom edges for a match.
                if (leftSideF == desiredColourF and leftSideL == desiredColourL) or (rightSideF == desiredColourF and rightSideR == desiredColourR):
                    continue
                if bottomSideF == desiredColourF and bottomSideD == desiredColourL:
                    ## Left algo, correct position.
                    second_layer.leftAlgorithm(cube)
                if bottomSideF == desiredColourL and bottomSideD == desiredColourF:
                    ## Left algo, incorrect position.
                    second_layer.leftAlgorithm(cube)
                    second_layer.leftAlgorithm(cube)
                    second_layer.leftAlgorithm(cube)
                if bottomSideF == desiredColourF and bottomSideD == desiredColourR:
                    ## Right algo, correct position.
                    second_layer.rightAlgorithm(cube)
                if bottomSideF == desiredColourR and bottomSideD == desiredColourF:
                    ## Right algo, incorrect position.
                    second_layer.rightAlgorithm(cube)
                    second_layer.rightAlgorithm(cube)
                    second_layer.rightAlgorithm(cube)

                ## Rotate to the next one.
                cube.rotateSide("d")
        
        