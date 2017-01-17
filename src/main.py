from sys import argv
import tree
import tennis_data
import data
import mushroom_data

def main():
    datas = data.get_data_from_file(argv[1])
    t = tree.init_root(datas)
    tree.print_tree(t)


if __name__ == "__main__":
    main()
