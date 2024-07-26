import pytest
import nerd
import cube

def test_white_cross_complete_pos():
    aCube = cube.Cube()
    assert nerd.Nerd.whiteCrossComplete(aCube)
    
def test_solveBadCross():
    scrambledCube = cube.Cube()
    scrambledCube.rotateSide("f")
    solvedCross = nerd.Nerd.solve(scrambledCube)
    assert nerd.Nerd.whiteCrossComplete(solvedCross)

def test_cubeEquality():
    scrambledCube = cube.Cube()
    scrambledCube.rotateSide("f")
    scrambledCube.rotateSide("f")
    scrambledCube.rotateSide("f")
    assert cube.Cube() == scrambledCube
