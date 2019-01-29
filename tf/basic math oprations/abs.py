# encoding: utf8

import tensorflow as tf

num = tf.constant(-1)
num2 = tf.constant(1)

abs = tf.abs(num)
abs2 = tf.abs(num2)

print(abs)

with tf.Session() as sess:
    print(sess.run(abs))
    print(sess.run(abs2))