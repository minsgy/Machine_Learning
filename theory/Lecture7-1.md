# Learning rate, Evaluation

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Training and Test datasets

- Training 값과, Test Datasets을 **반드시** 구분해야 한다.
- ![image](https://user-images.githubusercontent.com/60251579/95017361-d812c500-0693-11eb-8c11-c5461d0efa3a.png)
  - Traning Data : X_data, Y_data
  - Test Data : x_test, y_test

```python
    # Training Data
    x_data = [[1,2,1],[1,3,2],[1,3,4]]
    y_data = [[0,0,1],[0,0,1],[0,0,1]]

    # Evaluation our model using Test Dataset
    x_test = [[2,1,1],[3,1,2],[3,3,4]]
    y_test = [[0,0,1],[0,0,1],[0,0,1]]
```
