import data
import tree
import math

def Entropy(label_values):
    nbdata = sum(label_values.values())
    res = 0
    for value in label_values.values():
        res -= value * math.log2(value / nbdata)
    return res / nbdata

def GiniImpurity(label_values):
    nbdata = sum(label_values.values())
    return sum([(value / nbdata) * (1 - value / nbdata) for value in label_values.values()])

def compute_entropy_attr(datas, attr_index, entropy_fun, cur_node_entropy):
    attr_values = {}
    for data_loop in datas:
        key = data_loop[attr_index]
        if key not in attr_values:
            attr_values[key] = {}
        if not data_loop[-1] in attr_values[key]:
            attr_values[key][data_loop[-1]] = 1
        else:
            attr_values[key][data_loop[-1]] += 1

    IG = 0
    IV = 0
    for key, label_values in attr_values.items():
        nbdata = sum(label_values.values())
        tmp = nbdata / len(datas)
        IG -= tmp * entropy_fun(label_values)
        IV -= tmp * math.log2(tmp)
    IG += cur_node_entropy
    if (IG == 0):
        return 0

    return IG #/ IV

def compute_index_entropy(datas, attr_array, entropy_fun, cur_node_entropy):
    attr_entr = -99999999
    attr_res = -1
    for attr in attr_array:
        tmp = compute_entropy_attr(datas, attr, entropy_fun, cur_node_entropy)
        if tmp > attr_entr:
            attr_entr = tmp
            attr_res = attr
    return [attr_res, attr_entr]
