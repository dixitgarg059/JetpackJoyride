import time
from obstacle import Obstacle
from bullet import Bullet
from os import system
import pyfiglet
import colorama
from colorama import Back as bg, Fore as fg,Style


class Mando:
	def __init__(self,i,j,tt):
		self.__posi=i
		self.__mat=[[' ','o',' '],[' ','|',' '],['/','|','\\']]
		# self.__mat=[[' ', '\\', '\\', '\\', '|', '|', '|', '/', '/', '/'], [' ', '.', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', ' '], ['/', ' ', '\\', '|', ' ', 'O', ' ', ' ', ' ', 'O', ' ', '|'], ['\\', ' ', '/', ' ', '\\', '`', '_', '_', '_', "'", '/', ' '], [' ', '#', ' ', ' ', ' ', '_', '|', ' ', '|', '_'], ['(', '#', ')', ' ', '(', ' ', ' ', ' ', ' ', ' ', ')', ' ', ' '], [' ', '#', '\\', '/', '/', '|', '*', ' ', '*', '|', '\\', '\\', ' '], [' ', '#', '\\', '/', '(', ' ', ' ', '*', ' ', ' ', ')', '/', ' ', ' ', ' '], [' ', '#', ' ', ' ', ' ', '=', '=', '=', '=', '=', ' ', ' '], [' ', '#', ' ', ' ', ' ', '(', ' ', 'U', ' ', ')', ' '], [' ', '#', ' ', ' ', ' ', '|', '|', ' ', '|', '|'], ['.', '#', '-', '-', '-', "'", '|', ' ', '|', '`', '-', '-', '-', '-', '.'], ['`', '#', '-', '-', '-', '-', "'", ' ', '`', '-', '-', '-', '-', '-', "'"]]
		# self.__mat=[[' ', ' ', ' ', ' ', '.', '-', ',', ';', '=', "'", "'", ';', '_', ')', ',', '-', '.'], [' ', ' ', ' ', ' ', ' ', '\\', '_', '\\', '(', ')', ',', '(', ')', '/', '_', '/'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', ',', '_', '_', '_', ',', ')'], [' ', ' ', ' ', ' ', ' ', ' ', ',', '-', '/', '`', '~', '`', '\\', '-', ',', '_', '_', '_'], [' ', ' ', ' ', ' ', ' ', '/', ' ', '/', ')', '.', ':', '.', '(', "'", '-', '-', '.', '_', ')'], [' ', ' ', ' ', ' ', '{', '_', '[', ' ', '(', '_', ',', '_', ')'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'Y', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|', ' ', '\\'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', '"', '"', ' ', '"', '"', '"']]


		self.__mat2=self.__mat
		# self.__mat2=[['|','o','|'],['-','|','-'],['/','|','\\']]
		self.__is_shield=False
		self.__shield_time=0.0
		self.__shield_finish_time=-70
		self.__i=i
		self.__j=j
		self.__points=0
		self.__timeremaining=tt
		self.__lives=5
		self.__speed_boost_time=time.time()-5

	def detect_colision(self,obj):
		# speed_boost=False
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				if obj.grid[i+self.__i][j+self.__j]=='*':
					self.__points=self.__points+1

		ans=0
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				if obj.grid[i+self.__i][j+self.__j] !=' ' and obj.grid[i+self.__i][j+self.__j]!='*' and obj.grid[i+self.__i][j+self.__j]!='X' and obj.grid[i+self.__i][j+self.__j]!='o' and obj.grid[i+self.__i][j+self.__j]!='@':
					# ans=1:
					ans=1
		if self.__is_shield:
			ans=0
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				if obj.grid[i+self.__i][j+self.__j] !=' ' and obj.grid[i+self.__i][j+self.__j]!='X' and obj.grid[i+self.__i][j+self.__j]!='*' and obj.grid[i+self.__i][j+self.__j]!='@':
					obj.base[i+self.__i][j+self.__j][0].destroy(obj)
		return ans
	def detect_magnet(self,obj,st):
		ret={
		"move_right" : False,
		"move_left"  : False,
		"move_up"    : False,
		"move_down"  : False
		}
		for i in range(-10,10+len(self.__mat)):
			for j in range(0,40):
				if i + self.__i < 55 and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:
					if obj.grid[i+self.__i][j+self.__j]=='#':
						ret["move_right"]=True
				if i + self.__i < 55 and  self.__j -j < 201 + st and i + self.__i >=0 and self.__j -j >=0:
					if obj.grid[i+self.__i][self.__j-j]=='#':
						ret["move_left"]=True
		for j in range(-10,10+len(self.__mat[0])):
			for i in range(0,40):
				if i + self.__i < 55  and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:				
					if obj.grid[self.__i+i][self.__j+j]=='#':
						ret["move_down"]=True
				if  self.__i -i < 55  and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:
					if obj.grid[self.__i-i][self.__j+j]=='#':
						ret["move_up"]=True



		return ret
	def detect_speed_boost(self,obj):
		if (time.time()-self.__speed_boost_time) <= 4:
			return 1
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				if obj.grid[i+self.__i][j+self.__j]=='@':
					self.__speed_boost_time=time.time()
					return 1
		return 0
	def move_right(self,inc,st,board):
		self.__timeremaining=self.__timeremaining-0.05
		if self.__j +inc+2 < st+201:
			self.__j=self.__j+inc
			# if  self.__detect_colision(self.__i,self.__j+inc,board) == 1:
				# quit()
	def move_left(self,st,board):
		if self.__j >st+2:
			self.__j=self.__j-2
			# if self.__detect_colision(self.__i,self,j-2,board) == 1 :
				# quit()
	def move_up(self,board):
		if self.__i >6:
			self.__i=self.__i-5
			# if self.__detect_colision(self.__i-5,self.__j,board) == 1:
				# quit()
	def move_down(self,board):
 		if self.__i <= self.__posi-1:
 			self.__i=self.__i+1
 			# if self.__detect_colision(self.__i+1,self.__j,board) == 1:
 				# quit()
	def shield(self,obj,val):
		if self.__is_shield:
			return 
		if (int(time.time() - self.__shield_finish_time))>= 60:
			self.__is_shield=val
			self.__shield_time=time.time()
		# for i in range(0,3):
		# 	for j in range(0,3):
		# 		obj.grid[self.__i+i][self.__j+j]=self.__mat2[i][j]
	def detect_shield(self):
		if self.__is_shield == False:
			return 
		diff=int(time.time()-self.__shield_time)
		if diff >= 10:
			self.__is_shield=False
			self.__shield_finish_time=time.time()

	def decrease_lives(self):
		self.__lives=self.__lives-1
		if self.__lives == 0:
			return 0
		else:
			return 1
	def on_ground(self):
		if self.__i == 51:
			return 1
		return 0
	def fire(self):
		bt=Bullet(self.__i,self.__j+2)
		return bt
		
	def add_to_board(self,obj,st):
		print('\033[0;0H',end='')
		print(fg.WHITE,end='')
		print("SCORE : ",end='')
		s=str(self.__points)
		l=st
		for i in s:
			obj.grid[0][l]=' '
			print(i,end='')
			l=l+1
		for i in range(0,5):
			print(' ',end='')
		print('TIME REMAINING :',end='')
		s=str(int(self.__timeremaining))
		print(s,end='')
		print(" LIVES : ",end='')
		print(self.__lives,end='')
		if self.__is_shield:
			print("    SHIELD ACTIVATED : ",end='')
			print(10-(int)(time.time()-self.__shield_time),end='')
			for i in range(0,136):
				print(' ',end='')
		else:	
			for i in range(0,161):
				print(' ',end='')
			# for i in range(0,90):
				# print(' ',end='')
			# print()
		# else:
			# for i in range(0,167):
				# print(' ',end='')
			# print()
		# print("helloworld")
		# print('\033[1;0H')
		c=1
		for i in range(0,200):
			if c==1:
				print(fg.MAGENTA,end='')
				c=0
			elif c==0:
				print(fg.WHITE,end='')
				c=1
			print('X',end='')
		print()
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				if self.__is_shield:
					obj.grid[self.__i+i][self.__j+j]=self.__mat2[i][j]
				else:
					obj.grid[self.__i+i][self.__j+j]=self.__mat[i][j]

	def remove_from_board(self,obj):
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				obj.grid[self.__i+i][self.__j+j]=' '
	def timeout(self):
		if int(self.__timeremaining) >0:
			return 1
		return 0
	def game_over(self,timeout=False):
		system('clear')
		print("YOUR SCORE : ",end='')
		print(self.__points)
		result=0
		if timeout:
			result=pyfiglet.figlet_format("TIMEOUT")
		else:
			result = pyfiglet.figlet_format("GAME OVER") 
		print(result) 
		quit()
