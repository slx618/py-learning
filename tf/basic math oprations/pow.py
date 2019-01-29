# encoding: utf-8

import tensorflow as tf

num = tf.constant(2)

pow = tf.pow(num, 3)

with tf.Session() as sess:
    print(sess.run(pow))