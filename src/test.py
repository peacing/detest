import os
import argparse

def run(dir_path):
    files = os.listdir(dir_path)
    for f in files:
        print(f'found file: {f}')


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--idir', dest='image_dir',
                        type=str,
                        required=True,
                        help='Path to images for classification.')

    args = parser.parse_args()
    image_dir = args.image_dir                    
    run(image_dir)