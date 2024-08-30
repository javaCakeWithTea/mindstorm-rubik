import pytest
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

def test_white_cross_complete_pos():
    ## Solved cube should pass.
    aCube = getDefaultCube()
    assert nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_neg():
    ## Cube with one rotation on f should fail.
    aCube = getDefaultCube()
    aCube.rotateSide("f")
    assert not nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_pos_2():
    ## Set a random face with white cross and other colours to test any conditions.
    aCube = getDefaultCube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","white","orange"]])
    assert nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_neg_2():
    ## Set a random face with white cross and other colours to test any conditions.
    aCube = getDefaultCube()
    aCube.u = np.array([["green","green","red"],
                        ["white","white","white"],
                        ["yellow","white","orange"]])
    assert not nerd.Nerd.whiteCrossComplete(aCube)

## Test algorithm to solve edge flip.
def test_edge_flip_algorithm():
    aCube = getDefaultCube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","green","orange"]])
    aCube.f = np.array([["green","white","red"],
                        ["yellow","green","orange"],
                        ["yellow","green","orange"]])
    solvedCube = nerd.Nerd.flipEdge(aCube)
    assert solvedCube.u[2,1] == "white"

## Test algorithm to from bottom layer.
def test_from_bottom_layer_algorithm():
    aCube = getDefaultCube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","green","orange"]])
    aCube.f = np.array([["green","green","red"],
                        ["yellow","green","orange"],
                        ["yellow","white","orange"]])
    solvedCube = nerd.Nerd.fromBottomLayer(aCube)
    assert solvedCube.u[2,1] == "white"

## Test algorithm to from middle layer right side.
def test_from_middle_layer_right_algorithm():
    aCube = getDefaultCube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","green","orange"]])
    aCube.f = np.array([["green","green","red"],
                        ["yellow","green","white"],
                        ["yellow","orange","orange"]])
    solvedCube = nerd.Nerd.fromMiddleLayerRight(aCube)
    assert solvedCube.u[2,1] == "white"

## Test algorithm to from middle layer right side.
def test_from_middle_layer_left_algorithm():
    aCube = getDefaultCube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","green","orange"]])
    aCube.f = np.array([["green","green","red"],
                        ["white","yellow","green"],
                        ["yellow","orange","orange"]])
    solvedCube = nerd.Nerd.fromMiddleLayerLeft(aCube)
    assert solvedCube.u[2,1] == "white"

def test_solve_completed_cube():
    aCube = getDefaultCube()
    aCube = nerd.Nerd.solve(aCube)
    assert aCube == getDefaultCube()
