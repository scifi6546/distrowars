class distrobution:
        starting_points = 10.0;
        def __init__(self, stability, community, bleedingedge):
                self.stability = stability
                self.bleedingedge = bleedingedge
                self.community = community
        def turn(self,choice):
                if(choice=="stability"):
                        self.stability+=self.community
                if(choice=="bleedingedge"):
                        self.bleedingedge+=self.community
                        self.stability-= .1*self.community
                if(choice=="community"):
                        self.community+= .1*self.community
        def spendturn(self):
                return self.community*.1
        def out(self):
                out = ""
                # [stability,bleedingedge,community]
                return [self.stability,self.bleedingedge,self.community]


