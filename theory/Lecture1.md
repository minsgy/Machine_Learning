# TensorFlow의 설치 및 기본적인 Operations

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Tensorflow

- Google Create.
- An open-source software library for Machine Interlligence.
- Deep learning libraries Accumulated GitHub Metrics 1st.
- Python

## What is a Data flow graph?

- Nodes in the graph represent mathematical operations
- Edges represent the multidimensional data arrays(tensors) communicated between them.
- Made by Tensorflow

## Windows Install

- `pip install --upgrade tensorflow`
- `pip install --upgrade tensorflow-gpu`
- ![image](https://user-images.githubusercontent.com/60251579/93843820-29a37300-fcd6-11ea-9092-3548cb028ba8.png)

## TensorFlow Mechaincs

1. Build graph using Tensorflow operations (graph build)
2. Feed data and run graph operations (`sess.run(op, feed_dict{x:x_data}`), graph run)
3. update variables in the graph (and return values)

## Tensor Ranks, Shapes and Types

| **Rank** | **Math entity**                      | **Python 예시**                       |
| -------- | ------------------------------------ | ------------------------------------- |
| 0        | **Scalar** (magnitude only)          | `s = 483`                             |
| 1        | **Vector** (magnitude and direction) | `v = [1.1, 2.2, 3.3]`                 |
| 2        | **Matrix** (table of numbers)        | `m = [[1,2,3],[4,5,6],[7,8,9]]`       |
| 3        | **3-Tensor** (cube of numbers)       | `t = [[[2],[4],[6]], [[8],[10],[12]]` |
| 4        | **n-Tensor** (you get the idea)      | `...`                                 |

## SHAPE

- 1차원, 2차원, n차원 등 tensor 구성에서 아주 중요한 부분
- `t = [[1,2,3],[4,5,6],[7,8,9]]`

| **Rank** | **Shape**                            | **Dimension number**                  | **Example**                           |
| -------- | ------------------------------------ | ------------------------------------- | ------------------------------------- |
| 0        | **Scalar** (magnitude only)          | `s = 483`                             | A 0 - D tensor, `A scalar`            |
| 1        | **Vector** (magnitude and direction) | `v = [1.1, 2.2, 3.3]`                 | A 1 - D tensor with `shape[5]`        |
| 2        | **Matrix** (table of numbers)        | `m = [[1,2,3],[4,5,6],[7,8,9]]`       | A 2 - D tensor with `shape[3, 4]`     |
| 3        | **3-Tensor** (cube of numbers)       | `t = [[[2],[4],[6]], [[8],[10],[12]]` | A 3 - D tensor with `shape[1, 4, 3]`  |
| 4        | **n-Tensor** (you get the idea)      | `...`                                 | A tensor with shape [D0, D1, ..., Dn] |

## Types

- float32를 많이 사용하게 되며, int32도 많이 사용합니다.
- `t = [[1,2,3],[4,5,6],[7,8,9]]`

| **Data Type** | **Python Type** | **Description**         |
| ------------- | --------------- | ----------------------- |
| DT_FLOAT      | **tf.float32**  | 32 bits floating point. |
| DT_DOUBLE     | **tf.float64**  | 64 bits floating point. |
| DT_INT8       | **tf.int8**     | 8 bits signed integer.  |
| DT_INT16      | **tf.int16**    | 16 bits signed integer. |
| DT_INT32      | **tf.int32**    | 32 bits signed integer. |
| DT_INT64      | **tf.int64**    | 64 bits signed integer. |

...
