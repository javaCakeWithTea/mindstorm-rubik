import unittest
import cube
import numpy as np
import yellow_cross
import second_layer
import white_corners
import nerd
import yellow_edges

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

class YellowEdgesTest(unittest.TestCase): 


    def test_yellow_edges_complete_assertion_1(self):
        ## Swapping l and b only.
        aCube = getDefaultCube()
        aCube.rotateSide("r")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))

    def test_yellow_edges_complete_assertion_2(self):
        ## Swapping l and r only.
        aCube = getDefaultCube()
        aCube.rotateSide("b")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))

    def test_yellow_edges_complete_assertion_3(self):
        ## Swapping r and b then l and b.
        aCube = getDefaultCube()
        aCube.rotateSide("b")
        aCube.rotateSide("u")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))

    def test_yellow_edges_complete_assertion_4(self):
        ## Swapping l and b then r and b.
        aCube = getDefaultCube()
        aCube.rotateSide("b")
        aCube.rotateSide("u")
        aCube.rotateSide("u")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))

    def test_yellow_edges_complete_assertion_5(self):
        ## Swapping r and b only.
        aCube = getDefaultCube()
        aCube.rotateSide("b")
        aCube.rotateSide("l")
        aCube.rotateSide("u")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))