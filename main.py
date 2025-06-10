import cube as c
import numpy as np
import white_corners

aCube = c.Cube()
aCube.rotateSide("l")
aCube.rotateSide("r")
aCube.rotateSide("d")
aCube.rotateSide("b")
aCube.rotateSide("u")
white_corners.white_corners.removeWhiteCornersFromU(aCube)
white_corners.white_corners.putCornersInPlace(aCube)
print([aCube.f[2,2],aCube.r[2,0],aCube.d[0,2]])
print([aCube.r[2,2],aCube.b[2,0],aCube.d[2,2]])
print([aCube.b[2,2],aCube.l[2,0],aCube.d[2,0]])
print([aCube.l[2,2],aCube.f[2,0],aCube.d[0,0]])
##Top
print([aCube.f[0,2],aCube.r[0,0],aCube.u[2,2]])
print([aCube.r[0,2],aCube.b[0,0],aCube.u[0,2]])
print([aCube.b[0,2],aCube.l[0,0],aCube.u[0,0]])
print([aCube.l[0,2],aCube.f[0,0],aCube.u[2,0]])