"""gaurav"""
import os
import sys
import termios
import atexit
from select import select


class KBHit(object):
    """dixit"""

    def __init__(self):
        if os.name == 'nt':
            pass
        else:
            self.filed = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.filed)
            self.old_term = termios.tcgetattr(self.filed)

            self.new_term[3] = (self.new_term[3] & ~
                                termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.filed, termios.TCSAFLUSH, self.new_term)
            atexit.register(self.set_normal_term)
            self.temp = 1

    def set_normal_term(self):
        """gaurav"""
        self.temp = 0
        termios.tcsetattr(self.filed, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        """gaurav"""
        self.temp = 1
        return sys.stdin.read(1)

    def getarrow(self):
        """dixit"""
        self.temp = 0
        car = sys.stdin.read(3)[2]
        vals = [65, 67, 66, 68]
        return vals.index(ord(car.decode('utf-8')))

    def kbhit(self):
        """dixit"""
        draw, dwarf, deaf = select([sys.stdin], [], [], 0)
        self.temp = dwarf
        self.temp = deaf
        return draw != []