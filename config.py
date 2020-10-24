"""
Author: Zhenbo Xu
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import os
import sys

project_root = os.path.dirname(os.path.realpath(__file__))
category_embedding = [[0.9479751586914062, 0.4561353325843811, 0.16707628965377808], [0.1,-0.1,0.1], [0.5455077290534973, -0.6193588972091675, -2.629554510116577], [-0.1,0.1,-0.1]]

# systemRoot = "/home/ajin/"
images_folder = None  # path to images
segmentation_output_folder = None  # path to save segmentation
tracking_output = None  # file to save tracking results
segmentation_model_file = None  # model for segmentation
tracking_model_file = None  # model for tracking
# rootDir = os.path.join(systemRoot, 'PointTrack')
python_path = sys.executable
