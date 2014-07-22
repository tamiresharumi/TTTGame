from math import floor
from insq import insq

"""O que a classe precisa?
	- getters e setters pra todas as coisas possíveis
	- todas as regras
	- um verificador de jogo ganho
	- algum algoritmo magico pra pegar esses dados e transformar em estrategia hohoho
	- uma variavel pra controlar quem jogou onde
"""
__CDATA__= True
class square:	
	def __init__(self):
		self.size = 3
		self.last_player = None
		self.last_position = None
		self.vms = 0
		self.fields = []
		self.fields = self.fill_steps()
		if(__CDATA__):
			self.f = open('data', 'w')
		
	def fill_steps(self):
		sts = range(self.size)
		what = []
		list = []		
		for i in sts:
			aux = []
			for j in sts:
				aux.append(what)
			list.append(aux)
		for i in sts:
			for j in sts:
				list[i][j] = {"owner": "none", "inner_sq":insq(self.size)}
		return list
	
	def int_to_coord(self,int):
		x = floor(int/self.size)
		y = int%self.size
		return [x,y]
	
	def coord_to_int(self, coord):
		return coord[0]*self.size+coord[1]
	
	def get_insquare(self, position):
		coord = self.int_to_coord(position)
		return self.fields[coord[0]][coord[1]]["inner_sq"]
	
	def get_owner(self, array_with_coords):
		return self.fields[array_with_coords[0]][array_with_coords[1]]["owner"]
		
	def set_owner(self, array_with_coords, owner):
		self.fields[array_with_coords[0]][array_with_coords[1]]["owner"] = owner
			
	"""
		Todas chora com essa classe :(
	"""
	def is_valid_move(self, insq, coords, player):
		x = self.get_insquare(insq)
		c = self.int_to_coord(coords)
		if(x.is_valid_move(c) == False): 
			y = self.get_insquare(self.last_position)
			i_f = x.is_filled()
			# print("this is filled is", i_f)
			if(i_f == True):
				# print("return -1")
				return -1
			else:
				# print("return 0")
				return 0
		else:
			# print("WTF", end="   \b")
			if((self.last_position == insq) or (self.last_position==None) or (self.get_insquare(self.last_position).is_filled())): 
				# print("return 1")
				return 1
			else:
				# print("return 0")
				return 0
		
	def is_over(self):
		return (self.vms==81)
		
	"""
		move takes 3 arguments:
			- the outside square coordinate (named insq)
			- the inside square coordinate (named position)
			- the owner aka who's playing at that time
	"""
	def move(self, insq, position, owner):
		if(self.is_over()==False):
			x = self.get_insquare(insq)
			sq_coord = self.int_to_coord(insq)		
			coords = self.int_to_coord(position)
			k = (self.is_valid_move(insq, position, owner))
			# print("a.move("+str(insq)+","+str(position)+","+str(owner)+")\nk is", k, "\n")
			if(k == 1):
				if(__CDATA__):
					self.f.write("i:"+str(insq)+" p:"+str(position)+" o:"+str(owner)+"\n")
					#self.f.write("a.move("+str(insq)+","+str(position)+","+str(owner)+")\nprint('a.move("+str(insq)+","+str(position)+","+str(owner)+")')\na.print_full_square()\n")
					
				self.last_player = owner
				self.last_position = position
				has_new_owner = x.set_move_to_coord(coords, owner)
				self.vms+=1
				if((has_new_owner == 1) and (self.get_owner(sq_coord) == "none")):	
					self.set_owner(sq_coord, owner)
				return 1
			else:
				return k
		else:
			if((__CDATA__) and (self.f.closed==False)):
				self.f.close()
			return 0
	
		
			
	def print_owners(self):
		string = ""
		for i in range(self.size):
			for j in range(self.size):
				string+='{:5s}'.format(str(self.fields[i][j]["owner"]))
			string+="\n"
				# print(str(self.fields[i][j]["owner"]), end="  \b")
			# print()
		return string

			
	def print_full_square(self):
		if(__CDATA__):
			string = ""
			string+=("-"*49)+'\n'
			for i in range(self.size):
				for j in range(self.size):
					for k in range(self.size):
						for l in range(self.size):
							string+='{:5s}'.format(str(self.fields[i][k]["inner_sq"].fields[j][l]))
						string+='|'
					string+='\n'
				string+=("-"*49)+'\n'
			string+='\n'
			return string
		else:
			print("-"*49)
			for i in range(self.size):
				for j in range(self.size):
					for k in range(self.size):
						for l in range(self.size):
							print("%4s" %(self.fields[i][k]["inner_sq"].fields[j][l]), end="  \b")
						print("|", end="  \b")
					print("")
				print("-"*49)
			print("")