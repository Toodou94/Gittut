# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import tensorflow as tf

a = tf.constant([3])
b = tf.constant([8])
c = tf.add(a,b)

session = tf.Session()

result = session.run(c)

print (result)