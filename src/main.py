from sys import argv
import tree
import tennis_data
import mushroom_data

def main():
    if argv[1] == "tennis":
        datas = tennis_data.datas_tennis()
    elif argv[1] == "mushroom":
        datas = mushroom_data.get_mushroom_data_from_file(argv[2])
    t = tree.init_root(datas)
    tree.print_tree(t)


if __name__ == "__main__":
    main()
