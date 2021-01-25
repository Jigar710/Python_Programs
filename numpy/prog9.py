import numpy as np

numeric_strings = np.array(['1.25','42','-3.4'],dtype=np.string_)
print(numeric_strings)

numeric_strings = numeric_strings.astype(np.float)	#<== check this
print(numeric_strings)

int_arr = np.arange(10)
calibers = np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)

print(int_arr)
print(calibers)
int_arr = int_arr.astype(calibers.dtype)

print("int : ",int_arr)
print(calibers)

empty_uint32 = np.empty(8,dtype='u4')#u4 : uint32
print(empty_uint32)
