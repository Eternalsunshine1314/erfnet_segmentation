from __future__ import print_function, division, unicode_literals
import numpy as np
import tensorflow as tf

# from model_base import ImageClassificationModel
# from model_base import PretrainedImageClassificationModel
from data_processing import prepare_data
from model_base import SegmentationModel
import tensorflow as tf

__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"


# ##############################################################################
#                                                                  ARCHITECTURES
# ##############################################################################
# USEFUL LAYERS
fc = tf.contrib.layers.fully_connected
conv = tf.contrib.layers.conv2d
# convsep = tf.contrib.layers.separable_conv2d
deconv = tf.contrib.layers.conv2d_transpose
relu = tf.nn.relu
maxpool = tf.contrib.layers.max_pool2d
dropout_layer = tf.layers.dropout
batchnorm = tf.contrib.layers.batch_norm
# bn_params = {"is_training": self.is_training}
winit = tf.contrib.layers.xavier_initializer()
repeat = tf.contrib.layers.repeat
arg_scope = tf.contrib.framework.arg_scope
l2_regularizer = tf.contrib.layers.l2_regularizer


# ==============================================================================
#                                                               GET_VGG_ARGSCOPE
# ==============================================================================
def get_vgg_argscope(weight_decay=0.0005, use_batch_norm=False, is_training=False):
    """ Gets the arg scope needed for VGG.
    Args:
        weight_decay: The l2 regularization coefficient.
    Returns:
        An arg_scope with the default arguments for layers in VGG .
    """
    with tf.contrib.framework.arg_scope(
        [conv],
        activation_fn=tf.nn.relu,
        normalizer_fn = batchnorm if use_batch_norm else None,
        normalizer_params = {"is_training": is_training},
        weights_regularizer=l2_regularizer(weight_decay),
        biases_initializer=tf.zeros_initializer(),
        trainable = True):
        with tf.contrib.framework.arg_scope([conv], padding='SAME') as scope:
                return scope
