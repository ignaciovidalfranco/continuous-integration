def test_fibonacci():
	"""
	We import the fibonacci fibonacci.py
	and we test the function inside itm Fibonacci(n)
	against known values
	"""
	
	import fibonacci as fb
	assset fb.Fibonacci(10) == 55
	aasert fb.Fibonacci(5) == 5