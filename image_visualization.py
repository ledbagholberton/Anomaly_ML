#!/usr/bin/env python3
import matplotlib.pyplot as plt


def show_img_inputs(imgs1, imgs2):
    """
        show images (10 random samples from 2 sets)
        - imgs1: first array of images to show
        - imgs2: second array of images to show
        - plot_type: string, values
                - inputs
                -inputvsoutput
                - outputs
    """
    fig, big_axes = plt.subplots(
        figsize=(20.0, 5.0), dpi=100, nrows=2, ncols=1, sharey=True)

    for row, big_ax in enumerate(big_axes, start=1):
        if row == 1:
            big_ax.set_title("Clean Images (random selected)", fontsize=16)
        if row == 2:
            big_ax.set_title(
                "Synthetic Noisy Images (correspond to clean img)",
                fontsize=16)
        big_ax.tick_params(
            labelcolor=(
                1.,
                1.,
                1.,
                0.0),
            top='off',
            bottom='off',
            left='off',
            right='off')
        # removes the white frame
        big_ax._frameon = False

    if len(imgs1) < 10:
        s = len(imgs1)
    else:
        s = 10

    for i in range(s):
        n = i
        if s < 10:
            n = np.random.randint(len(data))
        ax = fig.add_subplot(2, 10, i + 1)
        ax.set_title("clean img#{}".format(n))
        ax.axis('off')
        plt.imshow(imgs1[n])
        ax = fig.add_subplot(2, 10, i + 11)
        ax.set_title("noisy img#{}".format(n))
        ax.axis('off')
        plt.imshow(imgs2[n])
    plt.show()
    plt.close()


def show_img_in_out(imgs_in_clean, imgs_out_clean,
                    imgs_in_anomaly, imgs_out_anomaly,
                    diff_clean, diff_anomaly, thdl):
    """
        - imgs_in: images inputs to the model
        - imgs_out: images outputs from the model
        - diff_clean: list of difference between in and out for
                clean images
        - diff_anomaly: list of difference between in and out for
                images with anomalies.

    """
    fig, big_axes = plt.subplots(
        figsize=(20.0, 5.0), dpi=100, nrows=2, ncols=1, sharey=True)

    for row, big_ax in enumerate(big_axes, start=1):
        if row == 1:
            big_ax.set_title("Input (random selected)", fontsize=16)
        if row == 2:
            big_ax.set_title("Output", fontsize=16)
        big_ax.tick_params(
            labelcolor=(
                1.,
                1.,
                1.,
                0.0),
            top='off',
            bottom='off',
            left='off',
            right='off')
        # removes the white frame
        big_ax._frameon = False

    subtract = np.abs(
        imgs_in_anomaly.astype(
            np.int16) -
        imgs_out_anomaly.astype(
            np.int16))
    greens_anomaly = np.where(subtract < 20, imgs_in_anomaly, [0, 255, 0])

    subtract = np.abs(
        imgs_in_clean.astype(
            np.int16) -
        imgs_out_clean.astype(
            np.int16))
    greens_clean = np.where(subtract < 20, imgs_in_clean, [0, 255, 0])

    samples = imgs_in_clean.shape[0]
    if samples < 10:
        s = samples
    else:
        s = 10

    for i in range(s):
        n = i
        if s < 10:
            n = np.random.randint(samples)
        ax = fig.add_subplot(2, 10, i + 1)
        ax.axis('off')
        if i % 2 == 0:
            ax.set_title("Clean#{}".format(n))
            plt.imshow(imgs_in_clean[n])
        else:
            ax.set_title("With Anomalies#{}".format(n))
            plt.imshow(imgs_in_anomaly[n])

        ax = fig.add_subplot(2, 10, i + 11)
        ax.axis('off')
        if i % 2 == 0:
            if np.abs(diff_clean[n]) < thld:
                ax.set_title(
                    "No Anomalies\n diff:{:.4f}".format(
                        diff_clean[n]))
                plt.imshow(imgs_out_clean[n])
            else:
                ax.set_title(
                    "Anomalies\n detected\n diff:{:.4f}".format(
                        diff_clean[n]))
                plt.imshow(greens_clean[n])
        else:
            if np.abs(diff_anomaly[n]) < thld:
                ax.set_title(
                    "No Anomalies\n diff:{:.4f}".format(
                        diff_anomaly[n]))
                plt.imshow(imgs_out_anomaly[n])
            else:
                ax.set_title(
                    "Anomalies\n detected\n diff:{:.4f}".format(
                        diff_anomaly[n]))
                plt.imshow(greens_anomaly[n])
    plt.show()
    plt.close()


def show_img_eval(img_in, img_out, diff, thld):
    """
        - img_in: model input images
        - img_out: model output images
        - thld: threshold to define if it is anomaly
        - diff: list of values from comparison
    """
    subtract = np.abs(img_in.astype(np.int16) - img_out.astype(np.int16))
    greens = np.where(subtract < 20, data_noise_real, [0, 255, 0])

    fig, big_axes = plt.subplots(
        figsize=(20.0, 5.0), dpi=100, nrows=2, ncols=1, sharey=True)

    for row, big_ax in enumerate(big_axes, start=1):
        if row == 1:
            big_ax.set_title("Input Images (random selected)", fontsize=16)
        if row == 2:
            big_ax.set_title("Output Images", fontsize=16)
        big_ax.tick_params(
            labelcolor=(
                1.,
                1.,
                1.,
                0.0),
            top='off',
            bottom='off',
            left='off',
            right='off')
        # removes the white frame
        big_ax._frameon = False

    samples = img_in.shape[0]
    if len(imgs1) < 10:
        s = len(imgs1)
    else:
        s = 10

    for i in range(s):
        n = i
        if s < 10:
            n = np.random.randint(samples)
        ax = fig.add_subplot(2, 10, i + 1)
        ax.axis('off')
        ax.set_title("Input#{}".format(n))
        plt.imshow(img_in[n])
        ax = fig.add_subplot(2, 10, i + 11)
        ax.axis('off')
        if np.abs(diff[n]) < thld:
            ax.set_title("No Anomalies\n diff:{:.4f}".format(diff[n]))
            plt.imshow(img_out[n])
        else:
            ax.set_title("Anomalies\n detected\n diff:{:.4f}".format(diff[n]))
            plt.imshow(greens[n])
    plt.show()
    plt.close()
