types = {list, tuple, set}

def calculate_structure_sum(*args):
    res = 0
    for i in args:
        if type(i) in types:
            res += calculate_structure_sum(*i)
        else:
            if isinstance(i, int) or isinstance(i, float):
                res += i
                continue
            if isinstance(i, str):
                res += len(i)
                continue
            if isinstance(i, dict):
                for key,val in i.items():
                    if type(key) == int:
                        res += key
                    else:
                        res += len(key)
                    if type(val) == int:
                        res += val
                    else:
                        res += len(val)
                    continue
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
