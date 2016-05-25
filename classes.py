from random import *

class MemoryCell:
	def __init__(self, adr, cont):
		self.content = cont
		self.adress = adr

class Square:
	def __init__(self):
		self.label = ""
		self.adress0 = ""
		self.adress1 = None
		self.content = None

class Memory:
	def __init__(self, number):
		self.cells = []
		for i in range(number):
			c = MemoryCell(format(i,"08b"),randint(200000,9999999))
			self.cells.append(c)
			
class CacheMemory:
	def __init__(self,number):
		self.squares = []
		for i in range(number):
			self.squares.append(Square())