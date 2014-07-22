import random
from square import square

n = 500
p = 0
random.seed()

a = square()

x = random.randint(0,8)

r = True
for i in range(n):
	y = random.randint(0,8)
	if(i>400) or (n<250):
		print("x is", x, "y is", y, "z is", p)
	r = a.move(x,y,p)	
	if(r == 1):
		x = a.last_position
		p = p ^ 1
		if(a.is_over()):
			print("Game Over!")
			break
	else:
		if(r == -1):
			# a.print_full_square()
			x = random.randint(0,8)
		
f = open('stats', 'a')	
f.write(str(i)+" "+str(a.vms)+"\n")
f.close()

print("out in", i)
print("movements:",a.vms)
print("owners:")
print(a.print_owners())
print("full square:")
a.print_full_square()