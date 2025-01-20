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

    def testOrangeFaceExample(self):
        defaultCube = getDefaultCube()
        defaultCube.b[2,1] = "orange"
        defaultCube.d[2,1] = "blue"
        defaultCube.b[1,0] = "green"
        defaultCube.r[1,2] = "orange"
        defaultCube.centreOnFace("b")
        second_layer.second_layer.rightAlgorithm(defaultCube)
        self.assertEquals(defaultCube.b[1,0],"orange")
        self.assertEquals(defaultCube.r[1,2],"blue")

