import numpy as np
import cube

class orientate_corners:
    ## This nerd has learnt to go from a yellow cross solution to yellow edges solution.
    
    @staticmethod
    def complete(aCube:cube.Cube):
        ##Checks if the cube is complete.
        complete = cube.Cube()
        
        if (aCube == complete):
            return True
        else:
            return False
        
    @staticmethod
    def algo(aCube:cube.Cube):
        ## The algorithm that is repeated.
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("u")
        aCube.rotateSide("u")
        aCube.rotateSide("u")
        aCube.rotateSide("r")
        aCube.rotateSide("u")
        return

    @staticmethod
    def solve(aCube:cube.Cube):
        orientate_corners.itterate(aCube)
        print("All orientated ok.")
        return

    @staticmethod
    def itterate(aCube:cube.Cube):
        while not np.array_equal(aCube.d,np.full((3,3),"yellow")):
            if aCube.d[2,2] == "yellow":
                print("Rotate 'd' until another bad corner is found.")
                aCube.rotateSide("d")
            else:
                print("Found new badly orientated corner.")
                while aCube.d[2,2] != "yellow":
                    print("Executing algo unitl corner is arranged ok.")
                    print(aCube.b)
                    orientate_corners.algo(aCube)
                    orientate_corners.algo(aCube)
                    print(aCube.b)
        ## Orientated correctly.
        while aCube.f[2,1] != "red":
            ## Re-arranging yellow face to complete.
            print("Rotating 'd'.")
            aCube.rotateSide("d")
            print(aCube.d)
        return 
