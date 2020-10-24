import argparse
from unittest.mock import patch
import config
import sys


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img-fld', '--images-folder', type=str, required=True)
    parser.add_argument('-segm-out-fld', '--segmentation-output-folder', type=str, required=True, help='Segmentation results')
    parser.add_argument('-tracking-out', '--tracking-output-file', type=str, required=True, help='Tracking results. Extension must be .txt')
    parser.add_argument('-segm-model', '--segmentation-model-file', type=str, default='./pointTrack_weights/best_seed_model.pthCar')
    parser.add_argument('-tracking-model', '--tracking-model-file', type=str, default='./pointTrack_weights/PointTrack.pthCar')
    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    assert args.tracking_output_file.endswith('.txt')
    config.images_folder = args.images_folder
    config.segmentation_output_folder = args.segmentation_output_folder
    config.tracking_output = args.tracking_output_file
    config.segmentation_model_file = args.segmentation_model_file
    config.tracking_model_file = args.tracking_model_file
    print(sys.argv)
    with patch.object(sys, 'argv', ['test_mots_se.py', 'car_test_se_to_save']):
        print(sys.argv)
        import test_mots_se
    with patch.object(sys, 'argv', ['test_tracking.py', 'car_test_tracking_val']):
        print(sys.argv)
        import test_tracking
    print(sys.argv)
