# arraymin

in this python package, the arramin module can find the minimum of array with minimum number of comparisons.

input array: the first elements of array should strictly monotonically decrease and 
the rest of elements should strictly monotonically increase.

if the input is not based on the above, the check_input method inside of ArrayMin class will return Exception Error.

There is different unit test cases which is inside of directorsy arraymin/tests/, which can be observered by running python tests/test_array_min.py

the class ArrayMin has two methods:

check_input(): which this method checks for the input if it is based on the pattern of trend introduced.

get_min(low, high, array): find the minimum of array based on the minimum number of comparisons.

# installation:
after cloning the repository, 
run the following:

pip install dist/arraymin-1.0.0-py3-none-any.whl 

# check the input:

from arramin import arraymin

#define the array:

array = [1,0, 4,5,6,7]

arr = array(array)

arr.check_input()

if it is successful, then we can find the minimum based on the following:

minimum = arr.get_min(0, len(array) - 1, array)


