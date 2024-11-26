# TODO импортировать необходимые молули

import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r", encoding = "utf-8") as file1:
        csva = csv.DictReader(file1)
        d = [i for i in csva]

    with open(OUTPUT_FILENAME, "w", encoding = "utf-8") as file2:
        json.dump(d, file2, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
