# encoding: utf-8

import tensorflow as tf

arc = tf.constant(30, tf.float32)

my_cos = tf.cos(arc)

with tf.Session() as sess:
    print(sess.run(my_cos))
