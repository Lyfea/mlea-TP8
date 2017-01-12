import tennis_data
import data
import entropy

class Tree:

    attrs = 0

    def __init__(self, datas, cond, avail_attrs):
        self.sons = []
        self.cond = cond
        self.avail_attrs = avail_attrs
        self.datas = [data for data in datas if cond(data)]
        count = 0
        for data in self.datas:
            if data.datas[-1] == 1:
                count += 1
        self.label = count > (len(self.datas) / 2)
        self.build()

    def set_son(self, cond, avail_attrs):
        son = Tree(self.datas, cond, avail_attrs)
        self.sons.append(son)

    def classify(self, data):
        for son in self.sons:
            if son.cond(data):
                return son.classify(data)
        return self.label

    def build(self):
        if len(self.avail_attrs) == 0:
            return
        stop = True
        nb_label = self.datas[0].datas[-1]
        for d in self.datas:
            if d.datas[-1] != nb_label:
                stop = False
                break
        if stop:
            return
        chosen_one = entropy.compute_index_entropy(self.datas, self.avail_attrs)
        new_av_attr = list(self.avail_attrs)
        new_av_attr.remove(chosen_one)
        for values in self.attrs[chosen_one]:
            self.set_son(lambda data: data.datas[chosen_one] == values, new_av_attr)

def init_root_tennis():
    datas_t = tennis_data.datas_tennis()
    datas = []
    for d in datas_t:
        datas.append(data.Data(d))
    attrs = [ set() for _ in range(0, len(datas[0].datas) - 1) ]
    for data_loop in datas:
        for i in range(0, len(data_loop.datas) - 1):
            attrs[i].add(data_loop.datas[i])
    Tree.attrs = attrs
    return Tree(datas, lambda a: True, range(0, len(datas[0].datas) - 1))

def print_tree(tree):
    print("Tree:")
    for data in tree.datas:
        print(data)
    print("-----------------")
    for son in tree.sons:
        print_tree(son)

if __name__ == "__main__":
    t = init_root_tennis()
    print_tree(t)

    data_t = tennis_data.TennisData(3, 1, 2, 2, 1)
    print(t.classify(data.Data(data_t)))
