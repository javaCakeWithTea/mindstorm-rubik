import cube as c
import numpy as np
import nerd
import white_corners

aCube = c.Cube()
white_corners.white_corners.removeWhiteCornersFromU(aCube)
print([aCube.f[2,2],aCube.r[2,0],aCube.d[0,2]])
print([aCube.r[2,2],aCube.b[2,0],aCube.d[2,2]])
print([aCube.b[2,2],aCube.l[2,0],aCube.d[2,0]])
print([aCube.l[2,2],aCube.f[2,0],aCube.d[0,0]])