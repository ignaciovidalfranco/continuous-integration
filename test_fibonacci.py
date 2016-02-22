import unittest

class FibTest(unittest.TestCase):
	

	def test_fibonacci(self):
		"""
		We import the fibonacci fibonacci.py
		and we test the function inside itm Fibonacci(n)
		against known values
		"""
		
		import fibonacci as fb;
		
		assert fb.Fibonacci(10) == 55
		assert fb.Fibonacci(5) == 5
	
	def test_Fib_throws_exception(self):
		import fibonacci as fb
		self.assertRaises(ValueError, fb.Fibonacci, -5)
		self.assertRaises(ValueError, fb.Fibonacci, 1.2)
