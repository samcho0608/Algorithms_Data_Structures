# This problem was asked by Facebook.

# You have a large array with most of the elements as zero.

# Use a more space-efficient data structure, SparseArray, that implements the same interface:

# init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.

class SparseArray :

    def __init__(self, arr, size):
        self.size = size
        self._data = {
            i : v
            for i, v in enumerate(arr)
            if v > 0
        }

    def _validateInBound(self, i) :
        if i >= self.size or i < 0:
            raise Exception('out of bound')

    def set(self, i, val) :
        self._validateInBound(i)
        self._data[i] = val

    def get(self, i) :
        self._validateInBound(i)
        return self._data.get(i, 0)

## solution
# class SparseArray:
#     def __init__(self, arr, size):
#         self.size = size
#         self.map = {}

#         orig_arr_size = len(arr)
#         for i, e in enumerate(arr):
#             if i >= orig_arr_size:
#                 break
#             if e != 0:
#                 map[i] = e

#     def check_bounds(self, i):
#         if i < 0 or i >= self.size:
#             raise IndexError()
    
#     def set(self, i, v):
#         self.check_bounds(i)
#         self.map[i] = v

#     def get(self, i):
#         self.check_bounds(i)
#         v = self.map.get(i)
#         if v is None:
#             return 0
#         return v

longArray = [0,0,0,0,0,1,0]
sparseArray = SparseArray(longArray, len(longArray))

assert sparseArray.size == len(longArray)
assert sparseArray.get(5) == 1
sparseArray.set(0, 1)
assert sparseArray.get(0) == 1
