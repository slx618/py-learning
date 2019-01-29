# encoding: utf-8

import tensorflow as tf
import numpy as np

BATCH_SIZE = 8
seed = 23455

# 模拟样本
rng = np.random.RandomState(seed)
X = rng.rand(32, 2)
Y = [[int(x0 + x1 < 1)] for(x0, x1) in X]
print(Y)

# 占位符
x = tf.placeholder(dtype=tf.float32, shape=(None, 2))
y = tf.placeholder(dtype=tf.float32, shape=(None, 1))

# 定义变量
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 计算过程
a = tf.matmul(x, w1)
y_ = tf.matmul(a, w2)

# 训练
loss = tf.reduce_mean(tf.square(y - y_))
learning_rate = 0.001
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    size = 3000
    for i in range(size):
        start = (i * BATCH_SIZE) % 32
        end = BATCH_SIZE + start

        sess.run(train_step, feed_dict={x: X[start: end], y: Y[start: end]})

    total_loss = sess.run(loss, feed_dict={x: X, y: Y})
