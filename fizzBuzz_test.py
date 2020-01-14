import unittest

from fizzBuzz import canBedivide, fizzBuzz

class fizzBuzz_test(unittest.TestCase):

  def test_canBedivideCase1(self):
    self.assertTrue(canBedivide(15, 3, 5))

  def test_canBedivideCase2(self):
    self.assertFalse(canBedivide(7, 3))

  def test_fizzBuzzCase1(self):
    self.assertEqual(fizzBuzz(5),[1, 2, "Fizz", 4, "Buzz"])

  
if __name__ == "__main__":
  unittest.main()