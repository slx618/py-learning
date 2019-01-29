# encoding: utf-8
# 倒数

import tensorflow as tf

num = tf.constant(100, dtype=tf.float32)
reciprocal = tf.reciprocal(num)

with tf.Session() as sess:
    print(sess.run(reciprocal))
