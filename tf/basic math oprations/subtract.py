# encoding: utf-8

import tensorflow as tf

num = tf.constant(3, dtype=tf.float32)
num2 = tf.constant(3, dtype=tf.float32)
num3 = tf.constant(6, dtype=tf.float32)

subtract = tf.subtract(num, num2, name='my_subtract')
print(subtract)

with tf.Session() as sess:
    print(sess.run(subtract))