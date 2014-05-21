class insq:
	"""
		fields = matrix with the (duh) fields
		size = size of the inner square
		filled = number of positions filled. better than counting every damn time
	"""
	def __init__(self, size):
		self.size = size
		self.fields = self.fill_steps()
		self.filled = 0
		
	def fill_steps(self):
		sts = range(self.size)
		what = None
		list = []
		
		for i in sts:
			aux = []
			for j in sts:
				aux.append(what)
			list.append(aux)		
		return list

	def is_filled(self):
		# print("filled is", str(self.filled))
		return (self.filled==9)
		
	def is_valid_move(self, crds):
		#print("-", str(self.fields[crds[0]][crds[1]]))
		if(self.fields[crds[0]][crds[1]] == None):
			# print("-->This is", self.fields[crds[0]][crds[1]], "valid move!")
			return True
		else:
			# print("This is", self.fields[crds[0]][crds[1]], "invalid move!")
			return False
		
	"""
		só chama set_move... quando estiver tudo ok
	"""	
	def set_move_to_coord(self, array_with_coords, value):
		self.fields[array_with_coords[0]][array_with_coords[1]] = value
		self.filled+=1
		return self.check_rules(array_with_coords)		
		
	"""
		TODO checagem, tem que ser uma por uma porque senão dá errado
		primeiro linha, depois coluna, depois diagonais 
	"""
	def check_rules(self, coords):
		f = self.fields
		l = coords[0]
		c = coords[1]  #tenho preguica de digitar, mimjulgue
		win = True
		for i in range(1,self.size):
			if(f[l][i] != f[l][i-1]):
				win = False
			else:
				win = win and True
		if(win):
			return 1
		else:
			win = True
			for i in range(1,self.size):
				if(f[i][c] != f[i-1][c]):
					win = False
				else:
					win = win and True
			if(win):
				return 1
			else:
				if((l+c)%2 == 0):
					# print("[", l, c, "]é diagonal")
					if((l-c) == 0):
						# print("primária")							
						win = True
						for i in range(1,self.size):
							if(f[i-1][i-1] != f[i][i]):
								win = False
							else:
								win = win and True
						if(win):
							# print("win pela d.1")
							return 1					
					if((l+c) == 2):
						# print("secundária")
						win = True
						for i in range(1,self.size):
							# print("f[",i-1,"][",3-i,"], f[",i,"][",2-i,"]", f[i-1][3-i], f[i][2-i])
							if(f[i-1][3-i] != f[i][2-i]):
								win = False
							else:
								win = win and True
						if(win):
							# print("win pela d.2")
							return 1
						else:
							return 0
	
	def print(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.fields[i][j], end="  \b")
			print()
		