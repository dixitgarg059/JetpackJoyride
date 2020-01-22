class Bullet:
	def __init__(self,i,j):
		self._i=i             # protected variables to enable inheritance
		self._j=j
		self._mat=[['X']]
	def detect_colision(self,obj,st0):	
		ans=0
		grid=obj.get_grid()
		base=obj.get_base()
		for i in range(0,1):
			for j in range(-3,3):
				if grid[i+self._i][j+self._j+st0] !=' ' and grid[i+self._i][j+self._j+st0]!='*' and grid[i+self._i][j+self._j+st0]!='o' and grid[i+self._i][j+self._j+st0]!='@' and grid[i+self._i][j+self._j+st0]!='#':
					ans=1
		for i in range(0,1):
			for j in range(-3,3):
				if grid[i+self._i][j+self._j+st0] !=' ' and grid[i+self._i][j+self._j+st0]!='*' and grid[i+self._i][j+self._j+st0]!='o' and grid[i+self._i][j+self._j+st0]!='@' and grid[i+self._i][j+self._j+st0]!='#':
					if len(base[i+self._i][j+self._j+st0]) == 1:
						base[i+self._i][j+self._j+st0][0].destroy(obj)


		return ans
	def move_right(self,inc,st,st0):
		if self._j +5+2 +st0 < st+201:
			self._j=self._j+5
			return 1
		else:
			return 0

	def add_to_board(self,obj,st=0,st0=0):
		grid=obj.get_grid()
		leave=['*','#','@']
		while grid[self._i][self._j] in leave:
			self._j=self._j+1
		for i in range(0,len(self._mat)):
			for j in range(0,len(self._mat[i])):
				obj.set_grid(self._i+i,self._j+j+st0+st,self._mat[i][j])

	def remove_from_board(self,obj,st=0,st0=0):
		grid=obj.get_grid()
		for i in range(0,len(self._mat)):
			for j in range(0,len(self._mat[i])):
				obj.set_grid(self._i+i,self._j+st+j+st0,' ')


