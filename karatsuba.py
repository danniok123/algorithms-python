# Karatsuba String Multiplication
# Wanted to implement this algorithm but with strings instead

import unittest
from random import randint

def add(s1, s2):
	return str(int(s1) + int(s2))

def sub(s1, s2):
	return str(int(s1) - int(s2))

def karatsuba(s1, s2):
	if int(s1) < 10 or int(s2) < 10:
		return str(int(s1) * int(s2))

	m = max(len(s1), len(s2))

	# Need to add padding to the front
	# of the number that is smaller
	s1 = (m - len(s1))*'0' + s1
	s2 = (m - len(s2))*'0' + s2

	high1, low1 = s1[:m//2], s1[m//2:]
	high2, low2 = s2[:m//2], s2[m//2:]

	z0 = karatsuba(low1, low2) 
	z1 = karatsuba(add(high1, low1), add(high2, low2))
	z2 = karatsuba(high1, high2)

	tmp1 = z2 + (2 * len(low1))*'0' # (z2*10^(2*m2))
	tmp2 = sub(z1, add(z0, z2)) + len(low1)*'0' # ((z1-z2-z0)*10^(m2))
	tmp3 = add(tmp1, tmp2) 
	ans = add(tmp3, z0)

	return ans

class TestKaratsuba(unittest.TestCase):
	def test_random(self):
		for i in range(100):
			x = str(randint(1, 10000))
			y = str(randint(1, 10000))

			want = str(int(x) * int(y))

			self.assertEqual(karatsuba(x, y), want)

if __name__ == '__main__':
	unittest.main()