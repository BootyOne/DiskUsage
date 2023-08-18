from typing import NoReturn

import matplotlib.pyplot as plt


def visualize_disk(types: str, need_schedule: bool, free_in: float, used_in: float) -> NoReturn:
    size = ["K", "M", "G"]
    for i in range(size.index(types.upper()) + 1):
        free_in /= 1024
        used_in /= 1024
    if need_schedule:
        vals = [free_in, used_in]
        labels = [
            f"Free: {free_in:1.2f} {types.upper()}b",
            f"Used: {used_in:1.2f} {types.upper()}b"
        ]
        fig, ax = plt.subplots()
        ax.pie(vals, labels=labels)
        ax.axis("equal")
        plt.show()
    else:
        print(
            f"Free: {free_in:1.2f} {types.upper()}b\n"
            f"Used: {used_in:1.2f} {types.upper()}b"
        )


def visualize_path(path_size: float, types: str) -> NoReturn:
    size = ["K", "M", "G"]
    for i in range(size.index(types) + 1):
        path_size /= 1024
    print(f"Path size: {path_size:1.2f} {types}b")


def visualize_paths(paths: list, sizes: list, types: str) -> NoReturn:
    size = ["K", "M", "G"]
    for e in range(len(sizes)):
        for i in range(size.index(types) + 1):
            sizes[e] /= 1024
    for i in range(len(sizes)):
        print(
            f"Size: {sizes[i]:1.2f} {types}b"
            f" {' ':<10} path: {paths[i]}"
        )
