# Linear Regression의 Cost 최소화 알고리즘의 원리

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Simplified Hypothesis

- H(x) = Wx
- Cost(W)

## What cost(W) looks like?

- 최소한의 W값을 찾자. minimize
- W = 1, cost(W) = 0

  - (1+1-1)^2 + (1*2-2) + (1*3-3) = 0

- W = 0, cost(W) = 4.67

  - 1/3((0*1-1)^2 + (0*2-2)^2 + (0\*3-3)^2) = 4.67

- W = 2, cost(W) = 4.67

- ![image](https://user-images.githubusercontent.com/60251579/94142973-0df0c600-feaa-11ea-84f3-5c41be3b6489.png)

  | **x** | **y** |
  | ----- | ----- |
  | 1     | 1     |
  | 2     | 2     |
  | 3     | 3     |

## Gradient descent algorithm - 경사에 따라 내려가는 알고리즘

- Minimize cost function
- Gradient descent is used many minimization problems
- For a given cost function, cost(W, b), it will find W, b to minimize cost
- It can be applied to more general function: cost(w1, w2, ...)

## How it works?

- Start with inital guesses

  - Start any other value or 0,0
  - Keeping changing `W` and `b` a little bit to try and reduce cost(W,b)

- Each time you change the parameters, you select the gradient which reduces cost(W,b) the most possible.
- Repeat
- Do so until you converge to a local minimum
- Has an interesting property
  - Where you start can determine which minimum you end up

## Formal definition

- [미분 계산 WEB](https://www.derivative-calculator.net/)

## Gradient descent algorithm

-![image](https://user-images.githubusercontent.com/60251579/94146019-51e5ca00-feae-11ea-8ce8-5ebeeddaf8ad.png)

## Convex function

- cost(W, b)를 거꾸로 뒤집어 놓은 경우
- 시작점마다 결과를 확정 할 수 없는 것을 확정 시킴.
- Gradient 알고리즘이 무조건 답을 찾을 수 있도록 확인.

## Gradient Descent Tensorflow 구현

![image](https://user-images.githubusercontent.com/60251579/94149856-611b4680-feb3-11ea-9780-f09ba4ccad54.png)

```python
# Minimize : Gradient Descent using derivative
# W -= Learning_rate(alpha)* derivative
learning_rate = 0.1 # 학습률 설정
gradient = tf.reduce_mean((W*X-Y) * X) # 계산 수식
descent = W - learning_rate * gradient # W - gradient 값 계산.
update = W.assign(descent) # 게산값 assign 해줘서 넘김
```

## Optimizer을 통해 GradientDescent 원하는 대로 수정 가능.

- 위 식과 같음.
- `optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)`
