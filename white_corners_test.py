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

    def test_white_corners_complete_assertion(self):
        ## Solved cube should pass.
        aCube = getDefaultCube()
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))

    def test_can_get_from_white_cross_to_corners(self):
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))

        