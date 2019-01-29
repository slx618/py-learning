# encoding: utf-8
# 平方根

import tensorflow as tf

num = tf.constant(9, dtype=tf.float32)
sqrt = tf.sqrt(num)

with tf.Session() as sess:
    print(sess.run(sqrt))