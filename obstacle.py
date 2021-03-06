class Obstacle:
	def __init__(self,i,j,mode,obj):
		self.__i=i
		self.__j=j
		self.__mode=mode
		if mode==0:
			self.__mat=[[' ',' ',' ',' ','/'],[' ',' ',' ','/',' '],[' ',' ','/',' ',' '],[' ','/',' ',' ',' '],['/',' ',' ',' ',' ']]
		elif mode == 1:
			self.__mat=[['\\',' ',' ',' ',' '],[' ','\\',' ',' ',' '],[' ',' ','\\',' ',' '],[' ',' ',' ','\\',' '],[' ',' ',' ',' ','\\']]
		elif mode == 2:
			self.__mat=[[' ','|',' '],[' ','|',' '],[' ','|',' '],[' ','|',' ']]
		elif mode == 3:
			self.__mat=[[' ',' ',' ',' ',' ',' ',' '],['-','-','-','-','-','-','-'],['-','-','-','-','-','-','-']]
		elif mode==4 or mode == 5:
			self.__mat=[[' ', ' ', '*', '*', '*', ' ', ' '], [' ', '*', ' ', '*', ' ', '*', ' '], ['*', ' ', '*', ' ', '*', ' ', '*'], ['*', ' ', '*', '*', '*', ' ', '*'], [' ', '*', '*', '*', '*', '*', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

		elif  mode == 6:
			self.__mat=[['#','#','#'],['#','#','#'],['#','#','#']]
		elif mode == 7:
			self.__mat=[['*','*',' ','*','*',' ','*','*',' ','*','*'],['*','*',' ','*','*',' ','*','*',' ','*','*'],['*','*',' ','*','*',' ','*','*',' ','*','*']] # for coins
		elif mode == 8:
			self.__mat=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', '%', '%', '%', '%', '%'], [' ', ' ', '%', '%', ' ', '%', ' ', '%', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', '%'], [' ', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', ' ', '%', '%'], ['%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%'], [' ', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%'], [' ', ' ', ' ', '%', '%', ' ', '%', ' ', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', ' ', '%', ' ', '%', '%']]
		elif mode ==9:
			self.__mat=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', ' ', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', '%', '%', ' ', ' ', '%', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', ' ', ' ', '%', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', '%', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', '%', '%', '%', '%', ' ', ' ', '%', '%', '%', ' ', ' ', ' ', ' ', '%', ' ', '%', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', '%', ' ', ' ', ' ', ' ', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', ' ', '%', '%', ' ', ' ', ' ', '%', ' ', ' ', ' ', '%', ' ', '%', '%', ' ', ' ', '%', ' ', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['%', ' ', ' ', ' ', '%', '%', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '%', ' ', '%', ' ', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', '%', ' ', ' ', '%', ' ', ' ', ' ', ' ', ' ', '%', ' ', ' ', ' ', '%', ' ']]
		elif mode == 10:
			self.__mat=[['@','@','@','@','@'],['@','@','@','@','@'],['@','@',' ','@','@'],['@','@',' ','@','@'],['@','@',' ','@','@'],['@','@','@','@','@'],['@','@','@','@','@']]

		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				obj.set_grid(self.__i+i,self.__j+j,self.__mat[i][j])
	def destroy(self,obj):
		for i in range(0,len(self.__mat)):
			for j in range(0,len(self.__mat[i])):
				obj.set_grid(self.__i+i,self.__j+j,' ')


	def get_mat(self):
		return self.__mat