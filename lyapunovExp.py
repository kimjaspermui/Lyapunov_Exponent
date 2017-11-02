import math

lam = 0
N = 4000
r = 4.0
x = 0.5

def getNextX(r, x):
	return r * x * (1 - x)

def getLambda(N, r, x0):
	xn = x0
	tempSum = 0
	for i in range(N):
		inside = abs(r - 2 * r * xn)
		if inside != 0:
			tempSum += math.log(inside, 2)
		else:
			print("have 0 log")
		xn = getNextX(r, xn)
	return tempSum / N

print(getLambda(N, r, x))