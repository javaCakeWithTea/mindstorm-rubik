import unittest
import cube
import numpy as np
import yellow_cross
import second_layer
import white_corners
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

class YellowCrossTest(unittest.TestCase): 


    def test_yellow_cross_complete_assertion_1(self):
        ## Solved cube should pass. line 2
        aCube = getDefaultCube()
        aCube.rotateSide("r")
        aCube.rotateSide("d")
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))

    def test_yellow_cross_complete_assertion_2(self):
        ## Solved cube should pass. l3
        aCube = getDefaultCube()
        aCube.rotateSide("d")
        aCube.rotateSide("d")
        aCube.rotateSide("f")
        aCube.rotateSide("u")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))

    def test_yellow_cross_complete_assertion_3(self):
        ## Solved cube should pass. line 1
        aCube = getDefaultCube()
        aCube.rotateSide("d")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("f")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        self.assertTrue(second_layer.second_layer.secondLayerComplete(aCube))
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))

    def test_yellow_cross_complete_assertion_4(self):
        ## Solved cube should pass. l1
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("r")
        aCube.rotateSide("r")
        aCube.rotateSide("l")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        self.assertTrue(second_layer.second_layer.secondLayerComplete(aCube))
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))

    def test_yellow_cross_complete_assertion_5(self):
        ## Solved cube should pass. dot
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("r")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        self.assertTrue(second_layer.second_layer.secondLayerComplete(aCube))
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
    
    def test_yellow_cross_complete_assertion_6(self):
        ## Solved cube should pass. l4
        aCube = getDefaultCube()
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("l")
        aCube.rotateSide("b")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        self.assertTrue(second_layer.second_layer.secondLayerComplete(aCube))
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))

    def test_yellow_cross_complete_assertion_7(self):
        ## Solved cube should pass. l2
        aCube = getDefaultCube()
        aCube.rotateSide("u")
        aCube.rotateSide("u")
        aCube.rotateSide("l")
        aCube.rotateSide("l")
        aCube.rotateSide("f")
        aCube.rotateSide("d")
        aCube.rotateSide("r")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        self.assertTrue(second_layer.second_layer.secondLayerComplete(aCube))
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))