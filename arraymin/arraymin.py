"""
two classes:
the first one is assertion error class

the second is ArrayMin, with the following methods:
get_min and check_input

"""

class ArrayTrendError(Exception):
    """
    Exception raised when the input array is not based on the pattern,
    pattern: The first few elements should strictly monotonically decrease
    and the rest strictly monotonically

    Attributes:
    message -- explanation of error
    """

    def __init__(self, array , message = "The first few elements should strictly monotonically decrease and the rest strictly monotonically"):
        self.message = message
        self.array = array
        super().__init__(self.message)

    def __str__(self):
        return f'{self.array} -> {self.message}'


class ArrayMin:
    """
    we assume that the input array has the first few elements are monotonically decreasing,
    and the rest is monotonically increasing
    returns the minimum of array with minimum number of comparisons

    Attrbutes
    array
    """

    def __init__(self, arr):
        self.arr = arr
        self.comp_num = 0

    def check_input(self):
        """
        check the input if it is based on the mentioned pattern:
        the first few elements are strictly monotonically decreasing,
        and the rest is strictly moonotonically increasing

        returns the True if the pattern of input is correct
        and asserts error if it is not
        """

        length = len(self.arr)
        trend = 'decr'
        for i in range(length - 1):
            if self.arr[i] == self.arr[i + 1]:
                if not (self.arr[i - 1] and self.arr[i + 2] and
                self.arr[i - 1] > self.arr[i] and self.arr[i + 1] < self.arr[i + 2]):
                    raise ArrayTrendError(self.arr)
            if self.arr[i] < self.arr[i + 1]:
                trend = 'incr'
            elif trend == 'incr':
                raise ArrayTrendError(self.arr)
        return True


    def get_min(self, low, high, arr):
        """
        get the minimum of an array with minimum number of comparisons
        Attributes:
        low -- low index of array
        high -- high index of array
        arr -- array
        """

        if low == high:
            return self.arr[low]
        elif self.arr[low] < self.arr[low + 1]:
            self.comp_num += 1
            return self.arr[low]
        elif low + 1 == high:
            self.comp_num += 1
            return self.arr[high]
        else:
            mid = int((low + high) / 2)
            arg_min1 = self.get_min(low, mid, arr)
            arg_min2 = self.get_min(mid + 1, high, self.arr)
        self.comp_num += 1

        return min(arg_min1, arg_min2)
