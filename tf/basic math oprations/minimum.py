# encoding: utf-8

import tensorflow as tf

arc = tf.constant(30)

my_min = tf.minimum(arc, -1)

with tf.Session() as sess:
    print(sess.run(my_min))