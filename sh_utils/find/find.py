import argparse
import os
from glob import glob


TYPE_FILE = 0
TYPE_FOLDER = 1

def parse_args():
    parser = argparse.ArgumentParser(description='find searches the directory tree rooted at each given starting-point by evaluating the given expression from left to right')
    parser.add_argument('path', help='path to search', type=str, nargs='?', default='.')
    parser.add_argument('-name', help='file name', type=str, default='*')
    parser.add_argument('-type', help='file type', type=str)
    args = parser.parse_args()

    return args


def find(path, pattern):
    result = []
    scanned_folders = []
    folders_queue = [os.path.join(path, d) for d in os.listdir(path)]

    while True:
        current_dir = folders_queue.pop()
        if current_dir in scanned_folders:
            continue

        scanned_folders.append(current_dir)

        for match in glob(os.path.join(current_dir, pattern)):
            if os.path.isfile(match):
                result.append({'path': match, 'type': TYPE_FILE})
            elif os.path.isdir(match):
                result.append({'path': match, 'type': TYPE_FOLDER})
                folders_queue.append(match)

        if not folders_queue:
            break

    return result


def main():
    args = parse_args()
    found = find(args.path, args.name)
    filtered = []

    if args.type == 'd':
        filtered = [f['path'] for f in found if f['type'] == TYPE_FOLDER]
    else:
        filtered = [f['path'] for f in found]
    
    print('\n'.join(filtered))

if __name__ == '__main__':
    main()
