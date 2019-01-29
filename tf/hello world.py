# encoding: utf-8

import tensorflow as tf

hello = tf.constant('xx hello world')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))

