from os import listdir
from os.path import join
from os.path import isfile
from os.path import isdir
from compress import compress

import sys

def main():
    try:
        source = sys.argv[1]
        output = sys.argv[2]
        n_colors = int(sys.argv[3])
    except IndexError:
        print("Please provide input and output paths.")
        return

    if isfile(source):
        compress(source, output, n_colors)
    elif isdir(source):
        for f in listdir(source):
            print(f)
            compress(join(source, f), join(output, f), n_colors)

if __name__ == '__main__':
    main()
