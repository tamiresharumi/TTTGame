from math import floor
from insq import insq

"""O que a classe precisa?
	- getters e setters pra todas as coisas possíveis
	- todas as regras
	- um verificador de jogo ganho
	- algum algoritmo magico pra pegar esses dados e transformar em estrategia hohoho
	- 
"""

class square:	
	def __init__(self):
		self.size = 3
		self.fields = []
		self.fields = self.fill_steps()
		
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
	move takes 3 arguments:
			- the outside square coordinate (named insq)
			- the inside square coordinate (named position)
			- the owner aka who's playing at that time
	"""
	def move(self, insq, position, owner):
		x = self.get_insquare(insq)
		sq_coord = self.int_to_coord(insq)		
		coords = self.int_to_coord(position)
		
		has_new_owner = x.set_move_to_coord(coords, owner)
		if((has_new_owner == 1) and (self.get_owner(sq_coord) == "none")):		
			print("move(", insq, position, owner, ") called this")
			print(str(owner)+" has taken #"+str(insq)+" outside sq!")			
			self.set_owner(sq_coord, owner)
			print("out | coords:", coords, "owner:",self.get_owner(sq_coord))
	
	def print_owners(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.fields[i][j]["owner"], end="  \b")
			print()
			