import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)
sess = tf.Session()
print(sess.run([node1, node2]))
print("node3: ", node3)
print(sess.run(node3))
