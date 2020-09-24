# Multi-variable linear regression(New.Ver)

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Recap

- Hypothesis
  - H(x) = Wx + b (W,b 학습)
- Cost Function
  - cost(W,b)
  - 밥 그릇모양됨
- Gradient descent algorithm

## Matrix Multiplication

- "Dot Product"
- 행렬의 곱

## Hypothesis using matrix

| x1  | x2  | x3  | Y   |
| --- | --- | --- | --- |
| 73  | 80  | 75  | 152 |
| 93  | 88  | 93  | 185 |
| 89  | 91  | 90  | 180 |
| 96  | 98  | 100 | 196 |
| 73  | 66  | 70  | 142 |

- H(x1,x2,x3) = x1w1 + x2w2 + x3w3
- H(X) = XW

## Hypothesis using matrix exam

- (5, 3) \* (3, 1) = (5, 1)
- Plus
  - X \* W = H(x)
  - (5, 3) \* (W) = (5, 1)
  - W matrix ? (3, 1)

## Hypothesis using matrix (n output)

- (n, 3) \* (?, ?) = (n, 2)
- (n, 3) \* (3, 2) = (n, 2)

## Lecture(theory):

- H(x) = Wx + b

## Implementation(TensorFlow):

- H(x) = XW
- Matrix의 경우 순서가 바뀌면 안됨.
- 수학 적인 의미로는 같음
