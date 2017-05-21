import gui
import curses
import os
import time
class ggui:
    def __init__(self):
        self.collums, self.rows = os.get_terminal_size(0)
        self.window = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.window.keypad(True)
    def startup(self,total):
        self.window.addstr(1,0,"you have %f to spend in total how much do you want to spend on stability?" % (total)) 
        self.window.refresh()
        stability = self.userinput(2,0)
        return [1,1,1]
    def turnbanner(self,stability,community,bleedingedge):
        a = 1+1
    def turn(self,spend):
        time.sleep(.1)
        return "bleedingedge"
    def end():
        curses.nocbreak()
        curses.echo()
        self.window.keypad(False)
        curses.endwin()
    def userinput(self,y,x):
        endloop = 0
        string = ""
        while(endloop == 0):
           intchar = self.window.getch()
           char = chr(intchar) 
           used = 0
           if(intchar==127):
               length = len(string)
               string = string[:length-1]
               temp = string + " "
               self.window.addstr(y,x,temp)
               self.window.refresh()
               used = 1
           if(char=='\n'):
               endloop = 1
               used = 1
               return string
           if(used == 0):
               string+=char
               self.window.addstr(y,x,string)
               self.window.refresh()
