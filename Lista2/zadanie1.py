import sys
import os


def ex1(filename):
    words_amount = 0
    line_amount = 0
    words_in_line = []
    with open(filename, 'r') as f:
        for line in f:
            line_amount += 1
            words = line.split()
            words_amount += len(words)
            words_in_line.append(len(line))

    print("Number of words: " + str(os.stat(filename).st_size))
    print("Number of words: " + str(words_amount))
    print("Number of lines: " + str(line_amount))
    print("Maximum line length: " + str(max(words_in_line)))


def main():
    try:
        filename = sys.argv[1]
        ex1(filename)
    except IndexError:
        print('To few arguments, please specify a filename')


if __name__ == '__main__':
    main()
