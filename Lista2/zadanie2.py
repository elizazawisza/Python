import sys

import numpy as np

base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64encode(binary_data):
    result = ''
    index_table = []
    pad = (6 - len(binary_data) % 6) % 6
    binary_data += pad * "0"
    for i in range(0, len(binary_data), 6):
        number = binary_data[i:i + 6]
        index_table.append(int(number, 2))
    for i in range(len(index_table)):
        result += base64chars[index_table[i]]
    return result


def base64decode(base64_data):
    result = ''
    for i in range(0, len(base64_data)):
        letter = base64chars.index(base64_data[i])
        result += np.binary_repr(letter, 6)
    return result


def readFromFile(filename):
    file = open(filename, mode='r')
    file_data = file.read().splitlines()
    file.close()
    return file_data[0]


def writeToFile(result_data, filename):
    file = open(filename, mode='w+')
    file.write(result_data)
    file.close()


def main():
    try:
        option = sys.argv[1]
        sourcefile = sys.argv[2]
        outputfile = sys.argv[3]

        data = readFromFile(sourcefile)
        if option == "--encode":
            result = base64encode(data)
        else:
            result = base64decode(data)
        writeToFile(result, outputfile)
    except IndexError:
        print('To few arguments, please specify a filename')


if __name__ == '__main__':
    main()
