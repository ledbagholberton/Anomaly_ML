import flip
import numpy as np
import uuid
import cv2
import os
import re

# from pypeln import process as pr
from datetime import datetime
from glob import glob
# from tqdm import tqdm

# Global variables
global N_SAMPLES
global BACKGROUNDS_PATTERN
global OBJECTS_PATTERN
global NOISY_IMG_DIR
global N_OBJECTS

# ==============================================================================
# Environment global variables
# ==============================================================================

def add_noise(n_samples=5, n_objects=3, backgronds_pattern="data/images/*",
              objects_pattern="data/objects/*", noisy_img_dir="data/noisy/noisy_img"):
    
    # Number of output images when the data_generator.py is ejecuted
    global N_SAMPLES
    global BACKGROUNDS_PATTERN
    global OBJECTS_PATTERN
    global NOISY_IMG_DIR
    global N_OBJECTS
    
    N_SAMPLES = n_samples

    # Data - path for background images
    BACKGROUNDS_PATTERN = backgronds_pattern

    # Data - path for objects images
    # TODO: Create class selection
    OBJECTS_PATTERN = objects_pattern

    # current now date to create the result folder name for output images
    DATE = datetime.now().strftime("%Y%m%d_%H%M%S")

    # create name for result folder dir
    NOISY_IMG_DIR = noisy_img_dir + "_{}".format(DATE)

    # Object randomization
    # number of objects for full image
    # (1) = only one image -
    # (1,3) = random objects number
    # N_OBJECTS = (1, 5)
    N_OBJECTS = n_objects
    
    create_out_dir()
    setup_environment(OBJECTS_PATTERN, BACKGROUNDS_PATTERN, N_SAMPLES)


# ==============================================================================
# Functions
# ==============================================================================
def create_out_dir():
    """
  Args:
  Description:
    Create an empty folder with the name define in the OUT_DIR var to save the generated data.
  Returns: null
  """
    # make output dir
    os.makedirs(NOISY_IMG_DIR, exist_ok=True)


def setup_environment(objects_pattern, backgrounds_pattern, n_samples):
    """
  Args:
    objects_pattern:      path for objects images
    backgrounds_pattern:  path for background images
    n_samples:            Number of output images when the data_generator.py 
                          is ejecuted
  Description:
  Returns: TODO
  """
    # 'glob' function finds all path_names matching a specified pattern
    # get object paths
    objects_paths = glob(objects_pattern)
    # get background paths
    backgrounds_paths = glob(backgrounds_pattern)

    elements = []
    for idx in range(len(backgrounds_paths)):
        for _ in range(n_samples):
            el = create_element(objects_paths, backgrounds_paths[idx])
            elements.append(el)


def create_element(objects_paths, background_path):
    """
  Args:
  Description:
  Returns:
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
        flip.transformers.data_augmentation.Flip(mode='y'),
        flip.transformers.data_augmentation.RandomResize(
            mode='symmetric_w',
            relation='parent',
            w_percentage_min=0.2,
            w_percentage_max=0.5
        ),
    ]
    
    name1 = background_path.split("\\")[1].split(".")[0]
    name = name1 + "_" + str(uuid.uuid4())

    transform = flip.transformers.Compose(
        [
            flip.transformers.ApplyToObjects(transform_objects),
            flip.transformers.domain_randomization.ObjectsRandomPosition(
                x_min=0.3,
                y_min=0.3,
                x_max=0.7,
                y_max=0.7,
                mode='percentage'
            ),
            flip.transformers.labeler.CreateBoundingBoxes(),
            flip.transformers.domain_randomization.Draw(),
            flip.transformers.io.SaveImage(NOISY_IMG_DIR, name)
        ]
    )

    [el] = transform(el)

    return el


def create_child(path):
    img = flip.utils.inv_channels(cv2.imread(path, cv2.IMREAD_UNCHANGED))
    split_name_temp = re.split(r"/|\\", path)
    index = len(split_name_temp) - 2
    split_name = split_name_temp[index] if index >= 0 else split_name_temp[0]

    obj = flip.transformers.Element(image=img, name=split_name)

    return obj

# ==============================================================================
add_noise(2, 3)