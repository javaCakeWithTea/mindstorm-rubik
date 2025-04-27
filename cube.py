import numpy as np

class Cube:
    ## Defines the Cube class and saves the state of this cube in memory.
    def __init__(self,
                 f=np.full((3,3),"red",dtype="U6"),
                 u=np.full((3,3),"white",dtype="U6"),
                 l=np.full((3,3),"green",dtype="U6"),
                 r=np.full((3,3),"blue",dtype="U6"),
                 b=np.full((3,3),"orange",dtype="U6"),
                 d=np.full((3,3),"yellow",dtype="U6")):
        self.f = f
        self.u = u
        self.l = l
        self.r = r
        self.b = b
        self.d = d
        ## Variables to set temporary labeling of a side.
        ## By defualt this should be the side itself.
        self.labelF = "f"
        self.labelU = "u"
        self.labelL = "l"
        self.labelR = "r"
        self.labelB = "b"
        self.labelD = "d"

    def rotate(self,front,up,down,right,left):
        left = np.atleast_2d(left).T
        right = np.atleast_2d(right).T
        rotationMatrix = np.hstack((left,front,right))
        topRow = np.hstack((["empty"],up,["empty"]))
        bottomRow = np.hstack((["empty"],down,["empty"]))
        rotationMatrix = np.vstack((topRow,rotationMatrix,bottomRow))

        rotatedMatrix = self.rotateFiveByFive(rotationMatrix)

        return rotatedMatrix

    def rotateFiveByFive(self,tensor):
        ## Rotates a tensor by 90 degrees clockwise on its axis.
        return np.rot90(tensor,-1)
    
    def rotateSide(self,face):
        ## Rotates a certain face by 90 degrees clock-wise.
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
            up = self.b[0][::-1] # flipped
            down = self.f[0]
            right = self.r[0][::-1] # flipped
            left = self.l[0]
            rotatedMatrix = self.rotate(self.u,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.u = returnedValues[0]
            self.b[0][::-1] = returnedValues[1]
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
            down = self.d[2][::-1] # flipped
            right = self.l[:,0]
            left = self.r[:,2]
            rotatedMatrix = self.rotate(self.b,up,down,right,left)
            returnedValues = self.setCube(rotatedMatrix)
            self.b = returnedValues[0]
            self.u[0][::-1] = returnedValues[1]
            self.d[2][::-1] = returnedValues[2]
            self.l[:,0] = returnedValues[3]
            self.r[:,2] = returnedValues[4]
        return

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
        down = np.delete(rotationMatrix[4],[0,-1])
        left = np.delete(rotationMatrix[:,0],[0,-1])
        right = np.delete(rotationMatrix[:,4],[0,-1])
        front = rotationMatrix[1:-1,1:-1]
        return front,up,down,right,left
    
    def rotateBottom2Rows(self):
        ## Rotates the bottom two rows of the cube. If U is the top.
        self.d = np.rot90(np.copy(self.d),-1)
        bottomR = np.copy(self.f[1:,:])
        bottomF = np.copy(self.l[1:,:])
        bottomB = np.copy(self.r[1:,:])
        bottomL = np.copy(self.b[1:,:])
        self.r[1:,:] = bottomR
        self.f[1:,:] = bottomF
        self.b[1:,:] = bottomB
        self.l[1:,:] = bottomL
        return

    def centreOnFace(self,face):
        self.resetLabels()
        ## Changes this side to temporarily be the front.
        if face == "f":
            return
        elif face == "u":
            self.labelF = "u"
            self.labelD = "f"
            self.labelB = "d"
            self.labelU = "b"
        elif face == "d":
            self.labelF = "d"
            self.labelD = "b"
            self.labelB = "u"
            self.labelU = "f"
        elif face == "b":
            self.labelF = "b"
            self.labelL = "r"
            self.labelR = "l"
            self.labelB = "f"
        elif face == "r":
            self.labelF = "r"
            self.labelL = "f"
            self.labelR = "b"
            self.labelB = "l"
        elif face == "l":
            self.labelF = "l"
            self.labelL = "b"
            self.labelR = "f"
            self.labelB = "r"
        return

    def resetLabels(self):
        self.labelF = "f"
        self.labelU = "u"
        self.labelL = "l"
        self.labelR = "r"
        self.labelB = "b"
        self.labelD = "d"
        return

    def rotateLabeledSide(self,labeledSide):
        ## Checks what is the real side for this label and rotates this.
        if labeledSide=="f":
            self.rotateSide(self.labelF)
        if labeledSide=="u":
            self.rotateSide(self.labelU)
        if labeledSide=="l":
            self.rotateSide(self.labelL)
        if labeledSide=="r":
            self.rotateSide(self.labelR)
        if labeledSide=="b":
            self.rotateSide(self.labelB)
        if labeledSide=="d":
            self.rotateSide(self.labelD)
        return
    
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
