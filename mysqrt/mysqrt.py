
x = 4.
s = 1.
for k in range(6):
	print("Before iteration ", k, ", s = ", s)
	s = 0.5*(s + x/s)
print("After ", k+1, " iteration, s = ", s)