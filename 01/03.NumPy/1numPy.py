import numpy as np

#넘파이 기반 데이터 타입은 ndarray
#array() : ndarray로 변환하는 기능
#shape: : ndarray의 크기(행과 열의 수를 투플 형태로)

array1 = np.array([1, 2, 3])
print('array1 type:', type(array1))
print('array1 array 형태:', array1.shape)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1, 2, 3]])
print('array3 type:', type(array3))
print('array3 type 형태:', array3.shape)

#ndim: 차원
print('array1: {:0}차원, array: {:1}차원, array3: {:2}차원'.format(array1.ndim, array2.ndim, array3.ndim))
print("array1: {}, array2: {}, array3: {}".format(array1.ndim, array2.ndim, array3.ndim))
