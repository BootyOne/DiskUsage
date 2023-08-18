import argparse


def create_parser() -> argparse.ArgumentParser:
    parser_in = argparse.ArgumentParser()

    parser_in.add_argument(
        "-c",
        help="Введите каталог, если хотите посмотреть"
             " сколько он весит (Например 'C:\\Life')\n"
             "Введите букву диска, если хотите посмотреть"
             " сколько на нём места занято и "
             "свободного(Например 'С')",
        default=""
    )

    parser_in.add_argument(
        "-s",
        help="Введите букву системы исчесления данных,"
             " в которой будет выведен рузультат("
             "Например 'M'), по стандарту информация"
             " будет выводиться в байтах",
        default="b"
    )

    parser_in.add_argument(
        "-v",
        help="Поставьте этот флаг, если хотите узнать"
             " сколько весит каждая папка/файл в "
             "выбранной директории",
        default=False,
        action='store_true'
    )

    parser_in.add_argument(
        "-g",
        help="Поставьте этот флаг при подсчёте"
             " объёма жесткого диска,"
             " если хотите увидеть график",
        default=False,
        action='store_true'
    )

    parser_in.add_argument(
        "-r",
        help="Поставьте этот флаг, если хотите"
             " учитывать символические ссылки",
        default=False,
        action='store_true'
    )

    parser_in.add_argument(
        "-e",
        help="Поставьте флаг и введите тип(ы) файлов,"
             " тогда только они будут учитываться",
        default=""
    )

    parser_in.add_argument(
        "-i",
        help="Поставьте флаг и введите тип(ы) файлов,"
             "который(е) не хотите учитывать",
        default=""
    )

    return parser_in
