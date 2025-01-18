import unittest
import white_corners
import cube
import numpy as np
import nerd

def getDefaultCube():
    ## Constructor doesn't necessarily produce a new instance?
    defaultCube = cube.Cube()
    defaultCube.f=np.full((3,3),"red",dtype="U6")
    defaultCube.u=np.full((3,3),"white",dtype="U6")
    defaultCube.l=np.full((3,3),"green",dtype="U6")
    defaultCube.r=np.full((3,3),"blue",dtype="U6")
    defaultCube.b=np.full((3,3),"orange",dtype="U6")
    defaultCube.d=np.full((3,3),"yellow",dtype="U6")
    return defaultCube

class WhiteCornersTest(unittest.TestCase): 

    def test_white_corners_complete_assertion_1(self):
        ## Solved cube should pass.
        aCube = getDefaultCube()
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corners_complete_assertion_2(self):
        ## Solved cube should pass.
        aCube = getDefaultCube()
        aCube.rotateSide("d")
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corners_complete_assertion_neg_1(self):
        ## Solved cube should pass.
        aCube = getDefaultCube()
        aCube.rotateSide("r")
        self.assertFalse(white_corners.white_corners.whiteCornersComplete(aCube))


    def test_pop_out_all_corners_from_default(self):
        aCube = getDefaultCube()
        white_corners.white_corners.removeWhiteCornersFromU(aCube)
        result1 = aCube.u[0,0] != "white" and aCube.u[0,2] != "white" and aCube.u[2,0] != "white" and aCube.u[2,2] != "white"
        self.assertTrue(result1) ## Check all the top faces of U corners are not white.
        result2 = aCube.u[0,1] == "white" and aCube.u[1,0] == "white" and aCube.u[1,2] == "white" and aCube.u[2,1] == "white" and aCube.u[1,1]
        self.assertTrue(result2) ## Check the white cross is intact.
        result3 = aCube.f[0,0] != "white" and aCube.f[0,2] != "white" and aCube.r[0,0] != "white" and aCube.r[0,2] != "white" and aCube.b[0,0] != "white" and aCube.b[0,2] != "white" and aCube.l[0,0] != "white" and aCube.l[0,2] != "white"
        self.assertTrue(result3) ## Check that the peripherals of the top are not white on the corners.

    def test_popped_corners_can_be_added_back(self):
        aCube = getDefaultCube()
        white_corners.white_corners.removeWhiteCornersFromU(aCube)
        print([aCube.f[2,2],aCube.r[2,0],aCube.d[0,2]])
        print([aCube.r[2,2],aCube.b[2,0],aCube.d[2,2]])
        print([aCube.b[2,2],aCube.l[2,0],aCube.d[2,0]])
        print([aCube.l[2,2],aCube.f[2,0],aCube.d[0,0]])

    def test_swap_algo_1(self):
        aCube = getDefaultCube()
        white_corners.white_corners.swapAlgo(aCube)
        ## Cube with f corner swapped out with none white.
        aCube.centreOnFace("f")
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        ## Requires 5 swap algorithms.
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_swap_algo_2(self):
        aCube = getDefaultCube()
        aCube.centreOnFace("r")
        white_corners.white_corners.swapAlgo(aCube)

        ## Cube with f corner swapped out with none white.
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        ## Requires 5 swap algorithms.
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_swap_algo_3(self):
        aCube = getDefaultCube()
        aCube.centreOnFace("b")
        white_corners.white_corners.swapAlgo(aCube)
        ## Cube with f corner swapped out with none white.
        aCube.centreOnFace("b")
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        ## Requires 5 swap algorithms.
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

        