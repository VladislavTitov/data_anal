import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('/tmp/data', one_hot=True)

Xtrain = mnist.train.images
ytrain = mnist.train.labels
Xtest = mnist.test.images
ytest = mnist.test.labels

N_PIXELS = 28 * 28
N_CLASSES = 10
HIDDEN_SIZE = 64
EPOCHS = 20
BATCH_SIZE = 64

sess = tf.Session()

x = tf.placeholder(tf.float32, [None, N_PIXELS], name="pixels")
y_label = tf.placeholder(tf.float32, [None, N_CLASSES], name="labels")

W1 = tf.Variable(tf.truncated_normal([N_PIXELS, HIDDEN_SIZE], stddev=N_PIXELS**-0.5))
b1 = tf.Variable(tf.zeros([HIDDEN_SIZE]))

hidden = tf.nn.sigmoid(tf.matmul(x, W1) + b1)

W2 = tf.Variable(tf.truncated_normal([HIDDEN_SIZE, N_CLASSES], stddev=HIDDEN_SIZE**-0.5))
b2 = tf.Variable(tf.zeros([N_CLASSES]))

y = tf.matmul(hidden, W2) + b2

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_label))

accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_label, 1)), tf.float32))

sgd = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
sess.run(tf.global_variables_initializer())
inds = range(Xtrain.shape[0])

for i in xrange(EPOCHS):
    np.random.shuffle(inds)
    for j in xrange(0, len(inds), BATCH_SIZE):
        sess.run(sgd, feed_dict={x: Xtrain[inds[j:j+BATCH_SIZE]], y_label: ytrain[inds[j:j+BATCH_SIZE]]})
    
    print(sess.run([loss, accuracy], feed_dict={x: Xtest, y_label: ytest}))