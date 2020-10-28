#!/usr/bin/env python3
"""
Function Denoising Autoencoder
Train an Autoencoder Model with
Inputs: path of directory with Batch of pictures.
Outputs: Model anomaly_autoencoder.mh5
"""

import tensorflow.keras as K

def Convautoencoder(input_dims, filters):
    """ Creates an convolutional autoencoder:
        - input_dims is a tuple of integers containing
                the dimensions of the model input
        - filters is a list containing the number of filters
                for each convolutional layer in the encoder, respectively
                the filters should be reversed for the decoder
        Each convolution uses a kernel size of (3, 3) with same padding and
	relu activation
        The last convolution uses sigmoid activation
        Returns: auto
                - the model
        The autoencoder model is compiled using adam optimization and
        binary cross-entropy loss
    """
    input_encoder = K.Input(shape=input_dims)
    output = input_encoder

    for i in range(len(filters)):
        output = K.layers.Conv2D(filters=filters[i],
                                 kernel_size=3,
                                 padding='same',
                                 activation='relu')(output)

    for i in range(len(filters)-2, -1, -1):
        output = K.layers.Conv2D(filters=filters[i],
                                  kernel_size=3,
                                  padding='same',
                                  activation='relu')(output)


    out_decoder = K.layers.Conv2D(filters=input_dims[-1],
                                  kernel_size=3,
                                  padding='same',
                                  activation='sigmoid')(output)


    auto = K.models.Model(inputs=input_encoder, outputs=out_decoder)
    auto.summary()
    auto.compile(optimizer='Adam',
                 loss='binary_crossentropy')

    return auto
