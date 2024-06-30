import numpy as np

class Cube:
    ## Defines the Cube class and saves the state of this cube in memory.
    def __init__(self,
                 f=np.full((3,3),"white"),
                 u=np.full((3,3),"red"),
                 l=np.full((3,3),"blue"),
                 r=np.full((3,3),"orange"),
                 b=np.full((3,3),"black"),
                 d=np.full((3,3),"green")):
        self.f = f
        self.u = u
        self.l = l
        self.r = r
        self.b = b
        self.d = d

    def rotate(self,front,up,down,right,left):
        left = np.atleast_2d(left).T
        right = np.atleast_2d(right).T
        rotationMatrix = np.hstack((left,front,right))
        topRow = np.hstack((["empty"],up,["empty"]))
        bottomRow = np.hstack((["empty"],down,["empty"]))
        rotationMatrix = np.vstack((topRow,rotationMatrix,bottomRow))
        print("Matrix pre-rotation:")
        print(rotationMatrix)
        rotatedMatrix = self.rotateFiveByFive(rotationMatrix)
        print("Matrix post rotation:")
        print(rotatedMatrix)

    def rotateFiveByFive(self,tensor):
        ## Rotates a tensor by 90 degrees clockwise on its axis.
        return np.rot90(tensor,-1)
    
    def rotateSide(self,face):
        ## Fetches all the squares which will be transformed by moving this face.
        if face == "f":
            up = self.u[2]
            down = self.d[0]
            right = self.r[:,0]
            left = self.l[:,2]
            self.rotate(self.f,up,down,right,left)
        if face == "u":
            up = self.b[0]
            down = self.f[0]
            right = self.r[0][::-1] # flipped
            left = self.l[0]
            self.rotate(self.u,up,down,right,left)
        if face == "r":
            up = self.u[:,2][::-1] # flipped
            down = self.d[:,2]
            right = self.b[:,0]
            left = self.f[:,2]
            self.rotate(self.r,up,down,right,left)
        if face == "l":
            up = self.u[:,0]
            down = self.d[:,0][::-1] # flipped
            right = self.f[:,0]
            left = self.b[:,2]
            self.rotate(self.l,up,down,right,left)
        if face == "d":
            up = self.f[2]
            down = self.b[2][::-1] # flipped
            right = self.r[2]
            left = self.l[2][::-1] # flipped
            self.rotate(self.d,up,down,right,left)
        if face == "b":
            up = self.u[0][::-1] # flipped
            down = self.d[2]
            right = self.l[:,0]
            left = self.r[:,2]
            self.rotate(self.b,up,down,right,left)

    def setRotationMatrix(self,front,up,down,right,left):
        left = np.atleast_2d(left).T
        right = np.atleast_2d(right).T
        rotationMatrix = np.hstack((left,front,right))
        topRow = np.hstack((["empty"],up,["empty"]))
        bottomRow = np.hstack((["empty"],down,["empty"]))
        rotationMatrix = np.vstack((topRow,rotationMatrix,bottomRow))
        return rotationMatrix
    
    def setCube(self,rotationMatrix):
        up = np.delete(rotationMatrix[0],[0,-1])
        down = np.delete(rotationMatrix[2],[0,-1])
        left = np.delete(rotationMatrix[:,0],[0,-1])
        right = np.delete(rotationMatrix[:,2],[0,-1])
        front = np.delete(rotationMatrix[1:-2,1:-2])
        return front,up,down,right,left






        



