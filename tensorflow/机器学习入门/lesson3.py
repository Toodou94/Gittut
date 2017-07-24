# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:50:04 2017

@author: zhangli
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session() # It will print some warnings here.
print(sess.run(hello))