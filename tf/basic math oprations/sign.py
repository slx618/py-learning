# encoding: utf-8
# 返回正数 负数符号

import tensorflow as tf

num = tf.constant(2)
num2 = tf.constant(100)
num3 = tf.constant(-100)
num4 = tf.constant(0)

sign = tf.sign(num)
sign2 = tf.sign(num2)
sign3 = tf.sign(num3)
sign4 = tf.sign(num4)

with tf.Session() as sess:
    print(sess.run(sign))
    print(sess.run(sign2))
    print(sess.run(sign3))
    print(sess.run(sign4))