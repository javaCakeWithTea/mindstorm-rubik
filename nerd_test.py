import unittest
import nerd
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

## Testing white cross completion condition.
class TestNerdMethods(unittest.TestCase): 
    def test_white_cross_complete_pos(self):
        ## Solved cube should pass.
        aCube = getDefaultCube()
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))

    def test_white_cross_complete_neg(self):
        ## Cube with one rotation on f should fail.
        aCube = getDefaultCube()
        aCube.rotateSide("f")
        self.assertFalse(nerd.Nerd.whiteCrossComplete(aCube))

    def test_white_cross_complete_pos_2(self):
        ## Set a random face with white cross and other colours to test any conditions.
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","white","orange"]])
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube))

    def test_white_cross_complete_neg_2(self):
        ## Set a random face with white cross and other colours to test any conditions.
        aCube = getDefaultCube()
        aCube.u = np.array([["green","green","red"],
                            ["white","white","white"],
                            ["yellow","white","orange"]])
        self.assertFalse(nerd.Nerd.whiteCrossComplete(aCube))

    def test_bad_white_cross_complete_neg(self):
        ## Set a random face with white cross and other colours to test any conditions.
        aCube = getDefaultCube()
        aCube.u = np.array([["green","red","red"],
                            ["white","white","white"],
                            ["yellow","white","orange"]])
        aCube.f = np.array([["green","green","red"],
                            ["white","red","white"],
                            ["yellow","white","orange"]])
        self.assertFalse(nerd.Nerd.whiteBadCrossComplete(aCube))

    def test_bad_white_cross_complete(self):
        ## Set a random face with white cross and other colours to test any conditions.
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","white","orange"]])
        aCube.f = np.array([["green","green","red"],
                            ["white","red","white"],
                            ["yellow","white","orange"]])
        self.assertTrue(nerd.Nerd.whiteBadCrossComplete(aCube))

    ## Test algorithm to solve edge flip.
    def test_edge_flip_algorithm(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.f = np.array([["green","white","red"],
                            ["yellow","green","orange"],
                            ["yellow","green","orange"]])
        solvedCube = nerd.Nerd.flipEdge(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from bottom layer.
    def test_from_bottom_layer_algorithm(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.f = np.array([["green","green","red"],
                            ["yellow","green","orange"],
                            ["yellow","white","orange"]])
        solvedCube = nerd.Nerd.fromBottomLayer(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from middle layer right side.
    def test_from_middle_layer_right_algorithm(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.f = np.array([["green","green","red"],
                            ["yellow","green","white"],
                            ["yellow","orange","orange"]])
        solvedCube = nerd.Nerd.fromMiddleLayerRight(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from middle layer right side.
    def test_from_middle_layer_left_algorithm(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.f = np.array([["green","green","red"],
                            ["white","yellow","green"],
                            ["yellow","orange","orange"]])
        solvedCube = nerd.Nerd.fromMiddleLayerLeft(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from bottom face "d".
    def test_from_bottom_face_1(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.d = np.array([["green","green","red"],
                            ["white","yellow","green"],
                            ["yellow","orange","orange"]])
        solvedCube = nerd.Nerd.fromDFace(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from bottom face "d".
    def test_from_bottom_face_2(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.d = np.array([["green","white","red"],
                            ["yellow","yellow","green"],
                            ["yellow","orange","orange"]])
        solvedCube = nerd.Nerd.fromDFace(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from bottom face "d".
    def test_from_bottom_face_3(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.d = np.array([["green","green","red"],
                            ["yellow","yellow","white"],
                            ["yellow","orange","orange"]])
        solvedCube = nerd.Nerd.fromDFace(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    ## Test algorithm to from bottom face "d".
    def test_from_bottom_face_4(self):
        aCube = getDefaultCube()
        aCube.u = np.array([["green","white","red"],
                            ["white","white","white"],
                            ["yellow","green","orange"]])
        aCube.d = np.array([["green","green","red"],
                            ["yellow","yellow","orange"],
                            ["yellow","white","orange"]])
        solvedCube = nerd.Nerd.fromDFace(aCube)
        self.assertTrue(solvedCube.u[2,1] == "white")

    def test_solve_completed_cube(self):
        aCube = getDefaultCube()
        aCube = nerd.Nerd.solve(aCube)
        self.assertTrue(aCube == getDefaultCube())

    def test_solve_one_flip(self):
        aCube10 = getDefaultCube()
        aCube10.rotateSide("r")
        nerd.Nerd.solve(aCube10)
        self.assertTrue(nerd.Nerd.whiteBadCrossComplete(aCube10))

    def test_solve_two_flip(self):
        aCube10 = getDefaultCube()
        aCube10.rotateSide("r")
        aCube10.rotateSide("f")
        nerd.Nerd.solve(aCube10)
        self.assertTrue(nerd.Nerd.whiteBadCrossComplete(aCube10))

    def test_solve_tree_flip(self):
        aCube10 = getDefaultCube()
        aCube10.rotateSide("r")
        aCube10.rotateSide("f")
        aCube10.rotateSide("d")
        nerd.Nerd.solve(aCube10)
        self.assertTrue(nerd.Nerd.whiteBadCrossComplete(aCube10))

    def test_solve_tree_flip_good_cross(self):
        aCube10 = getDefaultCube()
        aCube10.rotateSide("r")
        aCube10.rotateSide("f")
        aCube10.rotateSide("d")
        nerd.Nerd.solve(aCube10)
        print(aCube10.l[0,1],aCube10.f[0,1],aCube10.r[0,1],aCube10.b[0,1])
        self.assertTrue(nerd.Nerd.whiteCrossComplete(aCube10))