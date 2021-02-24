import tensorflow as tf
with tf.compat.v1.Session() as sess:
    frase = tf.constant('Hello, World!')
    saida = sess.run(frase)
    print(saida)
