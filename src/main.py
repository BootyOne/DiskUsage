from arg_parser import create_parser
from algorithms import get_free_space, get_paths_size
from visualization import visualize_path, visualize_paths, visualize_disk


def main():
    parser = create_parser()
    args = parser.parse_args()

    type_filter = ""
    types_filter = []
    if args.e:
        types_filter = args.e.split(".")
        type_filter = "e"
    elif args.i:
        types_filter = args.i.split(".")
        type_filter = "i"

    if len(args.c) == 1:
        used = sum(
            get_paths_size(
                f"{args.c.upper()}", args.r,
                type_filter, types_filter
            )[1]
        )
        free = get_free_space(
            f"{args.c.upper()}"
        )
        visualize_disk(args.s, args.g, free, used)
    else:
        if not args.v:
            current_path_size = sum(
                get_paths_size(
                    f"{args.c}", args.r, type_filter, types_filter)[1]
            )
            visualize_path(current_path_size, args.s.upper())
        else:
            current_paths, current_sizes = get_paths_size(
                f"{args.c}", args.r, type_filter,
                types_filter
            )
            visualize_paths(
                current_paths, current_sizes, args.s.upper()
            )


if __name__ == "__main__":
    main()
