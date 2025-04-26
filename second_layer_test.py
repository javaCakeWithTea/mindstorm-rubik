import unittest
import second_layer
import cube
import numpy as np

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


