from statistics import median
from array import array
from collections import Counter
import random
from . import _utils

options_max_values = 20

class Array:
    '''
    This is a single-dimensional numeric
    array for scientific computing.

    This array will compute lots of
    basic statistics.

    Attributes
    ----------
    data: list
        List of numbers

    Methods
    -------
    TODO
    '''


    def __init__(self, data):
        # Allow user to pass only an array or a list
        if isinstance(data, array):
            # TODO - check for cases where typecode is not 'b', 'q', or 'd'
            self.data = data
        elif isinstance(data, list):
            dtype = _utils.get_dtype_of_list(data)

            # if there is mixed data types in the list
            # such that the first element is integer and the next float                
            try:
                self.data = array(dtype, data)
            except TypeError:
                self.data = array('d', data)
        else:
            raise TypeError('Array constructor only accepts lists or arrays')
        # b - boolean (1 byte integer)
        # q - interger (8 bytes)
        # d - float (8 bytes)
        self.dtype = self.data.typecode

    def sum(self):
        '''
        Sums all the values in the array

        Returns
        -------
        int or float
        '''
        return sum(self.data)

    def max(self):
        '''
        Finds max of all values in the array

        Returns
        -------
        int or float
        '''
        return max(self.data)

    def min(self):
        '''
        Finds min of all values in the array

        Returns
        -------
        int or float
        '''
        return min(self.data)

    def mean(self):
        '''
        Finds mean of all values in the array

        Returns
        -------
        int or float
        '''
        return self.sum() / len(self)

    def median(self):
        '''
        Finds median of all values in the array

        Returns
        -------
        int or float
        '''
        return median(self.data)

    def __repr__(self):
        final_str = ''
        # TODO: validate against even/odd number
        # TODO: CHeck if you array is a float. Limit decimals with an option
        # TODO: If dtype is 'b' then output True or False for each value
        half_max = options_max_values // 2
        if len(self) < options_max_values:
            for val in self.data:
                final_str += f'{val:5}\n'
        else:
            for val in self.data[:half_max]:
                final_str += f'{val:5}\n'
            final_str += '...\n'
            for val in self.data[-half_max:]:
                final_str += f'{val:5}\n'
        return final_str

    def __len__(self):
        return len(self.data)
    
    def sort(self, reverse=False):
        data = sorted(self, reverse=reverse)
        return Array(data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, slice):
            return Array(self.data[key])
        elif isinstance(key, list):
            # TODO: getitem with a list
            raise NotImplementedError('Not done yet. Will do soon!!')
        else:
            raise TypeError('key must be an int, slice, or a list')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            # TODO: Change data type of array if given float
            self.data[key] = value
        # TODO: Can you set items with a slice or list

    def __add__(self, other):
        # return an array that has `value` added to each element
        if isinstance(other, (bool, int, float)):
            data = [val + other for val in self]
        elif isinstance(other, Array):
            if len(self) != len(other):
                raise ValueError(f'Arrays must be same length {len(self)} != {len(other)}')
            data = [val1 + val2 for val1, val2 in zip(self, other)]
        else:
            raise TypeError('other must be a bool, int, float, or an Array')
        return Array(data)

    def __sub__(self, value):
        # return an array that has `value` added to each element
        data = [val - value for val in self]
        return Array(data)

    def __mul__(self, value):
        # return an array that has `value` added to each element
        data = [val * value for val in self]
        return Array(data)

    def __truediv__(self, value):
        # return an array that has `value` added to each element
        data = [val / value for val in self]
        return Array(data)

    def __floordiv__(self, value):
        # return an array that has `value` added to each element
        data = [val // value for val in self]
        return Array(data)

    def __pow__(self, value):
        # return an array that has `value` added to each element
        data = [val ** value for val in self]
        return Array(data)

    def __mod__(self, value):
        # return an array that has `value` added to each element
        data = [val % value for val in self]
        return Array(data)

    # TODO: implement the right-side operators like __radd__
    # TODO: implement array to array arithmetic operations just like we did in __add__

    # Implement >

    def __gt__(self, other):
        # return an array that has `value` added to each element
        if isinstance(other, (bool, int, float)):
            data = [val > other for val in self]
        elif isinstance(other, Array):
            if len(self) != len(other):
                raise ValueError(f'Arrays must be same length {len(self)} != {len(other)}')
            data = [val1 > val2 for val1, val2 in zip(self, other)]
        else:
            raise TypeError('other must be a bool, int, float, or an Array')
        return Array(data)

    # TODO: Implement the rest of the comparison operators

    # Use collection module to find mode

    ## Class method to create a random array

    def mode(self):
        c = Counter(self)
        return c.most_common(1)

    # TODO: What happens if there are ties
    # TODO: Create parameters for users to control output

    # MAKE ALTERNATE CONSTRUCTOR

    # arr = Array([1, 5, 6])

    # arr1 = Array.create_random(low, high, n) 
    # This would produce a random array of numbers between low and high
    # This is a class method

    @classmethod
    def create_random(cls, low, high, n):
        data = [random.randint(low, high) for i in range(n)]
        return cls(data)
        # does the same thing `Array(data)`

    @classmethod
    def create_from_dict(cls, d):
        if not isinstance(d, dict):
            raise TypeError('d must be a dictionary')
        data = list(d.keys())
        return cls(data)