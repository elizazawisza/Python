import hashlib
import os
import sys


def getFileSize(file):
    return os.stat(file).st_size


def findTheSameFiles(files):
    result = []
    files_len = len(files)
    for i in range(0, files_len):
        for j in range(i + 1, files_len):
            if files[j]['file_info'] == files[i]['file_info']:
                result.append(files[j]['filename'])
                result.append(files[i]['filename'])
    for i in set(result):
        print(i)


def allFilesInfo(directory_name):
    files_info = []
    for root, dirs, files in os.walk(directory_name):
        for name in files:
            file = os.path.join(root, name)
            file_dict = {
                'filename': file,
                'file_info': {
                    'file_size': getFileSize(file),
                    'hash_info': getHashInfo(file)
                }
            }
            files_info.append(file_dict)
    findTheSameFiles(files_info)


def getHashInfo(file):
    buffer_size = 1024 * 128
    sha512 = hashlib.sha512()

    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha512.update(data)
    return sha512.hexdigest()


def main():
    try:
        directory_name = sys.argv[1]
        allFilesInfo(directory_name)
    except IndexError:
        print('To few arguments, please specify a filename')


if __name__ == '__main__':
    main()
