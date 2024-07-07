import cube
import numpy as np
import nerd

cube1 = cube.Cube()
cube1.rotateSide("f")

solved = nerd.Nerd.solve(cube1)
print(solved)