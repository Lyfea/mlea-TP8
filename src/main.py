from sys import argv
import tree
import tennis_data
import data
import entropy
import mushroom_data

def main():
    datas = data.get_data_from_file(argv[1])
    entropy_fun = entropy.Entropy
    t = tree.init_root(datas, entropy_fun)
    tree.print_tree(t)


if __name__ == "__main__":
    main()
