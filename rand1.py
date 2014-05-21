import random
from square import square

n = 10
p = 0
random.seed()

a = square()

# a.move(7,3,1)
# a.move(3,3,0)
# a.move(3,3,1)

r = True
for i in range(n):
	x = random.randint(0,8)
	y = random.randint(0,8)
	r = a.move(x,y,p)	
	if(r == True):
		p = p ^ 1
		if(a.is_over()):
			print("Game Over!")
			break

# print(p)
	
# a.move(a.last_position,4,a.last_player)
# a.move(4,3,2)
# a.move(4,6,2) 
# a.move(2,0,1)
# a.move(2,1,1)
# a.move(2,2,1) # 2 pertence ao 1
# a.move(7,0,1)
# a.move(7,1,1)
# a.move(7,2,1) #7 pertence ao 1
# a.move(7,3,2)
# a.move(7,4,2)
# a.move(7,5,2) # 7 já tem dono

# a.move(3,0,2)
# a.move(3,3,2)
# a.move(3,6,2) # 3 pertence ao 2
# a.move(3,5,1)
# a.move(3,1,1)
	
# f = open('stats', 'w')
# f.write("owners:\n")
# um_print = a.print_owners()
# f.write(a.print_owners())
# f.write("\nTrials:"+str(i)+"\nFull Square:\n")
# #f.write(a.print_full_square())
# f.close()
print("movements:",a.vms)
print("owners:")
a.print_owners()
a.print_full_square()