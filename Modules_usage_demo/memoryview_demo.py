from array import array

numbers = array('h', [-2,-1,0,1,2])

memv = memoryview(numbers)

len(memv)

memv_oct = memv.cast("B")
memv_oct.tolist()
memv_oct[5] = 4
numbers
