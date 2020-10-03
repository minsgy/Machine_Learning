# Tensorflow로 파일에서 Data Read

🏅[Edwith](https://www.edwith.org/) - [머신러닝과 딥러닝 BASIC](https://www.edwith.org/others26/joinLectures/9829)

## Loding data from File

- csv, txt File을 불러옴. 그렇다면 어떻게 불러올까?
- `import numpy` 를 사용하여, 파일 값을 불러옵니다.

## 예시

```python
import numpy as np

xy = np.loadtxt('<DATA FILE NAME>', delimiter='<split 할 부분>', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

```

## Slicing

```python

nums = range(5)

print nums # [0,1,2,3,4]
print nums[2:4] # 2,3
print nums[2:] # 2,3,4
print nums[:2] # 0,1
print nums[:] # 0,1,2,3,4
print nums[:-1] # 0,1,2,3

nums[2:4] = [8,9]
print nums # 0,1,8,9,4

```

## indexing , Slicing, Iterating - numpy

```python
b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#   array([
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
# ])

b[:, 1]
# array([2,6,10]) , [모든 행, 1번 열]

b[-1]
# array([9, 10, 11, 12]) , [-1 인덱스 행(전부)]

b[-1, :]
# array([9, 10, 11, 12])

b[0:2, :]
# array([
# [1,2,3,4],
# [5,6,7,8],
#])

```

## Queue Runners

- ![image](https://user-images.githubusercontent.com/60251579/94522312-69380500-026a-11eb-9021-7680c240d7d7.png)

- Step

  1. ```python
     filename_queue = tf.train.string_input_producer(
       ['data-01-test-score.csv', 'data-02-test-score.csv', ...],
       shuffle=False, name='filename_queue)
     )
     ```

  2. ```python
     reader = tf.TextLineReader() # binary도 가능
     key, value = reader.read(filename_queue) # text 파일 읽을 시 일반적
     ```

  3. ```python
      record_defaults = [[0.],[0.],[0.],[0.]]
      xy = tf.decode_csv(value, record_defaults=record_defaults)
     ```

## tf.train.batch

- 위에서 값을 읽어오는 역할을 해주는 `batch`

```python
train_x_batch, train_y_batch = \
  tr.train.batch([xy[0:-1], xy[-1:]], batch_size=10)
  # xy[0:-1] - x_data, xy[-1:] - y_data, batch_size=한번에 가져올 값.

sess = tf.Session()

...

#Start populating the filename queue.
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(2001):
  x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
  ...

coord.request_stop()
coord.join(threads)
```
