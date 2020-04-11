import time


def timer(f):
    def modified_f(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print("Duration of function = " + str(end - start))

    return modified_f


@timer
def ex1():
    for _ in range(1000000):
        pass


if __name__ == '__main__':
    ex1()
