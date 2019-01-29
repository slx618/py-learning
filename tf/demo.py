import tensorflow as tf

hello = tf.constant('Hello World')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(2)
b = tf.constant(3)
print(sess.run(a + b))

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)
result = sess.run(product)
print(result)