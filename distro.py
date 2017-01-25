class distribution:
	starting_points = 10.0;
	def __init__(self, stability, bleedingedge, community, name):
		self.stability = stability
		self.bleedingedge = bleedingedge
		self.community = community
		self.name = name
	def turn(self,choice):
		if(choice=="stability"):
			self.stability+=self.community
		if(choice=="bleedingedge"):
			self.bleedingedge+=self.community
			self.stability-= .1*self.community
		if(choice=="community"):
			self.community+= .1*self.community
	def out(self):
		out = ""
		out = out + "stability: %f" % (self.stability)
		out = out + "  bleedingedge: %f" % (self.bleedingedge)
		out = out + "  community: %f" % (self.community)
		return [out]


