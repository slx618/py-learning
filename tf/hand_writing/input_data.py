# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Functions for downloading and reading MNIST data."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import tempfile

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

mnist = read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf

x = tf.placeholder(dtype=tf.float32, shape=[None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros(10))

y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(dtype=tf.float32, shape=[None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_rate = 0.001
train_step = tf.train.GradientDescentOptimizer(train_rate).minimize(cross_entropy)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    for i in range(3000):
        batch_xs, batch_ys = mnist.train.next_batch(50)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        print(train_step)