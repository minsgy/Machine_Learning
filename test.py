import os
import tensorflow as tf

os.environ['TF_CPP_MIN'] = '3'

hello = tf.constant('Hello, Tensorflow!')
sess = tf.session()
print(sess.run(hello))