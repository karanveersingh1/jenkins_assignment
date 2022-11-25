import unittest
from prog import angle_inside
class TestSum(unittest.TestCase):
 def test_1(self):
  a_1 = 10
  b_1 = 90
  c_1 = 45
  result = angle_inside(a_1, b_1,c_1)
  self.assertEqual(result, True)

 def test_2(self):
  a_2 = 100
  b_2 = 360
  c_2 = 180
  result = angle_inside(a_2, b_2,c_2)
  self.assertEqual(result, True)

 def test_3(self):
  a_3 = 350
  b_3 = 5
  c_3 = 0
  result = angle_inside(a_3, b_3,c_3)
  self.assertEqual(result, True)

 def test_4(self):
  a_4 = 5
  b_4 = 360
  c_4 = 0
  result = angle_inside(a_4, b_4,c_4)
  self.assertEqual(result, True) 

 def test_5(self):
  a_5 = 11
  b_5 = 234
  c_5 = 180
  result = angle_inside(a_5, b_5,c_5)
  self.assertEqual(result, True)

if __name__ == '__main__':
	unittest.main()
