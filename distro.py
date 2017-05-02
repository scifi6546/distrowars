import math
class distrobution:
        starting_points = 10.0;
        def __init__(self, stability, community, bleedingedge):
                self.stability = stability
                self.bleedingedge = bleedingedge
                self.community = community
                self.starttotal = stability + .1*community + bleedingedge
                self.turncount = 0;
        def turn(self,choice):
                if(choice=="stability"):
                        self.stability+=self.community
                if(choice=="bleedingedge"):
                        self.bleedingedge+=self.community
                        self.stability-= .1*self.community
                if(choice=="community"):
                        self.community+= .1*self.community
                self.turncount += 1
                self.community += .1*self.difference()
                if(self.community<0):
                    self.community = 0.0
        def spendturn(self):
                return self.community *.1
        def out(self):
                out = ""
                # [stability,bleedingedge,community]
                return [self.stability,self.bleedingedge,self.community]

        def score(self): 
                return self.stability+0.1*self.community+self.bleedingedge
        def difference(self):
                shouldbe = self.starttotal*math.e**(.1*self.turncount)
                return self.score() - shouldbe

