import distro
class person:
	def __init__(self):
		self.dist =distro.distribution(1,1,1,"temp")		
		name = raw_input("what do you want the name to be?\n")
		string = "you have %f to spend in total, how much do you want to spend on stability?" % (self.dist.starting_points)	
		pointsString = raw_input(string)
		stability = float(pointsString)
		if(stability>self.dist.starting_points or stability <=0):
			self.__init__()
		else:
			left = self.dist.starting_points - stability
			bleedingedge = 1/stability
		print("bleedingedge = %f" % (bleedingedge))
		string = "you have %f to spend in total, how much do you want to spend on community?" % (left)	
		pointsString = raw_input(string)
		community = float(pointsString)
		self.dist = distro.distribution(stability, bleedingedge, community, name)
	def turn(self):
		choice = raw_input("""pick a choice\n The choices are 1: stability 2: bleedingedge 3. community\n""")
		if(choice == "1"):
			self.dist.turn("stability")
		if(choice =="2"):
			self.dist.turn("bleedingedge")
		if(choice=="3"):
			self.dist.turn("community")
