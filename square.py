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
			
	def is_valid_move(self, insq, coords, player):
		x = self.get_insquare(insq)
		if((self.last_player != player) and ((self.last_position == insq)or(self.last_position==None))):			
			return True
		else:
			y = self.get_insquare(self.last_position)
			c = self.int_to_coord(coords)
			if(y.is_filled()):
				return True			
			if(x.is_filled()):
				return False
			else:
				print("insq")
				return x.is_valid_move(c)
		
		
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
			if(self.is_valid_move(insq, position, owner)):
				if(__CDATA__):
					self.f.write("a.move("+str(insq)+","+str(position)+","+str(owner)+")\n")
				self.last_player = owner
				self.last_position = position
				has_new_owner = x.set_move_to_coord(coords, owner)
				self.vms+=1
				if((has_new_owner == 1) and (self.get_owner(sq_coord) == "none")):	
					self.set_owner(sq_coord, owner)
				return True 
			# else:				
				# if(__CDATA__):
					#self.f.write("--"+str(insq)+" "+str(position)+" "+str(owner)+"\n")
				
		else:
			if((__CDATA__)&(self.f.closed==False)):
				self.f.close()
			return False
	
		
			
	def print_owners(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.fields[i][j]["owner"], end="  \b")
			print()

			
	def print_full_square(self):
		for i in range(self.size):
			for j in range(self.size):
				for k in range(self.size):
					for l in range(self.size):
						print("%4s" %(self.fields[i][k]["inner_sq"].fields[j][l]), end="  \b")
					print("|", end="  \b")
				print("")
			print("-"*49)