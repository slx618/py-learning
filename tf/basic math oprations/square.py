# encoding: utf-8
# 平方

import tensorflow as tf

num = tf.constant(2)

square = tf.square(num)

with tf.Session() as sess:
    print(sess.run(square))