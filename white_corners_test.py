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

    def test_can_get_from_white_cross_to_corners(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(white_corners.white_corners.solve(aCube)))

    def test_can_get_rid_of_all_white_corners_from_U_1(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.removeWhiteCornersFromU(aCube)
        self.assertFalse(aCube.f[0,2] == "white" or aCube.r[0,0] == "white" or aCube.u[2,2] == "white" or aCube.r[0,2] == "white" or aCube.b[0,0] == "white" or aCube.u[0,2] == "white" or aCube.b[0,2] == "white" or aCube.l[0,0] == "white" or aCube.u[0,0] == "white" or aCube.l[0,2] == "white" or aCube.f[0,0] == "white" or aCube.u[2,0] == "white")
        
    def test_can_get_rid_of_all_white_corners_from_U_2(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("b")
        aCube.rotateSide("r")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.removeWhiteCornersFromU(aCube)
        self.assertFalse(aCube.f[0,2] == "white" or aCube.r[0,0] == "white" or aCube.u[2,2] == "white" or aCube.r[0,2] == "white" or aCube.b[0,0] == "white" or aCube.u[0,2] == "white" or aCube.b[0,2] == "white" or aCube.l[0,0] == "white" or aCube.u[0,0] == "white" or aCube.l[0,2] == "white" or aCube.f[0,0] == "white" or aCube.u[2,0] == "white")

    def test_swap_algo_1(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("f")
        aCube.rotateSide("f")
        aCube.rotateSide("f")
        ## Cube with f corner swapped out with none white.
        aCube.centreOnFace("f")
        white_corners.white_corners.swapAlgo(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(white_corners.white_corners.solve(aCube)))

        