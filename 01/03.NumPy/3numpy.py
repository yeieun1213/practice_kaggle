import numpy as np

#arange(): range()
sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

#zero(): 함수 인자로 튜플 형태의 shape값을 입력하면 모든 값을 0으로 채운 npdarray
#ones(): 모든 값을 1로
zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_array = np.ones((3, 2))
print(one_array)
print(one_array.dtype, one_array.shape)

