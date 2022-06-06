import sys
import argparse
import algorithms
import matplotlib.pyplot as plt


def create_parser():
    parser_in = argparse.ArgumentParser()
    parser_in.add_argument("-c",
                           help="Введите каталог, если хотите посмотреть"
                                " сколько он весит (Например 'C:\\Life')\n"
                                "Введите букву диска, если хотите посмотреть"
                                " сколько на нём места занято и "
                                "свободного(Например 'С')",
                           default="")
    parser_in.add_argument("-s",
                           help="Введите букву системы исчесления данных,"
                                " в которой будет выведен рузультат("
                                "Например 'M'), по стандарту информация"
                                " будет выводиться в байтах",
                           default="b")
    parser_in.add_argument("-v",
                           help="Поставьте этот флаг, если хотите узнать"
                                " сколько весит каждая папка/файл в "
                                "выбранной директории",
                           default=False, action='store_true')
    parser_in.add_argument("-g",
                           help="Поставьте этот флаг при подсчёте"
                                " объёма жесткого диска,"
                                " если хотите увидеть график",
                           default=False, action='store_true')
    parser_in.add_argument("-r",
                           help="Поставьте этот флаг, если хотите"
                                " учитывать символические ссылки",
                           default=False, action='store_true')
    parser_in.add_argument("-e",
                           help="Поставьте флаг и введите тип(ы) файлов,"
                                " тогда только они будут учитываться",
                           default="")
    parser_in.add_argument("-i",
                           help="Поставьте флаг и введите тип(ы) файлов,"
                                "который(е) не хотите учитывать",
                           default="")
    return parser_in


def visualize_disk(free_in, used_in):
    size = ["K", "M", "G"]
    for i in range(size.index(args.s.upper()) + 1):
        free_in /= 1024
        used_in /= 1024
    if args.g:
        vals = [free_in, used_in]
        labels = [f"Free: {free_in:1.2f} {args.s.upper()}b",
                  f"Used: {used_in:1.2f} {args.s.upper()}b"]
        fig, ax = plt.subplots()
        ax.pie(vals, labels=labels)
        ax.axis("equal")
        plt.show()
    else:
        print(f"Free: {free_in:1.2f} {args.s.upper()}b\n"
              f"Used: {used_in:1.2f} {args.s.upper()}b")


def visualize_path(pathe_size, types):
    size = ["K", "M", "G"]
    for i in range(size.index(types) + 1):
        pathe_size /= 1024
    print(f"Path size: {pathe_size:1.2f} {types}b")


def visualize_paths(pathes, sizs, types):
    size = ["K", "M", "G"]
    for e in range(len(sizs)):
        for i in range(size.index(types) + 1):
            sizs[e] /= 1024
    for i in range(len(sizs)):
        print(f"Size: {sizs[i]:1.2f} {types}b"
              f" {' ':<10} path: {pathes[i]}")


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    os = sys.platform

    filter_type = ""
    filter_types = []
    if args.e:
        filter_types = args.e.split(".")
        filter_type = "e"
    elif args.i:
        filter_types = args.i.split(".")
        filter_type = "i"

    if len(args.c) == 1:
        used = sum(algorithms.get_paths_size(
            f"{args.c.upper()}", args.r,
            filter_type, filter_types)[1])
        free = algorithms.get_free_space(
            f"{args.c.upper()}")
        visualize_disk(free, used)
    else:
        if not args.v:
            path_size = sum(algorithms.get_paths_size(f"{args.c}",
                                                      args.r,
                                                      filter_type,
                                                      filter_types)[1])
            visualize_path(path_size, args.s.upper())
        else:
            paths, sizes = algorithms.get_paths_size(
                f"{args.c}", args.r, filter_type,
                filter_types)
            visualize_paths(paths, sizes, args.s.upper())
