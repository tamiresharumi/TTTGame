class insq:

	def __init__(self, size):
		self.size = size
		self.fields = self.fill_steps()
		# self.rules = self.fields[1]
		
	def fill_steps(self):
		sts = range(self.size)
		what = None
		list = []
		
		for i in sts:
			aux = []
			for j in sts:
				aux.append(what)
			list.append(aux)
		#print(list)		
		return list

	# def set_value(self, array_with_coords, value):
	def set_move_to_coord(self, array_with_coords, value):
		ret = 0
		field = self.fields[array_with_coords[0]][array_with_coords[1]]
		if(self.fields[array_with_coords[0]][array_with_coords[1]] == None):
			self.fields[array_with_coords[0]][array_with_coords[1]] = value
			ret = self.check_rules(array_with_coords)
		else:
			print("POSITION ALREADY IN USE U NO GET IT")		
		return ret
		
		
	"""TODO checagem, tem que ser uma por uma porque senão dá errado
		primeiro linha, depois coluna, depois diagonais """
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
			return 0
	
	def print(self):
		# print(self.fields)
		for i in range(self.size):
			for j in range(self.size):
				# print(self.fields[i][j], " ")
				#sys.stdout.write(self.fields+' \b')
				print(self.fields[i][j], end="  \b")
			print()
		