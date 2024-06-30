import numpy as np

class Cube:
    ## Defines the Cube class and saves the state of this cube in memory.
    def __init__(self,
                 f=np.full((3,3),"red",dtype="U6"),
                 u=np.full((3,3),"white",dtype="U6"),
                 l=np.full((3,3),"blue",dtype="U6"),
                 r=np.full((3,3),"orange",dtype="U6"),
                 b=np.full((3,3),"black",dtype="U6"),
                 d=np.full((3,3),"green",dtype="U6")):
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
        return rotatedMatrix

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
            rotatedMatrix = self.rotate(self.f,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.f = returnedValues[0]
            self.u[2] = returnedValues[1]
            self.d[0] = returnedValues[2]
            self.r[:,0] = returnedValues[3]
            self.l[:,2] = returnedValues[4]
        if face == "u":
            up = self.b[0]
            down = self.f[0]
            right = self.r[0][::-1] # flipped
            left = self.l[0]
            rotatedMatrix = self.rotate(self.u,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.u = returnedValues[0]
            self.b[0] = returnedValues[1]
            self.f[0] = returnedValues[2]
            self.r[0][::-1] = returnedValues[3]
            self.l[0] = returnedValues[4]
        if face == "r":
            up = self.u[:,2][::-1] # flipped
            down = self.d[:,2]
            right = self.b[:,0]
            left = self.f[:,2]
            rotatedMatrix = self.rotate(self.r,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.r = returnedValues[0]
            self.u[:,2][::-1] = returnedValues[1]
            self.d[:,2] = returnedValues[2]
            self.b[:,0] = returnedValues[3]
            self.f[:,2] = returnedValues[4]
        if face == "l":
            up = self.u[:,0]
            down = self.d[:,0][::-1] # flipped
            right = self.f[:,0]
            left = self.b[:,2]
            rotatedMatrix = self.rotate(self.l,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.l = returnedValues[0]
            self.u[:,0] = returnedValues[1]
            self.d[:,0][::-1] = returnedValues[2]
            self.f[:,0] = returnedValues[3]
            self.b[:,2] = returnedValues[4]
        if face == "d":
            up = self.f[2]
            down = self.b[2][::-1] # flipped
            right = self.r[2]
            left = self.l[2][::-1] # flipped
            rotatedMatrix = self.rotate(self.d,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.d = returnedValues[0]
            self.f[2] = returnedValues[1]
            self.b[2][::-1] = returnedValues[2]
            self.r[2] = returnedValues[3]
            self.l[2][::-1] = returnedValues[4]
        if face == "b":
            up = self.u[0][::-1] # flipped
            down = self.d[2]
            right = self.l[:,0]
            left = self.r[:,2]
            rotatedMatrix = self.rotate(self.b,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.b = returnedValues[0]
            self.u[0][::-1] = returnedValues[1]
            self.d[2] = returnedValues[2]
            self.l[:,0] = returnedValues[3]
            self.r[:,2] = returnedValues[4]

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
        front = rotationMatrix[1:-1,1:-1]
        return front,up,down,right,left
    
    def __eq__(self,other):
        ## Equality needs to handle "any" placeholders where we don't care for a match.
        for otherValue,selfValue in np.nditer([other.f,self.f],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
            
        for otherValue,selfValue in np.nditer([other.u,self.u],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
            
        for otherValue,selfValue in np.nditer([other.d,self.d],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
            
        for otherValue,selfValue in np.nditer([other.l,self.l],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
            
        for otherValue,selfValue in np.nditer([other.r,self.r],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
            
        for otherValue,selfValue in np.nditer([other.b,self.b],order='F'):
            if otherValue == "any" or selfValue == "any":
                continue
            elif otherValue == selfValue:
                continue
            else:
                return False
        
        return True
