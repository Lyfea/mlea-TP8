import data
import tree_cont
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
    list_values = set()
    for data_loop in datas:
        key = data_loop[attr_index]
        list_values.add(key)
        if key not in attr_values:
            attr_values[key] = {}
        if not data_loop[-1] in attr_values[key]:
            attr_values[key][data_loop[-1]] = 1
        else:
            attr_values[key][data_loop[-1]] += 1

    IG = -9999999999
    IGR = -999999999
    bound = -1
    list_values = sorted(list(list_values))
    growing_dic = {}
    decreasing_dic = {}
    for i in list_values:
        for key, value in attr_values[i].items():
            if key in decreasing_dic:
                decreasing_dic[key] += value
            else:
                decreasing_dic[key] = value

    for i in range(0, len(list_values) - 1):
        for key, value in attr_values[list_values[i]].items():
            if key in growing_dic:
                growing_dic[key] += value
            else:
                growing_dic[key] = value
            decreasing_dic[key] -= value
            if decreasing_dic[key] == 0:
                del decreasing_dic[key]

        nbdata = sum(growing_dic.values())
        tmp = nbdata / len(datas)
        IG_tmp = -tmp * entropy_fun(growing_dic)
        IV_tmp = -tmp * math.log2(tmp)
        nbdata = sum(decreasing_dic.values())
        tmp = nbdata / len(datas)
        IG_tmp -= tmp * entropy_fun(decreasing_dic)
        IV_tmp -= tmp * math.log2(tmp)

        if IG_tmp > IG:
            IG = IG_tmp
            bound = (float(list_values[i]) + float(list_values[i + 1])) / 2
        if IG_tmp / IV_tmp > IGR:
            IGR = IG_tmp / IV_tmp
            bound = (float(list_values[i]) + float(list_values[i + 1])) / 2

    IG += cur_node_entropy
    if (IG == 0):
        return 0

    return [IG, bound]

def compute_index_entropy(datas, attr_array, entropy_fun, cur_node_entropy):
    attr_entr = -99999999
    attr_res = -1
    bound = -1
    for attr in attr_array:
        [tmp, bound_tmp] = compute_entropy_attr(datas, attr, entropy_fun, cur_node_entropy)
        if tmp > attr_entr:
            attr_entr = tmp
            attr_res = attr
            bound = bound_tmp
    return [attr_res, attr_entr, bound]
