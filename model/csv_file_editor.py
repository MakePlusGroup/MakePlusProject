from ModelClassifier import ModelClassifier
import os
import pandas as pd
import csv
import numpy as np


def write_to_file(open_type, file_location):
    """
    Download files to the scans folder before running. This will allow for more objects to be classified
    and for more precise comparisons

    Disclaimer: This function will take a long time to run!
    :return:
    """
    temp_list = []
    training_files = os.listdir(file_location)
    for file in training_files:
        test_model = ModelClassifier(
            os.path.join(os.path.join(os.path.dirname(__file__), file_location.strip("./")), file))

        hist_data = test_model.generate_distribution_data(test_model.mesh_object.vertices)
        shape_name = file.split("_")
        temp_list.append([shape_name[0], ','.join(map(str, hist_data))])
        print(shape_name[0], "added")

    with open("object_data.csv", open_type) as training_data:
        writer = csv.writer(training_data)
        for line in temp_list:
            writer.writerow(line)


def hist_to_file(open_type, file_location):
    """
    An attempt to save data used for comparison histograms
    :return:
    """
    print_list = []

    training_files = os.listdir(file_location)
    for file in training_files:
        test_model = ModelClassifier(
            os.path.join(os.path.join(os.path.dirname(__file__), file_location.strip("./")), file))

        hist_list = test_model.hist_distribution_data(test_model.mesh_object.vertices)
        shape_name = file.split("_")
        print(hist_list)
        print_list = hist_list.tolist()
        print_list.insert(0, shape_name[0])
        print(print_list)
        print(shape_name[0], "added")

    with open("hist_data.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(print_list)


def read_from_file():
    """
    This is just a test function to determine how the file data will be manipulated or
    if the data was stored correctly
    :return:
    """
    with open("object_data.csv", 'r') as data:
        file_data = pd.read_csv(data, header=None)
        for i in list(file_data.values):
            print(i[0])


if __name__ == '__main__':
    hist_to_file('w', './training')
    # read_from_file()
