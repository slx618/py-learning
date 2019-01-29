# encoding: utf-8

import tensorflow as tf

num = tf.constant(2)

my_max = tf.maximum(num, 999)

with tf.Session() as sess:
    print(sess.run(my_max))