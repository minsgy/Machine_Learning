# Softmax classification: Multinomial classification

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Logistic regression

- H(x) = Wx : return 값이 실수의 형태가 되기 때문에, binary, logistic 등에 적합 하지 않은 알고리즘
- x -> w -> z (sigmoid) -> Y_HAT(0, 1 binary type) == H(x)

## Multinomial classification

- 다양한 데이터 타입이 존재하는 상황(경우가 0, 1, 2, 3, ...)
- 만약에 A,B,C 3개를 구분하게 한다면?
- [w1, w2, w3]\* [ [ x1 ], [ x2 ],[ x3 ] ] = [w1x1 + w2x2 + w3x3] 을 3번 반복 하게 됨.
- 그래서 w 행렬을 모아서 x값을 곱함. 나온 결과의 한 행의 값들이 h(a),h(b),h(c)를 나타나게됨.
  ![image](https://user-images.githubusercontent.com/60251579/94991430-15a51e80-05be-11eb-95df-cb6e364c91c9.png)

## Where is Sigmoid?

- ![image](https://user-images.githubusercontent.com/60251579/94991490-76ccf200-05be-11eb-9739-a7eb318c2301.png)

## SOFTMAX

- ![image](https://user-images.githubusercontent.com/60251579/94991752-01fab780-05c0-11eb-9730-750a71f52f5f.png)

## Sigmoid

- ![image](https://user-images.githubusercontent.com/60251579/94991755-0921c580-05c0-11eb-9a31-44d4fc302741.png)
- A가 나올 확률이 0.7
- B가 나올 확률이 0.2
- c가 나올 확률이 0.1

### 'One-hot encoding'

- 나온 확률 중 가장 높은 1개 값 빼고 다 0으로 초기화.

## Cost Function

- Cross-entropy

  - ![image](https://user-images.githubusercontent.com/60251579/94991805-6158c780-05c0-11eb-8571-c622a18becd5.png)
    - S(Y) = Y hat, L = 실제 값
    - D(S, L)

- Cross-entropy cost function
  - Y = L = [0, 1] = B 예측
    - Y hat = [0(A), 1(B)] = B (ok) 예측 성공, Data = 0 을 반환.
    - Y hat = [1(A), 0(B)] = A (NOOOO) 예측 실패, Data = 무한대 반환. 매우 큰 값
    - Cost 함수의 사용 이유대로 데이터 값이 나옴.

## Logisitic cost VS cross entropy

- C(H(x) y) = ylog(H(x)) - (1 - y)log(1 - H(x))
- D(S, L) = -∑ L\*Log(S)
- C와 D는 같다.

## Result COST Function

- ![image](https://user-images.githubusercontent.com/60251579/94992028-0c1db580-05c2-11eb-870b-b038ef99af15.png)

- 최소화 방법으로, Gradient Descent 방식을 사용합니다.
