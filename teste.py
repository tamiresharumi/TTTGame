from square import square

a = square()
# a.graphic_print()

#Teste de conversao de coordenadas
# b = a.int_to_coord(4)
# print(b)
# c = a.coord_to_int(b)
# print(c)

#teste da inner square
#print(a.fields)
# print(a.get_insquare(5))
# b = a.get_insquare(5)
# b."inner_sq"[1][2] = 1
# b["inner_sq"][1][2] = 1
# print(a.fields)
# a.move(6,0,2)
# a.get_insquare(6).print()
# print(a.fields)
# a.print()

#teste de regras
# b = a.get_insquare(4)
# b.rules[1] = 2
# print(b.rules)
# a.move(4,3,2)
#a.print_owners()
# a.move(4,4,2)
# a.move(4,5,2)
# a.move(4,5,2)
# a.move(2,0,1)
# a.move(2,1,1)
# a.move(2,2,1)
a.move(7,0,1)
a.move(7,1,1)
a.move(7,2,1)
a.move(7,3,2)
a.move(7,4,2)
a.move(7,5,2)

a.move(3,0,2)
a.move(3,3,2)
a.move(3,6,2)
a.move(3,5,1)
a.move(3,1,1)
# 
a.print_owners()