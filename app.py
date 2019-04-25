#!/usr/bin/env python3
# thoth-init-job
# Copyright(C) 2018, 2019 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This is just a Test."""


import os
import time

import numpy as np
import tensorflow as tf


if __name__ == "__main__":
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    print(f"TensorFlow version: {tf.__version__}, path: {tf.__path__}")

    tf.reset_default_graph()
    with tf.device("/cpu:0"):
        matrix1 = tf.Variable(tf.ones((512, 512), dtype="float64"))
        matrix2 = tf.Variable(tf.ones((512, 512), dtype="float64"))
        product = tf.matmul(matrix1, matrix2)

    times = []
    config = tf.ConfigProto()
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(product.op)

        for i in range(1000):
            start = time.time()
            sess.run(product.op)
            times.append(time.time() - start)

    times_ms = 1000 * np.array(times)
    elapsed_ms = np.median(times_ms)

    ops = 512 ** 3 + (512 - 1) * 512 ** 2
    rate = ops / elapsed_ms / 10 ** 6
    print(
        "%d x %d matmul took:   \t%.4f ms,\t %.2f GFLOPS" % (512, 512, elapsed_ms, rate)
    )
