import unittest
import Solvers.white_corners as white_corners
import cube
import numpy as np
import Solvers.nerd as nerd

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
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.putCornersInPlace(aCube)
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corners_complex(self):
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("u")
        aCube.rotateSide("r")
        aCube.rotateSide("d")
        nerd.Nerd.solve(aCube)
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_1(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("d")
        aCube.rotateSide("f")
        aCube.rotateSide("f")
        aCube.rotateSide("f")
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_2(self):
        aCube = getDefaultCube()
        aCube.rotateSide("r")
        aCube.rotateSide("d")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_3(self):
        aCube = getDefaultCube()
        aCube.rotateSide("b")
        aCube.rotateSide("d")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_4(self):
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_5(self):
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("d")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_white_corner_solve_6(self):
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        aCube.rotateSide("r")
        aCube.rotateSide("d")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_swap_algo_1(self):
        aCube = getDefaultCube()
        white_corners.white_corners.swapAlgo(aCube)
        self.assertFalse(white_corners.white_corners.whiteCornersComplete(aCube))
        ## Cube with f corner swapped out with none white.
        aCube.centreOnFace("f")
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        ## Requires 5 swap algorithms.
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))
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

    def test_swap_algo_4(self):
        aCube = getDefaultCube()
        aCube.centreOnFace("l")
        white_corners.white_corners.swapAlgo(aCube)
        ## Cube with f corner swapped out with none white.
        aCube.centreOnFace("l")
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        white_corners.white_corners.swapAlgo(aCube)
        ## Requires 5 swap algorithms.
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

        