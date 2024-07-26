import pytest
import nerd
import cube
import numpy as np

def test_centre_on_face_f():
    theCube = cube.Cube()
    theCube.centreOnFace("f")
    assert theCube == cube.Cube()
    assert theCube.labelF == "f"

def test_centre_on_face_b():
    theCube = cube.Cube()
    theCube.centreOnFace("b")
    assert theCube.labelF == "b"

def test_centre_on_face_u_and_rotate():
    theCube = cube.Cube()
    theCube.centreOnFace("u")
    assert theCube.labelF == "u"
    ## The "front" will now be centred on side u.
    theCube.rotateLabeledSide("f")
    ## Meaning this should be equivalent of rotating side u.
    assert np.array_equal(theCube.f,np.array([["blue","blue","blue"],
                                            ["red","red","red"],
                                            ["red","red","red"]],dtype="U6"))
    
def test_centre_on_face_u_and_rotate_twice():
    theCube = cube.Cube()
    theCube.centreOnFace("u")
    assert theCube.labelF == "u"
    ## The "front" will now be centred on side u.
    theCube.rotateLabeledSide("f")
    theCube.rotateLabeledSide("f")
    ## Meaning this should be equivalent of rotating side u.
    assert np.array_equal(theCube.f,np.array([["orange","orange","orange"],
                                            ["red","red","red"],
                                            ["red","red","red"]],dtype="U6"))