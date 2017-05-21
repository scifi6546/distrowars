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
        tempstr = "you have %f to spend in total how much do you want to spend on stability?" % (total)
        self.window.addstr(1,0,tempstr) 
        self.window.refresh()
        stability = float(self.userinput(2,0))
        self.window.addstr(1,0,self.spaces(tempstr))
        left = total - stability
        tempstr = "you have %f to spend in total how much do you want to spend on community?" % (left)
        self.window.addstr(1,0,tempstr)
        community = float(self.userinput(2,0))
        self.window.addstr(2,0,self.spaces(tempstr))  
        left -= community
        tempstr = "you have %f to spend in total how much do you want to spend on bleedingedge" % (left)
        self.window.addstr(1,0,tempstr)
        bleedingedte = float(self.userinput(2,0))
        self.window.addstr(1,0,self.spaces(tempstr))
        return [stabilitgy,community,bleedingedge]
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
    def spaces(self,string):
        outstring = ""
        for i in range(1,len(string)):
                outstring+=" "
        return outstring
