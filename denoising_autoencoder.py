#!/usr/bin/env python3
import tensorflow.keras as K
import tensorflow as tf
import numpy as np
import os
"""
Function Denoising Autoencoder
Train an Autoencoder Model with
Inputs: path of directory with Batch of pictures.
Outputs: Model anomaly_autoencoder.mh5
"""


def Convautoencoder(input_dims, filters):
    """ Creates an convolutional autoencoder:
        - input_dims is a tuple of integers containing
                the dimensions of the model input
        - filters is a list containing the number of filters
                for each convolutional layer in the encoder, respectively
                the filters should be reversed for the decoder

        Each convolution in the uses a kernel size of (3, 3)
        with same padding and relu activation

        The last convolution should have the same number of filters as the
        number of channels in input_dims with sigmoid activation

        Returns:
                - auto is the full autoencoder model

    """
    input_encoder = K.Input(shape=input_dims)
    output = input_encoder

    for i in range(len(filters)):
        output = K.layers.Conv2D(filters=filters[i],
                                 kernel_size=3,
                                 padding='same',
                                 dilation_rate=3,
                                 activation='relu')(output)

    for i in range(len(filters) - 2, -1, -1):
        output = K.layers.Conv2D(filters=filters[i],
                                 kernel_size=3,
                                 padding='same',
                                 dilation_rate=3,
                                 activation='relu')(output)

    out_decoder = K.layers.Conv2D(filters=input_dims[-1],
                                  kernel_size=3,
                                  padding='same',
                                  activation='sigmoid')(output)

    def ssim_loss(y_true, y_pred):
        return tf.reduce_mean(1 - tf.image.ssim(y_true, y_pred, 1.0))

    auto = K.models.Model(inputs=input_encoder, outputs=out_decoder)
    auto.summary()
    auto.compile(optimizer='Adam',
                 metrics=['mse', 'acc'],
                 loss=ssim_loss)

    return auto


def preprocess(train_dataset, validation_dataset):
    x_train, y_train = train_dataset
    x_validation, y_validation = validation_dataset
    # normalizing
    x_train = x_train.astype('float32') / 255.
    x_validation = x_validation.astype('float32') / 255.
    y_train = y_train.astype('float32') / 255.
    y_validation = y_validation.astype('float32') / 255.

    return x_train, y_train, x_validation, y_validation


def train(train_dataset, validation_dataset, input_size, filters):
    """
        - train_datset: 2 arrays for training (in and out)
        - validation_dataset: 2 arrays for training (in and out)
        - input_size: input image shape without channels
        - filters: list if number of filter per layer
    """

    x_train, y_train, x_val, y_val = preprocess(
        train_dataset, validation_dataset)
    np.random.seed(0)
    tf.random.set_seed(0)
    auto = Convautoencoder((227, 227, 3), filters)

    early_stop = K.callbacks.EarlyStopping(monitor='loss', patience=3)

    auto.fit(x_train, y_train, epochs=30, batch_size=32, shuffle=True,
             validation_data=(x_val, y_val),
             callbacks=[early_stop])

    if not os.path.exists('Model'):
                os.makedirs('Model')

    auto.save("./Model/autoencoder.h5")

    return auto
