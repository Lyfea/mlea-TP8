import tennis_data
import data
import entropy

class Tree:

    attrs = 0

    def __init__(self, datas, cond, avail_attrs, edge):
        self.sons = []
        self.chosen_one = -1
        self.edge = edge
        self.entropy = 0
        self.cond = cond
        self.avail_attrs = avail_attrs
        self.datas = [data for data in datas if cond(data)]
        nb_data_true = 0
        for data in self.datas:
            if data.datas[-1] == 1:
                nb_data_true += 1
        self.label = nb_data_true > (len(self.datas) / 2)
        self.build()

    def set_son(self, cond, avail_attrs, edge):
        son = Tree(self.datas, cond, avail_attrs, edge)
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
        [self.chosen_one, self.entropy] = entropy.compute_index_entropy(self.datas, self.avail_attrs)
        new_av_attr = list(self.avail_attrs)
        new_av_attr.remove(self.chosen_one)
        for values in self.attrs[self.chosen_one]:
            self.set_son(lambda data: data.datas[self.chosen_one] == values, new_av_attr, values)

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
    return Tree(datas, lambda a: True, range(0, len(datas[0].datas) - 1), '')

def print_node(node, f, names):
    if node.chosen_one >= 0:
        f.write('[' + names[node.chosen_one]);
    else:
        f.write('[' + ('True' if node.label else 'False'));
    if (node.edge):
        f.write(',edge label={node[midway,font=\\scriptsize] {' + str(node.edge) + '}}')
    for son in node.sons:
        print_node(son, f, names)
    f.write(']')
    return

def print_tree(tree):
    names = [a for a, v in sorted(vars(tennis_data.datas_tennis()[0]).items())]
    names.remove('label')
    f = open('mytree.tex', 'w')
    f.write('\\documentclass[border=5]{standalone} \n \
            \\usepackage{forest} \n \
            \\begin{document} \n \
            \\begin{forest} \n \
            ')
    print_node(tree, f, names)
    f.write(' \n \\end{forest} \n \
            \\end{document}')
    f.close()
    return

if __name__ == "__main__":
    t = init_root_tennis()
    print_tree(t)

    data_t = tennis_data.TennisData("Sunny", "Hot", "High", "Weak", 0)
    print(str(data_t))
    print(t.classify(data.Data(data_t)))