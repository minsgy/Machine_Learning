# numpy 사용해보기

+ ⚙[NIPA 인공지능/데이터분석 믹스앤매치 아카데미](https://nipa.elice.io/explore)

## numpy library function
- np.array : 배열 생성
- np.zeros : 0이 들어 있는 배열 생성
- np.ones : 1이 들어 있는 배열 생성
- np.empty : 초기화가 없는 값으로 배열을 반환
- np.arange(n) : 배열 버전의 range 함수
- np.random.randint : 다양한 난수가 들어있는 배열 생성

```python

array = np.random.radint(0, 5(3,5))
# 0~5 사이 랜덤 값이 들어간 3x5 array 생성

```

## array informations

- type(array) : array의 자료형(요소X)
- array.ndim : 차원 값 (1차원 배열, 2차원 배열 등)
- array.shape : array 모양
- array.size : array 크기
- array.dtype : array안의 요소 자료형(int64 등)
- array\[5] : array index 5인 요소
- array\[3:6] : array index 3~5인 요소

## 이어 붙이고 나누기
- reshape() 
    -  배열의 속성 중, shape 를 변경할 수 있게 하는 함수.
    - 1차원 배열을 2차원 배열로 바꾸거나, 2차원 행/열 조절가능
    - `matrix = array.reshape((2,4)) # array 2*4 크기` 
- concatenate()
    - array를 붙히는 기능, 이를 이용해 투 배열을 하나로 합칠 수 있음
    - 열의 개수가 같은 array 끼리 세로(axis=0)
    - 행의 개수가 같은 array 끼리 가로(axis=1)로 붙힐 수 있습니다.
    -`m = np.concatenate([matrix, matrix], axis=0)` 

- split()
    - array를 나누는 기능
    - concatenate() 함수와 달리, split() 함수는 하나의 배열과 방향을 지정하여 두 개의 배열로 나눕니다.
    -`c, d = np.split(matrix, [1], axis=1)`
        - 열을 기준으로, index 1을 기준하여 나누어 각 각 c, d 변수에 저장.


## 기본 연산

```python
array = np.array([1,2,3,4,5])

array + 5 # 6,7,8,9,10
array - 5 # -4, -3, -2, -1, 0
array * 5 # 5, 10, 15, 20, 25
array / 5 # 1/5, 2/5, 3/5, 4/5, 1
array + array2 
array - array2
```

## broadcasting
```python
# A = [[0]
#     [1]
#     [2]
#     [3]
#     [4]
#     [5]]

# B = [0 1 2 3 4 5]

A = np.arange(6).reshape(6, 1)
B = np.arange(6)
A+B 
# [[ 0  1  2  3  4  5]
#  [ 1  2  3  4  5  6]
#  [ 2  3  4  5  6  7]
#  [ 3  4  5  6  7  8]
#  [ 4  5  6  7  8  9]
#  [ 5  6  7  8  9 10]]
```

## 집계함수 및 마스킹 연산

```python
np.sum(matrix) # matrix 총합
np.max(matrix) # matrix 중 최대값
np.min(matrix) # matrix 중 최소값
np.mean(matrix) # matrix 의 평균 값
np.sum(matrix, axis=0) # 각 열의 값
np.sum(matrix, axis=1) # 각 행의 값
np.std(matrix) # 표준 편차

'''마스킹 연산'''
matrix[matrix<5] # matrix 중 5보다 작은 수
```

## 정리

### 배열의 황제! Numpy
- 고성능의 수치 계산을 위해 만들어진 라이브러리

**Numpy**

- Numpy가 널리쓰이고 강력하다는 말을 듣게 해주는 것은 바로 n darry의 힘이라고 봐도 과언이 아닙니다.

- numpy 라이브러리는 효율적인 데이터분석이 가능하도록 N차원의 배열 객체를 지원합니다.

- numpy library에서 자주 사용되는 함수들로는

    - np.array - 배열생성
    - np.zeros - 0이 들어있는 배열 생성
    - np.ones - 1이 들어있는 배열 생성
    - np.empty - 초기화가 없는 값으로 배열을 반환
    - np.arrange(n) - 배열 버전의 range 함수