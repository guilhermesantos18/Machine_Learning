import tensorflow as tf

with tf.compat.v1.Session() as sess:
    a = tf.constant(5)
    b = tf.constant(3)
    c = tf.constant(2)

    d = tf.multiply(a, b)
    e = tf.add(b, c)
    f = tf.subtract(d, e)
    saida = sess.run(f)
    print(saida)
sess.close()
