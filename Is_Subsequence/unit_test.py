import unittest

def isSubsequence(s,t):
	pass


class Test(unittest.TestCase):
	test_cases = [
		('abc', 'ahbgdc'), 
		('axc', 'ahbgdc'),
		('abc', 'ah'*100+'bgd'*100+'c'),
		('axc', 'ahbgd'*1000+'c'),
		('abc', ''),
		('', 'ahbgdc'),
		('abc'*100, 'ahbgdc'),
		('abc'*100, 'ahbgdc'*1000)
		]
	test_label = [True, False, True, False, False, True, False, True]

	def test_solution(self):
		for test_case, test_label in zip(self.test_cases, self.test_label):
			actual = isSubsequence(*test_case)
			if test_label: 
				self.assertTrue(actual)
			else:
				self.assertFalse(actual)

if __name__ == "__main__":
	unittest.main()