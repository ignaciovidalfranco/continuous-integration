def Fibonacci(n):
	if n < 0:
			raise ValueError("n < 0 is not valid")
	elif round(n) != n:
			raise ValueError("n is not an integer number!")
	if n < 2:
		return n
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
	
