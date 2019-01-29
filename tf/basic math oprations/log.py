# encoding: utf-8

import tensorflow as tf

num = tf.constant(100, tf.float32)

log = tf.log(num)

with tf.Session() as sess:
    print(sess.run(log))