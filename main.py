from classes import *

principal = Memory(256)
cache = CacheMemory(16)

for i in principal.cells:
	print(i.adress, i.content)


while True:
	op = int(input("MENU\n1- Ler Memoria\n2- Escrever Memoria\n3- Estatisticas\n4- Sair\nOpcao: "))
	print(chr(27) + "[2J")
	if op == 1:
		pass
	elif op == 2:
		pass
	elif op == 3:
		pass
	else:
		break