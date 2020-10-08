# Logisitic Classification의 가설 함수 정의

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Regression(HCG)

- H : Hypothesis - H(X) = WX
- C : Cost - cost(W), 최소화하는 W 값을 찾아야함.
- G : Gradient decent - 그래프 경사(기울기)를 이용해서 정확도 올리기.
- 위 세 가지를 가지고 Regreesion 구현가능함.

## Classification (Binary Choice)

- Example
  - Spam Detection : Spam or Ham (Email)
  - Facebook feed : Show or Hide
  - Credit Card Fraudulent Transaction detection: legitimate/fraud
  - Finance : AI

## 0, 1 Encoding

- Spam Dectection: spam(1) or Ham(0)
- Facebook feed: show(1) or hide(0)
- Credit Card Fraudulent Transaction detection: legitimate(0) or fraud(1)

## Logistic Hypothesis

- H(x) = WX+b : 0, 1 단위로 다루기 애매해서 찾은 함수
- 이를 Logistic Hypothesis를 함수화 하게됨.
