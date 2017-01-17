import data
import math

def entropy(label_values):
    tfs = sum(label_values.values())
    res = 0
    for value in label_values.values():
        res -= value * math.log2(value / tfs)
    return res / tfs

def compute_entropy_attr(datas, attr_index):
    attr_values = {}
    for data_loop in datas:
        key = data_loop[attr_index]
        if key not in attr_values:
            attr_values[key] = {}
        if not data_loop[-1] in attr_values[key]:
            attr_values[key][data_loop[-1]] = 1
        else:
            attr_values[key][data_loop[-1]] += 1

    res = 0
    for key, label_values in attr_values.items():
        tfs = sum(label_values.values())
        res += tfs / len(datas) * entropy(label_values)

    return res


def compute_index_entropy(datas, attr_array):
    attr_entr = 99999999
    attr_res = -1
    for attr in attr_array:
        tmp = compute_entropy_attr(datas, attr)
        if tmp < attr_entr:
            attr_entr = tmp
            attr_res = attr
        print(tmp)
    return attr_res
