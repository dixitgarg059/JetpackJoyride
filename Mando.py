class Mando:
	def __init__(self,i,j):
		self.mat=[[' ','o',' '],[' ','|',' '],['/','|','\\']]
		self.i=i
		self.j=j
	def move_right(self):
		if j < 80:
			self.j=self.j+5
		else:
			j=80
	def move_left(self):
		if j >0:
			self.j=self.j-1
		else:
			j=0
	def move_up(self):
		if i >0:
			self.i=self.i-1
		else:
			i=0
	def add_to_board(self,obj):
		for i in range(0,self.i):
			for j in range(0,self.j):
				obj.grid[self.i+i][self.j+j]=self.mat[i][j]
