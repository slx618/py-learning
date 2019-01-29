# encoding: utf-8

import tensorflow as tf

num = tf.constant([23.33])

round = tf.round(num)

with tf.Session() as sess:
    print(sess.run(round))