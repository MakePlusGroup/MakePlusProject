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
            unique_obj_list.append(row[0])

    # Create lists of each unique object
    for item in unique_obj_list:
        list_of_obj_lists = [[item]]
        for row in current_lib:
            if row[0] == item:
                list_of_obj_lists.append(row[1:])

        print(list_of_obj_lists)
        array_to_median = []

        # Convert the entries into median values.
        current_obj = list_of_obj_lists[0][0]

        for i in range(0, len(list_of_obj_lists[1])):
            to_median = []
            for x in range(1, len(list_of_obj_lists)):
                to_median.append(int(list_of_obj_lists[x][i]))
            formatted_to_median = int(np.median(to_median))
            array_to_median.append(formatted_to_median)
        array_to_median.insert(0, current_obj)
        optimized_library.append(array_to_median)

    with open("ref_lib_data.csv", 'w', newline='') as lib_file:
        wr = csv.writer(lib_file, quoting=csv.QUOTE_ALL)
        for eachList in optimized_library:
            wr.writerow(eachList)


if __name__ == '__main__':
    optimize('./hist_data.csv')
