# Learning rate, Data preprocessing, Overfitting

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Learning rate의 중요성

- Step의 간격이 적절하지 않으면, 학습이 제대로 되지 않음.
- 매우 큰 값으로 설정 시, learning rate 숫자가 아닌 매우 큰 값 등 출력할 수 있게됌.
- 매우 작은 값으로 설정 시, 학습 시간이 매우 오래 걸림.
- 이와 같은 경우를 **OverShooting** 이라고 말함.

## Try several learning rates

- Observe the cost function
- Check it goes down in a reasonable rate
- 0.01 부터 시작하여, 함수의 값을 환산하는 것이 좋음.

## Data (X) Preprocessing for Gradient descent

- Normalize data : cost 함수가 발산 한다던가, 데이터 차이가 큰 경우 사용하기 좋음.
- zero-centered data : 위와 같은 이유

## Standardization (Normalize data 중 하나)

- `X_std[:,0] = (X[:,0] - X[:, 0].mean()) / X[:,0].std()`

## Overfitting 이란?

- Our model is very good with training data set(with memorization)
- Not good at test dataset or in real use
- 우리가 테스트 한 학습 데이터들이 구현한 함수에 너무 알맞게 설정되어서 실제 데이터값을 대입 시, 일치 확률이 떨어지는 경우 입니다.

## Solutions for overfitting

- More Training data! => 많은 데이터들을 이용해 경우의 수를 다양하게 파악해야합니다.
- Reduce the number of features => 중복 된 값들을 줄입니다.
- **Regularization** (일반화)

## Regularization

- Let's not have too big numbers in the weight
- weight 값이 적은 값, cost 값을 최소화
- ![image](https://user-images.githubusercontent.com/60251579/95007728-de7e4e00-064d-11eb-9690-29e8908ca742.png)
  - regularization strength
  - `l2reg = 0.001 * tf.reduce_sum(tf.square(W))`
  - Square는 제곱수, 0.001로 최소화 시킨다.

## Summary

1. **Learning rate**
2. **Data preprocessing**
3. **Overfitting** 아주 중요!!
   - More training data
   - Regularization
