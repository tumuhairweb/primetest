import unittest
import prime_numbers

class Test_Prime(unittest.TestCase):
	def setUp(self):
		# self.primenum = PrimeNum();
		self.result1 = prime_numbers.generate_prime_num(1)
		self.result2 = prime_numbers.generate_prime_num(5)
		self.result3 = prime_numbers.generate_prime_num(10)

	#check if it raises TypeError when input is not an ineteger
	def test_if_raises_TypeError_when_non_int_passed_parameters(self):
		self.assertRaises(TypeError, prime_numbers.generate_prime_num, "Three")
		self.assertRaises(TypeError, prime_numbers.generate_prime_num, 3.6)
	
	def test_if_raise_ValeError_when_negative_parameter_is_passed(self):
		self.assertRaises(ValueError,prime_numbers.generate_prime_num, -7)

	# #Testing to see if it returns 1 0r 0 as a prime number
	def test_output_result1(self):
		self.assertEqual(self.result1, [0,1], msg="Invalid output")

	# 	#testing to see if it returns an even number as part of the prime numbers
	def test_output_result2(self):
		self.assertEqual(self.result2, [2,3,4,5], msg="Invalid output")

	# #testing to see if it returns 9 as a prime number
	def test_output_result3(self):
		self.assertEqual(self.result3, [2,3,5,7,9], msg="Invalid output")
