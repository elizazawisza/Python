def all_subsets(set_list):
    if not set_list:
        return [[]]
    return all_subsets(set_list[1:]) + list(map(lambda elem: [set_list[0]] + elem, all_subsets(set_list[1:])))


print(all_subsets([1, 2, 3]))
