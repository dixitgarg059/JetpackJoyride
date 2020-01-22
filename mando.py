import time
from obstacle import Obstacle
from bullet import Bullet
from os import system
# import pyfiglet
import colorama
from colorama import Back as bg, Fore as fg,Style


class Mando:
	def __init__(self,i,j,tt):
		self.__posi=i
		self.__mat=[[' ','o',' '],['-','|','-'],['/',' ','\\']]
		self.__matd1=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', '^', ' ', ' ', '^'], [' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', '\\', '/'], [' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', '-', '-', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
		self.__matd2=[['-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '^', ' ', ' ', '^'], [' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '\\', '/'], [' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' '], [' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
		self.__cur=self.__mat
		self.__dragon=False
		# self.__mat=[[' ', '\\', '\\', '\\', '|', '|', '|', '/', '/', '/'], [' ', '.', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', ' '], ['/', ' ', '\\', '|', ' ', 'O', ' ', ' ', ' ', 'O', ' ', '|'], ['\\', ' ', '/', ' ', '\\', '`', '_', '_', '_', "'", '/', ' '], [' ', '#', ' ', ' ', ' ', '_', '|', ' ', '|', '_'], ['(', '#', ')', ' ', '(', ' ', ' ', ' ', ' ', ' ', ')', ' ', ' '], [' ', '#', '\\', '/', '/', '|', '*', ' ', '*', '|', '\\', '\\', ' '], [' ', '#', '\\', '/', '(', ' ', ' ', '*', ' ', ' ', ')', '/', ' ', ' ', ' '], [' ', '#', ' ', ' ', ' ', '=', '=', '=', '=', '=', ' ', ' '], [' ', '#', ' ', ' ', ' ', '(', ' ', 'U', ' ', ')', ' '], [' ', '#', ' ', ' ', ' ', '|', '|', ' ', '|', '|'], ['.', '#', '-', '-', '-', "'", '|', ' ', '|', '`', '-', '-', '-', '-', '.'], ['`', '#', '-', '-', '-', '-', "'", ' ', '`', '-', '-', '-', '-', '-', "'"]]
		# self.__mat=[[' ', ' ', ' ', ' ', '.', '-', ',', ';', '=', "'", "'", ';', '_', ')', ',', '-', '.'], [' ', ' ', ' ', ' ', ' ', '\\', '_', '\\', '(', ')', ',', '(', ')', '/', '_', '/'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', ',', '_', '_', '_', ',', ')'], [' ', ' ', ' ', ' ', ' ', ' ', ',', '-', '/', '`', '~', '`', '\\', '-', ',', '_', '_', '_'], [' ', ' ', ' ', ' ', ' ', '/', ' ', '/', ')', '.', ':', '.', '(', "'", '-', '-', '.', '_', ')'], [' ', ' ', ' ', ' ', '{', '_', '[', ' ', '(', '_', ',', '_', ')'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'Y', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|', ' ', '\\'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', '"', '"', ' ', '"', '"', '"']]

		# self.__matd2=
		self.__mat2=[['|','o','|'],['-','|','-'],['/','|','\\']]
		# self.__mat2=[['|','o','|'],['-','|','-'],['/','|','\\']]
		self.__is_shield=False
		self.__shield_time=0.0
		self.__shield_finish_time=-70
		self.__i=i
		self.__change_time=0
		self.__j=j
		self.__points=0
		self.__timeremaining=tt
		self.__lives=5
		self.__speed_boost_time=time.time()-5
	def getx(self):
		return self.__i
	def gety(self):
		return self.__j
	def check_dragon(self,obj,st0):
		# return 1
		grid=obj.get_grid()
		for i in range(0,3):
			for j in range(0,3):
				if grid[i+self.__i][j+self.__j+st0]=='<':
					return 1
		return 0	
	def detect_colision(self,obj,st0):
		# speed_boost=False
		grid=obj.get_grid()
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				if i + self.__i < 55:
					if grid[i+self.__i][j+self.__j+st0]	=='*':
						self.__points=self.__points+1

		ans=0
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				grid=obj.get_grid()
				base=obj.get_base()
				if grid[i+self.__i][j+self.__j+st0] !=' ' and grid[i+self.__i][j+self.__j+st0]!='*' and grid[i+self.__i+st0][j+self.__j+st0]!='X' and grid[i+self.__i+st0][j+self.__j+st0]!='o' and grid[i+self.__i][j+self.__j+st0]!='@' and grid[i+self.__i][j+self.__j+st0]!='#' and grid[i+self.__i][j+self.__j+st0]!='<' and grid[i+self.__i][j+self.__j+st0]!='%':
					base[i+self.__i][j+self.__j+st0][0].destroy(obj)
					# ans=1:
					ans=1
				if grid[i+self.__i][j+self.__j+st0]=='@':
					self.__dragon=True
		if self.__is_shield:
			ans=0
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				if grid[i+self.__i][j+self.__j+st0] !=' ' and grid[i+self.__i][j+self.__j+st0]!='X' and grid[i+self.__i][j+self.__j+st0]!='*' and grid[i+self.__i][j+self.__j+st0]!='#' and grid[i+self.__i][j+self.__j+st0]!='<' and grid[i+self.__i][j+self.__j+st0]!='%':
					base[i+self.__i][j+self.__j+st0][0].destroy(obj)
		if ans == 1 and self.__dragon:
			self.__dragon=False
			ans=0

		return ans
	def detect_magnet(self,obj,st,st0):
		grid=obj.get_grid()
		base=obj.get_base()
		ret={
		"move_right" : False,
		"move_left"  : False,
		"move_up"    : False,
		"move_down"  : False
		}
		# flg=0
		# for i in range(0,3):
			# for j in range(0,3):
				# if grid[i+self.__i][j+self.__j+st0]=='#':
					# flg=1
		# if flg==1:
			# return ret
		for i in range(-10,10+len(self.__cur)):
			for j in range(0,40):
				if i + self.__i < 55 and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:
					if grid[i+self.__i][j+self.__j]=='#':
						ret["move_right"]=True
				if i + self.__i < 55 and  self.__j -j < 201 + st and i + self.__i >=0 and self.__j -j >=0:
					if grid[i+self.__i][self.__j-j]=='#':
						ret["move_left"]=True
		for j in range(-10,10+len(self.__cur[0])):
			for i in range(0,20):
				if i + self.__i < 55  and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:				
					if grid[self.__i+i][self.__j+j]=='#':
						ret["move_down"]=True
				if  self.__i -i < 55  and j + self.__j < 201 + st and i + self.__i >=0 and j + self.__j >=0:
					if grid[self.__i-i][self.__j+j]=='#':
						ret["move_up"]=True



		return ret
	def detect_dragon_mode(self,obj):
		grid=obj.get_grid()
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				if grid[i+self.__i][j+self.__j]=='@':
					return 1
		return 0
	def move_right(self,inc,st,board,dragon_finished):
		# inc=10
		self.__timeremaining=self.__timeremaining-0.05
		if self.__j +inc+len(self.__mat)-1 < st+201:
			self.__j=self.__j+inc
		elif dragon_finished:
			system('clear')
			print("YOU WON")
			quit()
	def move_left(self,st,board,st0=0):
		if self.__j +st0 >st+3:
			# flg=True
			# j=0
			# for i in range(0,2):
			# 	if board.grid[self.__i][self.__j-i] !='#':
			# 		flg=False
			# 		j=i
			self.__j=self.__j-3
			# if self.__detect_colision(self.__i,self,j-2,board) == 1 :
				# quit()
	def move_up(self,board):

		if self.__i >11:
			# flg=True
			# j=0
			# for i in range(0,5):
			# 	if board.grid[self.__i-i][self.__j] !='#':
			# 		j=i
			# 		flg=False
			
			self.__i=self.__i-2
			# if self.__detect_colision(self.__i-5,self.__j,board) == 1:
				# quit()
	def move_down(self,board,t):
 			self.__i=self.__i+int((5*t-5)/2)
 			# if self.__i > 55-len(self.__cur)-1:
 				# self.__i=55-len(self.__cur)-1

 			self.__i = self.__i + 1
 			if self.__i > 55 -len(self.__cur)-1:
 				self.__i = 55 - len(self.__cur)-1

 			# self.__i=54
 			# flg=True
 			# for i in range(0,1):
 			# 	if board.grid[self.__i+i][self.__j]!='#':
 			# 		flg=False
 			# if flg:
 			# if self.__detect_colision(self.__i+1,self.__j,board) == 1:
 				# quit()
	def shield(self,obj,val):
		if self.__is_shield:
			return 
		if (int(time.time() - self.__shield_finish_time))>= 60:
			self.__is_shield=val
			self.__shield_time=time.time()
			if self.__cur == self.__mat:
				self.__cur=self.__mat2
		# for i in range(0,3):
		# 	for j in range(0,3):
		# 		obj.grid[self.__i+i][self.__j+j]=self.__mat2[i][j]
	def detect_shield(self):
		if self.__is_shield == False:
			if self.__cur == self.__mat2:
				self.__cur=self.__mat
			return 
		diff=int(time.time()-self.__shield_time)
		if diff >= 10:
			self.__is_shield=False
			self.__shield_finish_time=time.time()
			if self.__cur == self.__mat2:
				self.__cur=self.__mat

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
		# self.__i,self.__j+2
		bt=Bullet(self.__i,self.__j+2)
		return bt
		
	def add_to_board(self,obj,st,st0=0,dragon_came=False,dragon_lives=4):
		self.dragon_mode()
		print('\033[0;0H',end='')
		print(fg.WHITE,end='')
		print(Style.BRIGHT,end='')
		print("SCORE : ",end='')
		s=str(self.__points)
		l=st

		for i in s:
			obj.set_grid(0,l,' ')
			# obj.grid[0][l]=' '
			print(i,end='')
			l=l+1
		for i in range(0,5):
			print(' ',end='')
		print('TIME REMAINING :',end='')
		s=str(int(self.__timeremaining))
		print(s,end='')
		print(" LIVES : ",end='')
		print(self.__lives,end='')
		c=0
		if dragon_came:
			print("     DRAGON LIVES : ",end='')
			print(dragon_lives,end='')
			c=22

		# else:	

		if self.__is_shield:
			print("    SHIELD ACTIVATED : ",end='')
			print(10-(int)(time.time()-self.__shield_time),end='')
			for i in range(0,136-c):
				print(' ',end='')
		else:	
			for i in range(0,161-c):
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
		# print()
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				if self.__is_shield:
					obj.set_grid(self.__i+i,self.__j+j+st0,self.__cur[i][j])
				else:
					obj.set_grid(self.__i+i,self.__j+j+st0,self.__cur[i][j])

	def remove_from_board(self,obj,st0=0):
		# grid=obj.get_grid()
		for i in range(0,len(self.__cur)):
			for j in range(0,len(self.__cur[i])):
				obj.set_grid(self.__i+i,self.__j+j+st0,' ')
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

			result="TIMEOUT"
		else:
			result = "GAME OVER" 
		print(result) 
		quit()
	def detect_dragon(self,i):
		if self.__i > i :
			return 1
		elif self.__i < i:
			return -1
		else: 
			return 0

	def isshield(self):
		if self.__is_shield:
			return True
		else:
			return False

	def dragon_mode(self):
		if self.__dragon == True:
			if self.__cur == self.__matd1:
				if time.time()-self.__change_time >=0.5:
					self.__cur=self.__matd2
					self.__change_time=time.time()

			elif self.__cur == self.__matd2:
				if time.time()-self.__change_time >=0.5:
					self.__cur = self.__matd1
					self.__change_time=time.time()

			else:
				self.__cur=self.__matd1
				self.__change_time=time.time()
		else:
			if self.__cur == self.__matd1 or self.__cur == self.__matd2:
				self.__cur=self.__mat

	def dragon_mode_finish(self):
		self.__cur=self.__mat

	def is_in_dragon_mode(self):
		if self.__cur == self.__matd1 or self.__cur == self._matd2:
			return 1
		return 0
