import tennis_data
import data
import entropy

class Tree:

    name_attrs = []

    def __init__(self, datas, cond, avail_attrs, edge):
        self.sons = []
        self.chosen_one = -1
        self.edge = edge
        self.entropy = -1
        self.cond = cond
        self.avail_attrs = avail_attrs
        self.datas = [data for data in datas if cond(data)]
        nb_data_true = 0
        for data in self.datas:
            if data[-1] == 'e':
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
        label_values = {}
        for data_loop in self.datas:
            if not data_loop[-1] in label_values:
                label_values[data_loop[-1]] = 1
            else:
                label_values[data_loop[-1]] += 1
        self.entropy = 0
        tfs = sum(label_values.values())
        self.entropy += tfs / len(self.datas) * entropy.entropy(label_values)
        stop = True
        first_label = self.datas[0][-1]
        for d in self.datas:
            if d[-1] != first_label:
                stop = False
                break
        if stop:
            return
        self.chosen_one = entropy.compute_index_entropy(self.datas, self.avail_attrs)
        new_av_attr = list(self.avail_attrs)
        new_av_attr.remove(self.chosen_one)

        dist_val_attr = set()
        for data in self.datas:
            dist_val_attr.add(data[self.chosen_one])

        for value in dist_val_attr:
            cond = lambda data, co=self.chosen_one,v=value: data[co] == v
            if any(cond(datata) for datata in self.datas):
                self.set_son(cond, new_av_attr, value)

def init_root(datas):
    Tree.name_attrs = datas.attr_names
    return Tree(datas.values, lambda a: True, range(0, len(datas.attr_names) - 1), '')

def print_node(node, f, names):
    if node.chosen_one >= 0:
        f.write('\n[{' + names[node.chosen_one] + '?');
    else:
        f.write('\n[{' + ('True' if node.label else 'False'));
    f.write(' (Entropy=' + "{:1.3f}".format(node.entropy) + ')}')
    if (node.edge):
        f.write(',edge label={node[midway,font=\\scriptsize] {' + str(node.edge) + '}}')
    for son in node.sons:
        print_node(son, f, names)
    f.write(']')
    return

def print_tree(tree):
    names = tree.name_attrs
    f = open('mytree.tex', 'w')
    f.write(\
'\\documentclass[border=5]{standalone}\n\
\\usepackage{forest}\n\
\\begin{document}\n\
\\begin{forest}')
    print_node(tree, f, names)
    f.write('\
\n\\end{forest} \n\
\\end{document}')
    f.close()
    return
