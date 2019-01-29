# encoding: utf-8

import tensorflow as tf

num = tf.constant(2)
num2 = tf.constant(3)

mod = tf.mod(num, num2)

with tf.Session() as sess:
    print(sess.run(mod))