# encoding: utf-8
# e的指数

import tensorflow as tf

num = tf.constant(8, tf.float32)

exp = tf.exp(num)

with tf.Session() as sess:
    print(sess.run(exp))