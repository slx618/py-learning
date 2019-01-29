# encoding: utf-8

import tensorflow as tf

num = tf.constant(2, dtype=tf.float32)
num2 = tf.constant(3, dtype=tf.float32)

division = tf.div(num, num2)

with tf.Session() as sess:
    print(sess.run(division))
    print(type(sess.run(division)))

