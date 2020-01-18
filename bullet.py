class Bullet:
	def __init__(self,i,j):
		self.__i=i
		self.__j=j
		self.__mat=[['X']]
	def detect_colision(self,obj):	
		ans=0
		for i in range(0,1):
			for j in range(-3,3):
				if obj.grid[i+self.__i][j+self.__j] !=' ' and obj.grid[i+self.__i][j+self.__j]!='*' and obj.grid[i+self.__i][j+self.__j]!='o' and obj.grid[i+self.__i][j+self.__j]!='@' and obj.grid[i+self.__i][j+self.__j]!='#':
					ans=1
		for i in range(0,1):
			for j in range(-3,3):
				if obj.grid[i+self.__i][j+self.__j] !=' ' and obj.grid[i+self.__i][j+self.__j]!='*' and obj.grid[i+self.__i][j+self.__j]!='o' and obj.grid[i+self.__i][j+self.__j]!='@' and obj.grid[i+self.__i][j+self.__j]!='#':
					if len(obj.base[i+self.__i][j+self.__j]) == 1:
						obj.base[i+self.__i][j+self.__j][0].destroy(obj)


		return ans
	def move_right(self,inc,st,board):
		# self.__timeremaining=self.__timeremaining-1
		if self.__j +5+2 < st+201:
			self.__j=self.__j+5
			return 1
		else:
			return 0

	def add_to_board(self,obj,st):
		leave=['*','#','@']
		while obj.grid[self.__i][self.__j] in leave:
			self.__j=self.__j+1
		
		obj.grid[self.__i][self.__j]='X'

	def remove_from_board(self,obj):
		for i in range(0,1):
			for j in range(0,1):
				obj.grid[self.__i+i][self.__j+j]=' '


