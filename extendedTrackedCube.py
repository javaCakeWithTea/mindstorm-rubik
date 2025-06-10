import cube

class ExtendedTrackedCube(cube):

    def __init__(self,cube):
        self.cube = cube
        self.solution = ""

    def append(self,newRotation):
        self.solution = self.solution + newRotation

    def optimise(self):
        ## Replace any tripple movements with a single anti-clockwise movement.
        self.solution = self.solution.replace("lll","l'")
        self.solution = self.solution.replace("fff","f'")
        self.solution = self.solution.replace("rrr","r'")
        self.solution = self.solution.replace("bbb","b'")
        self.solution = self.solution.replace("uuu","u'")
        self.solution = self.solution.replace("ddd","d'")
        ## Add any other optimisations.

    def getSolutionString(self):
        return self.solution
    
    def readInColours():
        ## Code to read in the colours of tiles from the NXT.
    









