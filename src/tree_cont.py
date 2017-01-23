import tennis_data
import data
import entropy_cont

class Tree:

    name_attrs = []
    entropy_fun = 0

    def __init__(self, datas, cond, avail_attrs, edge):
        self.sons = []
        self.chosen_one = -1
        self.edge = edge
        self.entropy_val = -1
        self.cond = cond
        self.avail_attrs = avail_attrs
        self.datas = [data for data in datas if cond(data)]
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
        labels = {}
        for data in self.datas:
            if not data[-1] in labels:
                labels[data[-1]] = 1
            else:
                labels[data[-1]] += 1
        self.label = max(labels.keys(), key=lambda k:labels[k])
        self.error = len(self.datas) - labels[self.label]
        label_values = {}
        for data_loop in self.datas:
            if not data_loop[-1] in label_values:
                label_values[data_loop[-1]] = 1
            else:
                label_values[data_loop[-1]] += 1
        self.entropy_val = Tree.entropy_fun(label_values)
        if len(self.avail_attrs) == 0 or self.entropy_val == 0:
            return
        [self.chosen_one, attr_entr, bound] = entropy_cont.compute_index_entropy(self.datas,\
                                    self.avail_attrs, Tree.entropy_fun, \
                                    self.entropy_val)
        print(Tree.name_attrs[self.chosen_one])
        print(bound)
        if (attr_entr <= 0):
            return
        new_av_attr = list(self.avail_attrs)

        cond = lambda data, co=self.chosen_one,b=bound: float(data[co]) <= b
        self.set_son(cond, new_av_attr, "<= " + str(bound))
        cond = lambda data, co=self.chosen_one,b=bound: float(data[co]) > b
        self.set_son(cond, new_av_attr, "> " + str(bound))

def init_root(datas, entropy_fun):
    Tree.name_attrs = datas.attr_names
    Tree.entropy_fun = entropy_fun
    return Tree(datas.values, lambda a: True, range(0, len(datas.attr_names) - 1), '')

def print_node(node, f, names):
    node_name = ''
    if node.chosen_one < 0:
        node_name += node.label;
    else:
        node_name += names[node.chosen_one] + '?';
    node_name += ' (' + Tree.entropy_fun.__name__ + "={:1.3f}".format(node.entropy_val) + ')'
    if (node.edge):
        f.write('"' + str(node) + '" [label="' + str(node.edge) + '"];\n')
    f.write('  {"' + str(node) + '" [label="' + node_name + '"]};\n')
    for son in node.sons:
        f.write('  "' + str(node) + '" -> ')
        print_node(son, f, names)
    return

def print_tree(tree):
    names = tree.name_attrs
    f = open('trees/mytree.dot', 'w')
    f.write('digraph g {\n')
    print_node(tree, f, names)
    f.write('}\n')
    f.close()
    return
