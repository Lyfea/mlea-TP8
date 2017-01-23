from sys import argv
import tree
import data
import entropy
import pruning

def main():
    [datas, datas_test] = data.get_data_from_file(argv[1])
    entropy_fun = entropy.Entropy
    t = tree.init_root(datas, entropy_fun)
    pruning.pruning(t)
    tree.print_tree(t)

    goods = 0
    for d in datas_test:
        if d[-1] == t.classify(d):
            goods += 1
    print(str((goods / len(datas_test)) * 100))

if __name__ == "__main__":
    main()
