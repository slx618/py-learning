# encoding: utf-8
# 反数

import tensorflow as tf

num = tf.constant(2)
num2 = tf.constant(-2)

negative = tf.negative(num)
negative2 = tf.negative(num2)

print(negative)

with tf.Session() as sess:
    print(sess.run(negative))
    print(sess.run(negative2))