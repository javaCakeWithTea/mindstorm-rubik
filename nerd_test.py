import pytest
import nerd
import cube
import numpy as np

## Testing white cross completion condition.

def test_white_cross_complete_pos():
    ## Solved cube should pass.
    aCube = cube.Cube()
    assert nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_neg():
    ## Cube with one rotation on f should fail.
    aCube = cube.Cube()
    aCube.rotateSide("f")
    assert not nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_pos_2():
    ## Set a random face with white cross and other colours to test any conditions.
    aCube = cube.Cube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","white","orange"]])
    assert nerd.Nerd.whiteCrossComplete(aCube)

def test_white_cross_complete_neg_2():
    ## Set a random face with white cross and other colours to test any conditions.
    aCube = cube.Cube()
    aCube.u = np.array([["green","green","red"],
                        ["white","white","white"],
                        ["yellow","white","orange"]])
    assert not nerd.Nerd.whiteCrossComplete(aCube)

## Test algorithm to solve edge flip.
def test_edge_flip_algorithm():
    aCube = cube.Cube()
    aCube.u = np.array([["green","white","red"],
                        ["white","white","white"],
                        ["yellow","green","orange"]])
    aCube.f = np.array([["green","white","red"],
                        ["yellow","green","orange"],
                        ["yellow","green","orange"]])
    solvedCube = nerd.Nerd.flipEdge(aCube)
    assert solvedCube.u[2,1] == "white"

def test_solve():
    aCube = cube.Cube()
    aCube = nerd.Nerd.solve(aCube)
    assert aCube == cube.Cube()