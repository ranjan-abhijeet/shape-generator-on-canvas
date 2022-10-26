"""
Generate an image with random shapes, labeled with bounding boxes.

The image is populated with random shapes with random sizes, random locations,
and random colors, with or without overlap.

Shapes have random (row, col) starting coordinates and random sizes bounded 
by min_size and max_size.

It can occur that a randomly generated shape will not fit the image at all. 
In that case, the algorithm will try again with new starting coordinates a certain 
number of times. However, it also means that some shapes may be skipped altogether. 
In that case, this function will generate fewer shapes than requested.

"""
import matplotlib.pyplot as plt

from skimage.draw import random_shapes

GRID_SIZE = (128, 128)
OBJECT_SHAPE = 'rectangle' # {rectangle, circle, triangle, ellipse, None}
MAX_OBJECTS = 30
MIN_OBJECTS = 10
# RANDOM_SEED = 43
ALLOW_OVERLAP = False

for i in range(10):
    result = random_shapes(
                        image_shape=GRID_SIZE,
                        max_shapes=MAX_OBJECTS,
                        min_shapes=MIN_OBJECTS, 
                        shape=OBJECT_SHAPE,
                        allow_overlap=ALLOW_OVERLAP,
                        channel_axis=2,
                        random_seed=None)

    image, labels = result
    # Uncomment below line to see info regarding the shapes
    # print(f'Image shape: {image.shape}\nLabels: {labels}')

    plt.imshow(image)
    plt.axis('off')
    plt.savefig(f"/home/abhijeet/Desktop/recycle_bin/{i}.png")
