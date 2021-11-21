"""
Test Scenarios for ArrayMin class and get_min function
"""
import unittest
import sys
import os

# setting path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

#importing our main package

from arraymin import ArrayMin

class TestarrayMin(unittest.TestCase):
    """
    Test Class for ArrayMin class and get_min function
    """

    def test_arr_min1(self):
        """
        Test if it can return the minumum,
        Senario: the first is not monotically deceasing, and the rest is increasing
        """
        array = [8,5,4,3,1,20,30,40,45,70]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, 1, "should be 1")

    def test_arr_min2(self):
        """
        Test if it can return the minumum,
        Senario: the first is monotically deceasing, and the rest is increasing
        """
        array = [8,5,4,-3,-4,2,3,4,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, -4, "should be -4")

    def test_arr_min_non_monotonic1(self):
        """
        Test if it can return the minumum,
        Senario: the first is not monotically deceasing, and the rest is increasing
        it should assert error
        """
        array = [8,0,4,-3,-4,2,3,4,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, -4, "should be -4")

    def test_arr_min4(self):
        """
        Test if it can return the minumum,
        Senario: the first is  monotically deceasing, and the rest is increasing
        """
        array = [1,2,3,4,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, 1, "should be 1")

    def test_arr_min5(self):
        """
        Test if it can return the minumum,
        Senario: the first is monotically deceasing, and the rest is increasing
        """
        array = [3,1,2,3,4,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, 1, "should be 1")

    def test_arr_min_non_monotonic2(self):
        """
        Test if it can return the minumum,
        Senario: the first is not monotically deceasing, and the
        function shpuld assert error
        """
        array = [3,0,1,-2,4,5,7,2,20,1, 0, 14, -5]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, -5, "should be -5")

    def test_arr_min_with_equal(self):
        """
        Test if it can return the minumum,
        Senario: there is two 3's in the second tail,
        it should assert error
        """
        array = [3,1,0,3,3,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, 0, "should be 0")

    def test_arr_min_with_equal_in_middle(self):
        """
        Test if it can return the minumum,
        Senario: there is two 1's in the middle,
        the first few elements is monotonically decreasing,
        and the rest is increasing
        """
        array = [3,1,1,3,4,5,7]
        arraymin = ArrayMin(array)
        if arraymin.check_input():
            min_ = arraymin.get_min(0, len(array) -1 , array)
            self.assertEqual(min_, 1, "should be 1")

if __name__ == '__main__':
    unittest.main()
