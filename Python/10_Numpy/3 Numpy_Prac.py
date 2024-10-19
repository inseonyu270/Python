# numpy를 import시켜주세요
import numpy as np

# 1. 0부터 9까지의 정수로 이루어진 크기가 10인 1차원 배열을 생성하시오
# np.array 금지

array1 = np.arange(10)
print(array1)

# 2. 뽑은 1차원 배열의 순서를 반대로 바꿔보세요.
array2 = array1[::-1]
print(array2)

# 3. 주어진 두 배열의 합,차,곱,나눗셈을 계산해 보시요
# 첫 번째 배열 : [1,2,3,4,5]
# 두 번째 배열 : [6,7,8,9,10]

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)


# 4.1. 주어진 1차원 배열의 모든 요소의 합을 계산하시오
# 배열 : [1,2,3,4,5]

ar1 = np.array([1, 2, 3, 4, 5])
print(ar1.sum())

# 4.2 : 주어진...평균을 계산하시오
# 배열 : [10,20,30,40,50]
ar2 = np.array([10, 20, 30, 40, 50])
print(ar2.mean())

# 4.3 : 주어진 배열에서 최댓값과 최솟값을 찾아보시오.
# 배열 : [17,12,25,9,30]
ar3 = np.array([17, 12, 25, 9, 30])
print(ar3.max())
print(ar3.min())