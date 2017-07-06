""" Fibonacci Recursive """

def fibrec(n):
	return n if n < 2 else fibrec(n - 2) + fibrec(n - 1)

""" Fibonacci Memoization"""
def fibmem(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

print(fibrec(4))
print(fibmem(4))