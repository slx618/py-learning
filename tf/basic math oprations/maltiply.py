# encoding: utf-8

import tensorflow as tf

num = tf.constant(3, dtype=tf.float32, name='my_num')
num2 = tf.constant(4, dtype=tf.float32, name='my_num2')

print(num)
print(num2)

multiply = tf.multiply(num, num2, name='my_multiply')

with tf.Session() as sess:
    print(sess.run(multiply))