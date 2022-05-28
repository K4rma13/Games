for x in range(50):
	for y in range(50):
		if (x-25)**2 + (y-25)**2 <= 25:
			print("X",end="")
		else:
			print(" ",end="")
	print()