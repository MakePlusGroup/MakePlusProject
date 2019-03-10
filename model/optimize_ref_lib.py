import csv
import numpy as np

optimized_library = []


def optimize(file):
    current_lib = []
    unique_obj_list = []
    file_read = open(file, "r")
    file_data = csv.reader(file_read)
    for row in file_data:
        current_line = []
        for cell in row:
            current_line.append(cell)
        current_lib.append(current_line)

    # Adding object types to obj_list
    for x, row in enumerate(current_lib):
        if row[0] not in unique_obj_list:
            print("new object")
            unique_obj_list.append(row[0])

    # Create lists of each unique object
    for item in unique_obj_list:
        list_of_obj_lists = [[item]]
        for row in current_lib:
            if row[0] == item:
                list_of_obj_lists.append(row[1:])

        print(list_of_obj_lists)

        # Convert the entries into median values.

        for i, obj_list in list_of_obj_lists:
            print(i, obj_list)


if __name__ == '__main__':
    optimize('./hist_data.csv')
