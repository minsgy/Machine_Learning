# Linear Regression의 Hypothesis와 Cost

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Perdicting exam score - regression

**Training Data**

| **x**(hours) | **y**(scores) |
| ------------ | ------------- |
| 10           | 90            |
| 9            | 80            |
| 3            | 50            |
| 2            | 30            |

- Training Data를 토대로 예측 해주는 Model
- 0~100의 사이값을 예측
- 10시간을 공부해서 90점, 9시간을 공부해서 80점.

## Linear (Hypothesis)

- 어떠한 데이터가 있다면, 일정한 선을 그어주는 것.
- H(x) = Wx + b, 1차 방정식 가설
- 데이터들을 넣어서 예상 값을 생각함.

### which hypothesis is better?

- 가장 좋은 경우의 수? 실제 데이터를 기준 삼아, 어떠한 데이터들이 기준과 가장 가까운지 Check.

### Cost Function (Loss Function)

- How fit the line to our(training) data.
- `H(x) - y` -> `(H(x)-y)^2`
- 음수 값을 양수로 바꿔주며, 차이 값이 클 경우 패널티가 더욱 크게 하는 방법.

### Goal : Minimize Cost

- minimize cost(W,b)
- W,b가 최소하는 값을 찾는 것이, Linear의 목표
