import unittest
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

class TestCubeMethods(unittest.TestCase): 
    def test_rotate_u_twice(self):
        theCube6 = getDefaultCube()
        theCube6.rotateSide("u")
        self.assertTrue(np.array_equal(theCube6.f,np.array([["blue","blue","blue"],
                                                ["red","red","red"],
                                                ["red","red","red"]],dtype="U6")))
        theCube6.rotateSide("u")
        self.assertTrue(np.array_equal(theCube6.f,np.array([["orange","orange","orange"],
                                                ["red","red","red"],
                                                ["red","red","red"]],dtype="U6"))) 
        
    def test_rotate_r_twice(self):
        theCube7 = getDefaultCube()
        theCube7.rotateSide("r")
        theCube7.rotateSide("r")
        self.assertTrue(np.array_equal(theCube7.f,np.array([["red","red","orange"],
                                                ["red","red","orange"],
                                                ["red","red","orange"]],dtype="U6")))   

    def test_rotate_side_d(self):
        aCube = getDefaultCube()
        aCube.l[2] = np.array(["1","2","3"],dtype="U6")
        aCube.f[2] = np.array(["4","5","6"],dtype="U6")
        aCube.r[2] = np.array(["7","8","9"],dtype="U6")
        aCube.b[2] = np.array(["10","11","12"],dtype="U6")
        aCube.d = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("d")
        self.assertTrue(np.array_equal(aCube.l[2],np.array(["10","11","12"],dtype="U6")) and
                        np.array_equal(aCube.f[2],np.array(["1","2","3"],dtype="U6")) and
                        np.array_equal(aCube.r[2],np.array(["4","5","6"],dtype="U6")) and
                        np.array_equal(aCube.b[2],np.array(["7","8","9"],dtype="U6"))) 
        self.assertTrue(np.array_equal(aCube.d,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        
    def test_rotate_side_f(self):
        aCube = getDefaultCube()
        aCube.l[:,2] = np.array(["12","11","10"],dtype="U6")
        aCube.u[2] = np.array(["1","2","3"],dtype="U6")
        aCube.r[:,0] = np.array(["4","5","6"],dtype="U6")
        aCube.d[0] = np.array(["9","8","7"],dtype="U6")
        aCube.f = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("f")
        self.assertTrue(np.array_equal(aCube.l[:,2],np.array(["9","8","7"],dtype="U6")) and
                        np.array_equal(aCube.u[2],np.array(["10","11","12"],dtype="U6")) and
                        np.array_equal(aCube.r[:,0],np.array(["1","2","3"],dtype="U6")) and
                        np.array_equal(aCube.d[0],np.array(["6","5","4"],dtype="U6")))
        self.assertTrue(np.array_equal(aCube.f,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        
    def test_rotate_side_r(self):
        aCube = getDefaultCube()
        aCube.f[:,2] = np.array(["12","11","10"],dtype="U6")
        aCube.u[:,2] = np.array(["3","2","1"],dtype="U6")
        aCube.b[:,0] = np.array(["4","5","6"],dtype="U6")
        aCube.d[:,2] = np.array(["9","8","7"],dtype="U6")
        aCube.r = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("r")
        self.assertTrue(np.array_equal(aCube.f[:,2],np.array(["9","8","7"],dtype="U6")) and
                        np.array_equal(aCube.u[:,2],np.array(["12","11","10"],dtype="U6")) and
                        np.array_equal(aCube.b[:,0],np.array(["1","2","3"],dtype="U6")) and
                        np.array_equal(aCube.d[:,2],np.array(["6","5","4"],dtype="U6")))
        self.assertTrue(np.array_equal(aCube.r,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        
    def test_rotate_side_u(self):
        aCube = getDefaultCube()
        aCube.f[0] = np.array(["9","8","7"],dtype="U6")
        aCube.l[0] = np.array(["12","11","10"],dtype="U6")
        aCube.b[0] = np.array(["3","2","1"],dtype="U6")
        aCube.r[0] = np.array(["6","5","4"],dtype="U6")
        aCube.u = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("u")
        self.assertTrue(np.array_equal(aCube.f[0],np.array(["6","5","4"],dtype="U6")) and
                        np.array_equal(aCube.l[0],np.array(["9","8","7"],dtype="U6")) and
                        np.array_equal(aCube.b[0],np.array(["12","11","10"],dtype="U6")) and
                        np.array_equal(aCube.r[0],np.array(["3","2","1"],dtype="U6")))
        self.assertTrue(np.array_equal(aCube.u,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        
    def test_rotate_side_l(self):
        aCube = getDefaultCube()
        aCube.f[:,0] = np.array(["4","5","6"],dtype="U6")
        aCube.u[:,0] = np.array(["1","2","3"],dtype="U6")
        aCube.b[:,2] = np.array(["12","11","10"],dtype="U6")
        aCube.d[:,0] = np.array(["7","8","9"],dtype="U6")
        aCube.l = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("l")
        self.assertTrue(np.array_equal(aCube.f[:,0],np.array(["1","2","3"],dtype="U6")) and
                        np.array_equal(aCube.u[:,0],np.array(["10","11","12"],dtype="U6")) and
                        np.array_equal(aCube.b[:,2],np.array(["9","8","7"],dtype="U6")) and
                        np.array_equal(aCube.d[:,0],np.array(["4","5","6"],dtype="U6")))
        self.assertTrue(np.array_equal(aCube.l,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        
    def test_rotate_side_b(self):
        aCube = getDefaultCube()
        aCube.l[:,0] = np.array(["4","5","6"],dtype="U6")
        aCube.u[0] = np.array(["3","2","1"],dtype="U6")
        aCube.r[:,2] = np.array(["12","11","10"],dtype="U6")
        aCube.d[2] = np.array(["7","8","9"],dtype="U6")
        aCube.b = np.array([["1","2","3"],["4","5","6"],["7","8","9"]],dtype="U6")
        aCube.rotateSide("b")
        self.assertTrue(np.array_equal(aCube.l[:,0],np.array(["1","2","3"],dtype="U6")) and
                        np.array_equal(aCube.u[0],np.array(["12","11","10"],dtype="U6")) and
                        np.array_equal(aCube.r[:,2],np.array(["9","8","7"],dtype="U6")) and
                        np.array_equal(aCube.d[2],np.array(["4","5","6"],dtype="U6")))
        self.assertTrue(np.array_equal(aCube.b,np.array([["7","4","1"],
                                                         ["8","5","2"],
                                                         ["9","6","3"]],dtype="U6")))
        

    def test_centre_on_face_f(self):
        theCube1 = getDefaultCube()
        theCube1.centreOnFace("f")
        self.assertEqual(theCube1,cube.Cube())
        self.assertEqual(theCube1.labelF,"f")

    def test_centre_on_face_b(self):
        theCube2 = getDefaultCube()
        theCube2.centreOnFace("b")
        self.assertEqual(theCube2.labelF,"b")

    def test_centre_on_face_u_and_rotate(self):
        theCube3 = getDefaultCube()
        theCube3.centreOnFace("u")
        self.assertEqual(theCube3.labelF,"u")
        ## The "front" will now be centred on side u.
        theCube3.rotateLabeledSide("f")
        ## Meaning this should be equivalent of rotating side u.
        self.assertTrue(np.array_equal(theCube3.f,np.array([["blue","blue","blue"],
                                                ["red","red","red"],
                                                ["red","red","red"]],dtype="U6")))
                                                
        
    def test_centre_on_face_u_and_rotate_twice(self):
        theCube4 = getDefaultCube()
        theCube4.resetLabels()
        theCube4.centreOnFace("u")
        self.assertEqual(theCube4.labelF,"u")
        ## The "front" will now be centred on side u.
        theCube4.rotateLabeledSide("f")
        ## Meaning this should be equivalent of rotating side u.
        theCube4.rotateLabeledSide("f")
        ## Meaning this should be equivalent of rotating side u.
        self.assertTrue(np.array_equal(theCube4.f,np.array([["orange","orange","orange"],
                                                ["red","red","red"],
                                                ["red","red","red"]],dtype="U6")))
        
    def test_rotateBottom2Rows(self):
        theCube5 = getDefaultCube()
        theCube5.rotateBottom2Rows()
        self.assertTrue(np.array_equal(theCube5.f,np.array([["red","red","red"],
                                    ["green","green","green"],
                                    ["green","green","green"]],dtype="U6")))
        
        self.assertTrue(np.array_equal(theCube5.r,np.array([["blue","blue","blue"],
                                    ["red","red","red"],
                                    ["red","red","red"]],dtype="U6")))
        
        self.assertTrue(np.array_equal(theCube5.b,np.array([["orange","orange","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","blue"]],dtype="U6")))
        
        self.assertTrue(np.array_equal(theCube5.l,np.array([["green","green","green"],
                                    ["orange","orange","orange"],
                                    ["orange","orange","orange"]],dtype="U6")))
        
    def test_rotateBottom2Rows_2(self):
        theCube5 = getDefaultCube()
        theCube5.d = np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        self.assertTrue(np.array_equal(theCube5.d,np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")))
        
    def test_rotateBottom2Rows_3_neg(self):
        theCube5 = getDefaultCube()
        theCube5.d = np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        self.assertFalse(np.array_equal(theCube5.d,np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")))
        
    def test_rotateBottom2Rows_4(self):
        theCube5 = getDefaultCube()
        theCube5.d = np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        theCube5.rotateBottom2Rows()
        self.assertFalse(np.array_equal(theCube5.d,np.array([["orange","green","orange"],
                                    ["blue","blue","blue"],
                                    ["blue","blue","red"]],dtype="U6")))


        
        
        