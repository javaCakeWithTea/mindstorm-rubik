import unittest
import Solvers.second_layer as second_layer
import cube
import numpy as np
import Solvers.nerd as nerd
import Solvers.white_corners as white_corners

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

class SecondLayerTest(unittest.TestCase): 

    def testRedFaceLeftAlgo(self):
        defaultCube = getDefaultCube()
        defaultCube.f[1,0] = "blue"
        defaultCube.f[2,1] = "red"
        defaultCube.l[1,2] = "orange"
        defaultCube.d[0,1] = "green"
        defaultCube.centreOnFace("f")
        second_layer.second_layer.rightAlgorithm(defaultCube)
        self.assertEqual(defaultCube.f[1,0],"red")
        self.assertEqual(defaultCube.l[1,2],"green")

    def testRedFaceRightAlgo(self):
        defaultCube = getDefaultCube()
        defaultCube.f[1,2] = "green"
        defaultCube.f[2,1] = "red"
        defaultCube.r[1,0] = "orange"
        defaultCube.d[0,1] = "blue"
        defaultCube.centreOnFace("f")
        second_layer.second_layer.leftAlgorithm(defaultCube)
        self.assertEqual(defaultCube.f[1,2],"red")
        self.assertEqual(defaultCube.r[1,0],"blue")

    def testLFaceRightAlgo(self):
        defaultCube = getDefaultCube()
        defaultCube.l[1,0],"blue"
        defaultCube.b[1,2],"red"
        defaultCube.l[2,1] = "green"
        defaultCube.d[1,0] = "orange"
        defaultCube.centreOnFace("l")
        second_layer.second_layer.rightAlgorithm(defaultCube)
        self.assertEqual(defaultCube.l[1,0],"green")
        self.assertEqual(defaultCube.b[1,2],"orange")

    def testLFaceLeftAlgo(self):
        defaultCube = getDefaultCube()
        defaultCube.l[1,2],"blue"
        defaultCube.f[1,0],"yellow"
        defaultCube.l[2,1] = "green"
        defaultCube.d[1,0] = "red"
        defaultCube.centreOnFace("l")
        second_layer.second_layer.rightAlgorithm(defaultCube)
        self.assertEqual(defaultCube.l[1,2],"green")
        self.assertEqual(defaultCube.f[1,0],"red")

    def testSolveSecondLayer1(self):
        defaultCube = getDefaultCube()
        defaultCube.l[1,2],"blue"
        defaultCube.f[1,0],"yellow"
        defaultCube.l[2,1] = "green"
        defaultCube.d[1,0] = "red"
        defaultCube.centreOnFace("l")
        second_layer.second_layer.matchFace(defaultCube)
        self.assertEqual(defaultCube.l[1,2],"green")
        self.assertEqual(defaultCube.f[1,0],"red")
        self.assertTrue(second_layer.second_layer.secondLayerComplete(defaultCube))
        

    def testSolveSecondLayer2(self):
        defaultCube = getDefaultCube()
        defaultCube.r[1,2],"red"
        defaultCube.b[1,0],"yellow"
        defaultCube.r[2,1] = "blue"
        defaultCube.d[1,2] = "orange"
        defaultCube.centreOnFace("l")
        second_layer.second_layer.matchFace(defaultCube)
        self.assertEqual(defaultCube.r[1,2],"blue")
        self.assertEqual(defaultCube.b[1,0],"orange")
        self.assertTrue(second_layer.second_layer.secondLayerComplete(defaultCube))

    def testSolveSecondLayer3(self):
        ## Same as first one but has the other way so it needs to repeat the algo.
        defaultCube = getDefaultCube()
        defaultCube.l[1,2],"blue"
        defaultCube.f[1,0],"yellow"
        defaultCube.l[2,1] = "red"
        defaultCube.d[1,0] = "green"
        defaultCube.centreOnFace("l")
        second_layer.second_layer.matchFace(defaultCube)
        self.assertEqual(defaultCube.l[1,2],"green")
        self.assertEqual(defaultCube.f[1,0],"red")
        self.assertTrue(second_layer.second_layer.secondLayerComplete(defaultCube))

    def testInStatement(self):
        self.assertTrue("green" in ["red","blue","orange","green"])

    def testPopOutEdgesThatAreCorrect(self):
        ## This method should leave the cube with no correct edges in the middle layer.
        defaultCube = getDefaultCube()
        defaultCube.rotateSide("l")
        defaultCube.rotateSide("u")
        defaultCube.rotateSide("r")
        defaultCube.rotateSide("l")
        nerd.Nerd.solve(defaultCube)
        white_corners.white_corners.solve(defaultCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(defaultCube))
        second_layer.second_layer.popOutEdgesThatAreCorrect(defaultCube)   
        LSideOfF,FSideOfL,RSideOfF,FSideOfR,bottomSideF,bottomSideD = second_layer.second_layer.setValues(defaultCube)
        self.assertTrue("yellow" in [LSideOfF,FSideOfL])
        self.assertTrue("yellow" in [RSideOfF,FSideOfR])
        self.assertTrue("yellow" in [defaultCube.r[1,2],defaultCube.b[1,0]])
        self.assertTrue("yellow" in [defaultCube.l[1,0],defaultCube.b[1,2]])


    def testSolveComplex(self):
        defaultCube = getDefaultCube()
        defaultCube.rotateSide("l")
        defaultCube.rotateSide("u")
        defaultCube.rotateSide("r")
        defaultCube.rotateSide("l")
        nerd.Nerd.solve(defaultCube)
        white_corners.white_corners.solve(defaultCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(defaultCube))
        second_layer.second_layer.solve(defaultCube)
        print(defaultCube.f[1,0],defaultCube.f[1,2],defaultCube.l[1,0],defaultCube.l[1,2],defaultCube.r[1,0],defaultCube.r[1,2],defaultCube.b[1,0],defaultCube.b[1,2])
        self.assertTrue(second_layer.second_layer.secondLayerComplete(defaultCube))
        
    def testSolveComplex2(self):
        defaultCube = getDefaultCube()
        defaultCube.rotateSide("r")
        defaultCube.rotateSide("d")
        defaultCube.rotateSide("l")
        defaultCube.rotateSide("b")
        nerd.Nerd.solve(defaultCube)
        white_corners.white_corners.solve(defaultCube)
        self.assertTrue(white_corners.white_corners.whiteCornersComplete(defaultCube))
        second_layer.second_layer.solve(defaultCube)
        print(defaultCube.f[1,0],defaultCube.f[1,2],defaultCube.l[1,0],defaultCube.l[1,2],defaultCube.r[1,0],defaultCube.r[1,2],defaultCube.b[1,0],defaultCube.b[1,2])
        self.assertTrue(second_layer.second_layer.secondLayerComplete(defaultCube))


