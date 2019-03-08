import csv
import numpy as np

optimized_library = []


def optimize(file):
    current_lib = []
    obj_list = []
    to_optimize = []
    file_read = open(file, "r")
    file_data = csv.reader(file_read)
    for row in file_data:
        current_line = []
        for cell in row:
            current_line.append(cell)
        current_lib.append(current_line)

    for x, row in enumerate(current_lib):
        print(x, row)
        if row[0] not in obj_list:
            print("new object")
            for i in range(1, 2):
                print(row[i])
                to_optimize.append(row[i])

    print(to_optimize)


if __name__ == '__main__':
    optimize('./hist_data.csv')
