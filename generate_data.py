import flip
import numpy as np
import uuid
import cv2
import os
import re
import matplotlib.pyplot as plt
from glob import glob

"""
Generate dataset with synthetic data
"""

# ============================================================================
# Functions
# ============================================================================


def generate_data(n_samples=5, n_objects=3, objects_pattern="data/objects/*",
                  backgronds_pattern="data/Casting_Similar_95/*", show=False,
                  output_dir="data/noisy/noisy_img"):
    """
    Function that creates and setups the global variables and
    start the creation of the data

    - n_samples: number of new images to create for each background
    - n_objects: object number to place in each new image
    - objects_pattern: path where are the images to use as objects or noise
    - backgrounds_pattern: path where are the images to use as background
    - show: if True it shows some images created else they are not shown
    - output_dir: path where the generated images will be saved
    """

    # Environment global variables
    global N_SAMPLES
    global BACKGROUNDS_PATTERN
    global OBJECTS_PATTERN
    global OUTPUT_DIR
    global N_OBJECTS
    global SHOW

    # Setup global variables
    SHOW = show
    N_SAMPLES = n_samples
    BACKGROUNDS_PATTERN = backgronds_pattern
    OBJECTS_PATTERN = objects_pattern
    OUTPUT_DIR = output_dir
    N_OBJECTS = n_objects

    # creates an empty folder
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    setup_environment(OBJECTS_PATTERN, BACKGROUNDS_PATTERN, N_SAMPLES)


def setup_environment(objects_pattern, backgrounds_pattern, n_samples):
    """
    Call function that generates synthetic data
    and shows some images if SHOW is True

    - objects_pattern: path for objects images
    - backgrounds_pattern: path for background images
    - n_samples: number of new images to create for each background
  """

    # get object paths
    objects_paths = glob(objects_pattern)

    # get background paths
    backgrounds_paths = glob(backgrounds_pattern)

    if SHOW is True:
        n_background = len(backgrounds_pattern)
        n_w = 6
        n_h = 5
        fig = plt.figure(figsize=(n_h, n_w))
        n_fig = 1
        aux = 1

    # iterate all backgrounds
    for idx in range(len(backgrounds_paths)):

        if SHOW is True and aux <= n_h:
            background = flip.utils.inv_channels(
                cv2.imread(backgrounds_paths[idx], cv2.IMREAD_UNCHANGED,)
            )
            fig.add_subplot(n_h, n_w, n_fig)
            plt.title("original")
            plt.imshow(background)
            plt.axis("off")
            n_fig += 1
            aux += 1
            temp = 1

        # create a new image until reaching n_samples
        for sample in range(n_samples):
            el = create_element(objects_paths, backgrounds_paths[idx])

            if SHOW is True and temp <= n_w - 1:
                image = el.created_image
                fig.add_subplot(n_h, n_w, n_fig)
                plt.title(sample + 1)
                plt.imshow(image)
                plt.axis('off')
                n_fig += 1
                temp += 1

        if SHOW is True and aux == n_h + 1:
            plt.tight_layout(pad=2)
            plt.show()
            aux += 1


def create_element(objects_paths, background_path):
    """
    Function that generates and saves the synthetic images

    - objects_paths: path where images that will be used as elements are saved
    - background_path: path where images that will be used as backgrounds are

    Returns: Element class instance
    """
    # Check if N_OBJECTS is iterable and define amount of objects
    if hasattr(N_OBJECTS, "__iter__"):
        n_objs = np.random.randint(low=N_OBJECTS[0], high=N_OBJECTS[1] + 1)
    else:
        n_objs = N_OBJECTS

    # get random elements
    object_idxs = np.random.choice(objects_paths, n_objs)

    # Create elements for the object images
    objects = [create_child(i) for i in object_idxs]

    # get background
    background_image = flip.utils.inv_channels(
        cv2.imread(background_path, cv2.IMREAD_UNCHANGED,)
    )

    # create new element
    el = flip.transformers.Element(image=background_image, objects=objects)

    # Transformer element
    transform_objects = [
        flip.transformers.data_augmentation.Rotate(mode='random'),
        flip.transformers.data_augmentation.Flip(mode='random'),
        flip.transformers.data_augmentation.RandomResize(
            mode='symmetric_w',
            relation='parent',
            w_percentage_min=0.2,
            w_percentage_max=0.7,
        ),
    ]

    name1 = background_path.split("\\")[1].split(".")[0]
    name = name1 + "__" + str(uuid.uuid4())

    transform = flip.transformers.Compose(
        [
            flip.transformers.ApplyToObjects(transform_objects),
            flip.transformers.domain_randomization.ObjectsRandomPosition(
                x_min=0.0,
                y_min=0.0,
                x_max=0.7,
                y_max=0.7,
                mode='percentage'
            ),
            flip.transformers.domain_randomization.Draw(),
            flip.transformers.io.SaveImage(OUTPUT_DIR, name)
        ]
    )

    [el] = transform(el)

    return el


def create_child(path):
    """
    Function that creates child-type instances of the Element class

    Return: Element instance
    """

    # reads image and changes the order of channels
    img = flip.utils.inv_channels(cv2.imread(path, cv2.IMREAD_UNCHANGED))

    # saves image name
    split_name_temp = re.split(r"/|\\", path)
    index = len(split_name_temp) - 1
    split_name = split_name_temp[index] if index >= 0 else split_name_temp[0]

    # creates Element child instance
    element_instance = flip.transformers.Element(image=img, name=split_name)

    return element_instance

# ==============================================================================
generate_data(1, 1,
              backgronds_pattern="data/backgrounds/*",
              objects_pattern="data/objects/*",
              output_dir="data/output",
              show=False)
