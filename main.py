import cube
import numpy as np
import nerd

cube1 = cube.Cube()
cube1.d[0] = np.array(["messing","a","bout"])

print(nerd.Nerd.whiteCrossComplete(cube1))
