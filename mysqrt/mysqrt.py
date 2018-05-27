
x = 0.01
s = 1.
kmax = 100
tol  = 1.e-14
for k in range(kmax):
	print("Before iteration ", k, ", s = ", s)
	s0 = s
	s = 0.5*(s + x/s)
	delta_s = s - s0
	if abs(delta_s/x) < tol:
		break
print("After ", k+1, " iteration, s = ", s)