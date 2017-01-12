import data
import math

def entropy(tf):
    if tf[0] == 0 or tf[1] == 0:
        return 0
    tfs = tf[0] + tf[1]
    return -(tf[0] * math.log2(tf[0] / tfs) + tf[1] * math.log2(tf[1] / tfs)) / tfs

def compute_entropy_attr(datas, attr_index):
    attr_values = {}
    for data_loop in datas:
        key = data_loop.datas[attr_index]
        if key not in attr_values:
            attr_values[key] = [0, 0]
        attr_values[key][data_loop.datas[-1]] += 1

    res = 0
    for key, t_f in attr_values.items():
        if t_f[0] != 0 and t_f[1] != 0:
            tfs = t_f[0] + t_f[1]
            res += tfs / len(datas) * entropy(t_f)

    return res
    """
    attr_values = {}
    count_true_label = 0
    for data_loop in datas:
        key = data_loop.datas[attr_index]
        if data_loop.datas[-1] == 0:
            if key not in attr_values:
                attr_values[key] = 0
            attr_values[key] += 1
            count_true_label += 1

    res = 0
    print("Attribut: " + str(attr_index))
    for key, true_knowing_key in attr_values.items():
        print(str(key) + ": " + str(true_knowing_key) + ", " + str(count_true_label))
        res -= (true_knowing_key / count_true_label) * math.log(true_knowing_key / count_true_label, 4)
    return res
    """



def compute_index_entropy(datas, attr_array):
    value_res = 99999999
    attr_res = -1
    for attr in attr_array:
        tmp = compute_entropy_attr(datas, attr)
        if tmp < value_res:
            value_res = tmp
            attr_res = attr
        print(tmp)
    return attr_res
