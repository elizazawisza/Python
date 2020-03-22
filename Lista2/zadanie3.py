import os
import sys


def changeNames(directory_name):
    for root, dirs, files in os.walk(directory_name):
        for name in dirs + files:
            os.rename(os.path.join(root, name), os.path.join(root, name.lower()))


def main():
    try:
        directory_name = sys.argv[1]
        changeNames(directory_name)
    except IndexError:
        print('To few arguments, please specify a filename')


if __name__ == '__main__':
    main()
