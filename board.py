import random
from obstacle import Obstacle
# from colorama import Fore,Back,Style
import colorama
from colorama import Back as bg, Fore as fg,Style



class Board:    
    grid=[]
    base=[]
    def __init__(self,rows,cols):   
        self.__rows=rows
        self.__cols=cols
        for i in range(0,rows-1):
            tmp=[]
            tmp2=[]
            for j in range(0,2000):
                tmp.append(' ')
                tmp2.append([])
            self.grid.append(tmp)
            self.base.append(tmp2)
        for i in range(0,1):
            tmp=[]
            tmp2=[]
            for j in range(0,2000): 
                tmp.append('X')
                tmp2.append([])
            self.grid.append(tmp)
            self.base.append(tmp2)

        l=0          
        f=2000
        while True:
            l1=random.randint(l,l+4)
            if l1>f:
                break
            num=random.randint(1,120)
            l2=3
            for i in range(0,num):
                mode=random.randint(0,7)
                # l3=55;
                l2=random.randint(l2,l2+10)
                if l2 >=50:
                    break
                mode=6
                ob=Obstacle(l2,l1,mode,self)
                for i in range(0,len(ob.mat)):
                    for j in range(0,len(ob.mat[0])):
                        self.base[l2+i][l1+j].append(ob)

                l2=l2+10

            l1=l1+50
            l=l1

    print(bg.BLACK,end='')
    print(Style.BRIGHT,end='')
    def clear(self):
        return 1
        print('\033[3;1H',end='')
    def printboard(self,st):
        c=1
        for i in range(3,self.__rows):
            for j in range(st,self.__cols+st):
                ch=self.grid[i][j]
                # color="RED"
                if ch=='*':
                    print(fg.YELLOW,end='')
                    # print(Style.BRIGHT,end='')
                #     color="YELLOW"
                elif ch=='X':
                    if c==0:
                        print(fg.MAGENTA,end='')
                        c=1
                    elif c==1:
                        print(fg.WHITE,end='')
                        c=0

                elif ch=='/' or ch=='\\':
                    if c == 0:
                        print(fg.RED,end='')
                        c=1
                    elif c == 1:
                        print(fg.YELLOW,end='')
                        c=0
                elif ch == '@' and c == 1:
                    print(fg.BLUE,end='')
                    c=0
                elif ch =='@' and c == 0:
                    print(fg.YELLOW,end='')
                    c=1
                elif ch =='-':
                    if c==0:
                        print(fg.CYAN,end='')
                        c=1
                    elif c==1:
                        print(fg.YELLOW,end='')
                        c=0
                elif ch == '|':
                    if c ==0:
                        print(fg.YELLOW,end='')
                        c=1
                    elif c==1:
                        print(fg.RED,end='')
                        c=0

                #     # print(bg.RED+fg.RED+' ')
                #     print(fg.RED,end='')
                #     # print(bg.RED,end='')
                #     # print('\033[35m',end='')
                # elif ch== '@':
                #     print(fg.GREEN,end='')
                #     # print(Style.BRIGHT,end='')
                # elif ch == '(' or ch== ')':
                #     print(fg.GREEN,end='')
                # else:
                #     print(fg.RED,end='')
                #     color = "BLACK"
                #     print(fg.RED,end='')

                print(self.grid[i][j],end='')
            print()
    def printboard1(self):
        for i in range(0,self.__rows-1):
            for j in range(0,self.__cols):
                print(self.grid[i][j],end='')          
            print()
# board=Board(55,200)
# board.printboard()


