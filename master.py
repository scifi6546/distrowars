import player
import gui
import distro
import goodgui
class master:
    def startplayer(self):
        person = player.person()
    def __init__(self):
        total = 1.8
        # self.userin = gui.cligui()
        self.userin = goodgui.ggui()
        [stability,community,bleedingedge] = self.userin.startup(total)
        self.playerdistro = distro.distrobution(stability,community,bleedingedge)
        # self.startplayer()
        while(0==0):
            self.turn()
    def turn(self):
        stability = self.playerdistro.stability
        community = self.playerdistro.community
        bleedingedge = self.playerdistro.bleedingedge
        self.userin.turnbanner(stability,community,bleedingedge)
        amount = self.playerdistro.spendturn()
        self.playerdistro.turn(self.userin.turn(amount)) 
a = master()
