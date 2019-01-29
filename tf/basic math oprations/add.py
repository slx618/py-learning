# encoding: utf-8

import tensorflow as tf

num = tf.constant([2, 33], dtype=tf.int32)
num2 = tf.constant([3, 3], dtype=tf.int32)

add_num = tf.add(num, num2)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    result = sess.run(add_num)
    print(type(result))
    print(result)

