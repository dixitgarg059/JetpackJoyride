import random
from obstacle import Obstacle
import colorama
from colorama import Back as bg, Fore as fg,Style
import time
class Board:    
    __grid=[]
    __base=[]
    def __init__(self,rows,cols,magnetss):   
        self.__rows=rows
        self.__cols=cols
        for i in range(0,rows-1):
            tmp=[]
            tmp2=[]
            for j in range(0,2300):
                tmp.append(' ')
                tmp2.append([])
            self.__grid.append(tmp)
            self.__base.append(tmp2)
        for i in range(0,1):
            tmp=[]
            tmp2=[]
            for j in range(0,2300): 
                tmp.append('X')
                tmp2.append([])
            self.__grid.append(tmp)
            self.__base.append(tmp2)

        l=0          
        f=1960
        count_magnets=0
        dragon_done=False
        while True:
            random.seed(time.time())
            l1=random.randint(l,l+4)
            if l1>f:
                break
            num=random.randint(1,100)
            l2=10
            if l1 > 800 and dragon_done == False:
                l2=random.randint(10,30)
                ob=Obstacle(l2,l1,10,self)
                for i in range(0,len(ob.get_mat())):
                    for j in range(0,len(ob.get_mat()[0])):
                        self.__base[l2+i][l1+j].append(ob)
                l2=l2+10
                dragon_done=True
            is_magnet=False
            for i in range(0,num):

                mode=random.randint(0,7)
                l2=random.randint(l2,l2+10)
                if l2 >=48:
                    break
                if mode == 6 and is_magnet==False and count_magnets < 4:
                    magnetss.append([l2,l1])
                    is_magnet=True
                    count_magnets=count_magnets+1
                elif mode == 6:
                    mode=random.randint(0,5)
                ob=Obstacle(l2,l1,mode,self)
                for i in range(0,len(ob.get_mat())):
                    for j in range(0,len(ob.get_mat()[0])):
                        self.__base[l2+i][l1+j].append(ob)

                l2=l2+10

            l1=l1+50
            l=l1
        l=0
        f=1960
        while True:
            random.seed(time.time())
            l1=random.randint(l,l+10)
            if l > f:
                break

            ob=Obstacle(4,l1,random.randint(8,9),self)
            l1=l1+100
            l=l1

    print(bg.BLACK,end='')
    print(Style.BRIGHT,end='')
    def printboard(self,st,is_dragon=False):
        is_dragon=False
        if is_dragon:
            print("hello world")
            for i in range(3,self.__rows):
                for j in range(st,self.__cols+st):
                    self.__grid[i][j]=' '

        c=1
        for i in range(2,self.__rows):
            for j in range(st,self.__cols+st):
                ch=self.__grid[i][j]
                if ch=='*':
                    print(fg.YELLOW,end='')
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
                elif ch == '#' and c == 1:
                    print(fg.BLUE,end='')
                    c=0
                elif ch =='#' and c == 0:
                    print(fg.YELLOW,end='')
                    c=1

                elif ch == '@' and c==1:
                    print(fg.WHITE,end='')
                    c=0
                elif ch == '@' and c==0:
                    print(fg.MAGENTA,end='')
                    c=1
                elif ch =='-':
                    if c==0:
                        print(fg.RED,end='')
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
                elif ch == '%':
                    print(fg.CYAN,end='')
                print(self.__grid[i][j],end='')
            print()
    def remove(self):
        for i in range(0,len(self.__grid)):
            for j in range(0,len(self.__grid[i])):
                if self.__grid[i][j] !='X':
                    self.__grid[i][j]=' '
    def get_grid(self):
        return self.__grid
    def get_base(self):
        return self.__base
    def set_grid(self,i,j,new_val):
        self.__grid[i][j]=new_val


