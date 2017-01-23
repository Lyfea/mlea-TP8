import tennis_data
import operator

class Data:
    def __init__(self, data, attr_names):
        self.attr_names = attr_names
        self.values = data


def get_data_from_file(f):
    fd = open(f)
    attr_names = fd.readline()[:-1].split(',')
    label_index = attr_names.index("label")
    attr_names.remove("label")
    attr_names.append("label")
    datas = []
    for line in fd.readlines():
        data_line = line[:-1].split(',')
        label = data_line[label_index]
        del data_line[label_index]
        data_line.append(label)
        datas.append(data_line)

    bound = int(len(datas) /  7 * 6)
    return [Data(datas[:bound], attr_names), datas[bound:]]



if __name__ == "__main__":
    datas_t = tennis_data.datas_tennis()
    datas = []
    for data in datas_t:
        datas.append(Data(data))
