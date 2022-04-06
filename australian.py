import math
import numpy as np


def readfile(name):
    matrix = list()
    with open(name, "r") as f:
        for line in f.readlines():
            matrix.append(list(map(lambda x: float(x), line.split())))
    return matrix


# def distance(a, b) -> float:
#     return math.sqrt(sum(map(lambda x, y: (y - x) ** 2, a[:-1], b[:-1])))


def euclides_metric(a, b) -> float:
    a = np.array(a) - np.array(b)
    return math.sqrt(np.dot(a, a))


def measure(x, data) -> list:
    result = list()
    for record in data:
        if record == x:
            continue
        result.append((record[-1], euclides_metric(x, record)))
    return result


def group(list) -> dict:
    result = dict()
    for element in list:
        if element[0] not in result.keys():
            result[element[0]] = [element[1]]
        else:
            result[element[0]].append(element[1])
    return result


def sum_distance(dict, k) -> dict:
    for key in dict.keys():
        dict[key].sort()
        dict[key] = sum(dict[key][:k])
    return dict


def decide(dict) -> float:
    result, smallest_sum = list(dict.keys())[0], list(dict.values())[0]
    for key in list(dict.keys())[1:]:
        if dict[key] < smallest_sum:
            smallest_sum, result = dict[key], key
        elif dict[key] == smallest_sum:
            return None
    return result


if __name__ == "__main__":
    test_element = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    file_data = readfile("australian.dat")          # matrix
    tuple_list = measure(test_element, file_data)   # list of tuples (class, distance)
    grouped = group(tuple_list)                     # dict with {class: list of distances}
    summary = sum_distance(grouped, 5)              # dict with {class: sum of k the smallest distances}
    output = decide(summary)                        # class with the smallest sum of k distances

    print(output)
