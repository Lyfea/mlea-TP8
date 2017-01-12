import tennis_data
import operator

class Data:
    def __init__(self, data):
        self.datas = []
        self.str = str(data)
        for attr, value in sorted(vars(data).items()):
            if attr != "label":
                self.datas.append(value)
        self.datas.append(data.label)

    def __str__(self):
        return self.str



if __name__ == "__main__":
    datas_t = tennis_data.datas_tennis()
    datas = []
    for data in datas_t:
        datas.append(Data(data))
