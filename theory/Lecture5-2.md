# Logistic classification : Cost function & Gradient decent

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Cost Function

- H(x) = Wx + b 의 경우, 최소 값을 찾아야함.

- 선형 회귀
  - H(x) = 1 -> cost = O
  - H(x) = 0 -> cost = 무한
  - H(x) = 0, cost = 0
  - h(x) = 1, cost = 무한

## Cost Function

- C(H(x), y) = - ylog(H(x)) - (1 - y)log(1 - H(x))
  - y = 1, c = -log(1+h(x))
  - y = 0, c = -log(1-h(x))

## Minimize cost - Gradient decent Algorithm

- 기울기를 구한다. (미분)
- W (GradientDescentOptimizer) 라이브러리 존재.

```python
# cost function
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis)))
```

```python
# Minimize
a = tf.Variable(0.1) # Learning rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

```

## Exercise

- CSV reading using tf.decode_csv
- Try other classification data from [Kaggle](https://www.kaggle.com/)
