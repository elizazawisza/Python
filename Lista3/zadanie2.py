nestedList = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]


def flatten(given_list):
    for item in given_list:
        if isinstance(item, list):
            for element in flatten(item):
                yield element
        else:
            yield item


print(list(flatten(nestedList)))
