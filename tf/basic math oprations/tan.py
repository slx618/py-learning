# encoding: utf-8

import tensorflow as tf

arc = tf.constant(30, tf.float32)

my_tan = tf.tan(arc)

with tf.Session() as sess:
    print(sess.run(my_tan))