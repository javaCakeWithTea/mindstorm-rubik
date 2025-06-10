import unittest
import cube
import numpy as np
import Solvers.yellow_cross as yellow_cross
import Solvers.second_layer as second_layer
import Solvers.white_corners as white_corners
import Solvers.nerd as nerd
import Solvers.yellow_edges as yellow_edges
import Solvers.yellow_corners as yellow_corners
import Solvers.orientate_corners as orientate_corners

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

class OrientateCornersTest(unittest.TestCase): 


    def test_corners_orientated_1(self):
        ## LF in place.
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
        yellow_corners.yellow_corners.solve(aCube)
        self.assertTrue(yellow_corners.yellow_corners.yellowCornersComplete(aCube))
        orientate_corners.orientate_corners.solve(aCube)
        self.assertTrue(orientate_corners.orientate_corners.complete(aCube))

    def test_corners_orientated_2(self):
        ## LF in place.
        aCube = getDefaultCube()
        aCube.rotateSide("u")
        aCube.rotateSide("d")
        aCube.rotateSide("r")
        aCube.rotateSide("b")
        nerd.Nerd.solve(aCube)
        white_corners.white_corners.solve(aCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(aCube))
        second_layer.second_layer.solve(aCube)
        yellow_cross.yellow_cross.solve(aCube)
        self.assertTrue(yellow_cross.yellow_cross.yellowCrossComplete(aCube))
        yellow_edges.yellow_edges.solve(aCube)
        self.assertTrue(yellow_edges.yellow_edges.yellowEdgesComplete(aCube))
        yellow_corners.yellow_corners.solve(aCube)
        self.assertTrue(yellow_corners.yellow_corners.yellowCornersComplete(aCube))
        orientate_corners.orientate_corners.solve(aCube)
        self.assertTrue(orientate_corners.orientate_corners.complete(aCube))
        

