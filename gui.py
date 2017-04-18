class cligui:
     def __init__(self): 
         print("welcome to my game")
     def startup(self,total):   #[stability,community,bleedingedge]
         print("you have %f to spend in total" % (total))
         stability = float(input("how much do you want to spend on stability"))
         left = total - stability
         community = float(input("you have %f to spend on community, how much do you want to spend?\n" % (left)))
         left -= community
         bleedingedge = float(input("you have %f left to spend on bleedingedge, how much do you want to spend?" % (left)))
         left -= bleedingedge
         if(left<0):
             print("you naughty little person try again")
             self.startup(total)
         return [stability,community,bleedingedge]
     def turnbanner(self, stability,community,bleedingedge):
         print("stability: %f" % (stability))
         print("community: %f" % (community))
         print("bleedingedge: %f" % (bleedingedge))
     def turn(self,spend):
         print("you have %f to spend" % (spend))
         out = ""
         choice = input("you can spend it on 1. stability, 2. community, 3. bleedingedge\n")
         if(choice == "1"):
             out = "stability"
         if(choice == "2"):
             out = "community"
         if(choice == "3"):
             out = "bleedingedge"
         return out
