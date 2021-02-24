import tensorflow as tf 
a = tf.constant(2)
b = tf.constant([3, 1, 5, 8, 6])
c = tf.constant([[2, 0, 4], [3, 5, 7]])
# Nos exemplos acima, a é um tensor 0-dimensional (escalar), b é 1-dimensional
# (vector) e c é 2-dimensional (matriz)

sess = tf.compat.v1.Session()
saida = sess.run(c)
sess.close()
