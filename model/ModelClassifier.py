import numpy as np
import trimesh as tmesh
from random import choice
import matplotlib.pyplot as plt
import os
import pandas as pd
import zipfile
import seaborn as sns
from sklearn import preprocessing
import math


class ModelClassifier:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
        numpy is used to measure distances between any two points in 3 dimensional space as well as
        to compare histograms for classification
    """

    def __init__(self, model):
        """ Loads the model file for processing
            Currently compatible with .obj and .ply files

        Arguments:
            model {file path} -- file path of the model file
        """
        self.mesh_object = tmesh.load(model)
        self.results = []
        self.data = []
        self.existing_data = []
        self.matching_shape = ''
        self.highest = []
        self.big_list = []

    def classify(self):

        """ Main function to generate user input data which is then compared to existing data
            from the object_data.csv file

            More data can be added to improve the number of classifications.
            A real database should be implemented for more robust data storage.
        """
        self.data = preprocessing.scale(self.generate_distribution_data(self.mesh_object.vertices))
        self.results = self.compare_models(self.data)


    def compare_models(self, data):
        # Loads data from object_data.csv

        file_data = self._get_shape_data()
        match_data = [[], []]

        data1 = [x for x in data if str(x) != 'nan']
        loaded_file_data, _ = np.histogram(data1, bins=40)
        self.highest.append(loaded_file_data.tolist())

        # Loop through file_data to find the best matching shape for the input scan
        for shape in file_data:

            compared_list = np.asarray(shape)
            # print('compared list is ', compared_list)
            just_nums = []
            for i in compared_list[1:]:
                just_nums.append(i)

            # Get the minimum data points between two Lists for each index
            minima = np.minimum(just_nums, loaded_file_data)
            # Calculate the percentage of overlap between the two sets of data
            intersection = np.true_divide(np.sum(minima), np.sum(loaded_file_data))
            if shape[0] not in match_data[0]:
                match_data[0].append(shape[0])
                match_data[1].append(intersection * 100)

            elif intersection * 100 >= match_data[1][match_data[0].index(shape[0])]:
                match_data[1][match_data[0].index(shape[0])] = intersection * 100

            if intersection * 100 >= max(match_data[1]):
                just_nums_histo = preprocessing.scale(just_nums)
                self.matching_shape = shape[0]
                self.existing_data = just_nums_histo

        print("loaded file data is ", self.highest)
        return match_data

    def generate_hist(self, data):
        # lite version of compare models which will return histogram details
        data1 = [x for x in data if str(x) != 'nan']

        loaded_file_data, _ = np.histogram(data1, bins=40)

        return loaded_file_data

    def generate_distribution_data(self, vertices):

        """ Generate enough data for precise model comparisons
        Arguments:
            vertices {List} -- a nested list containing the vertices of the loaded model object
        Returns:
            List -- a list containing distances measured between any two random vertices
        """

        distribution_data = []
        for b in range(924):
            for i in range(924 ^ 2):
                distribution_data.append(self._calc_length(vertices))
        return distribution_data

    def hist_distribution_data(self, vertices):

        """ Sends histogram data back csv file editor. Does the same thing as classify function minus compare_models:
            vertices {List} -- a nested list containing the vertices of the loaded model object
        Returns:
            List -- a list containing distances measured between any two random vertices
        """

        distribution_data = []
        for b in range(924):
            for i in range(924 ^ 2):
                distribution_data.append(self._calc_length(vertices))

        hist_data = preprocessing.scale(distribution_data)

        hist_list = self.generate_hist(hist_data)

        return hist_list

    def _calc_length(self, vertices):
        """ Measures the distance between two random points in 3 dimensional space.
            No two points are measured twice to ensure more useful data is collected.
            Can be improved to measure the area of a triangle between any 3 random points.

        Arguments:
            vertices {List} -- a nested list containing the vertices of the loaded model object

        Returns:
            Float -- a distance between two points in 3 dimensional space
        """
        vertex_pair = [choice(vertices), choice(vertices), choice(vertices)]

        while True:
            # Reroll coordinates if they are the same
            if set(vertex_pair[0]).intersection(vertex_pair[1]) == 3 or set(vertex_pair[1]).intersection(
                    vertex_pair[2]) == 3 or set(vertex_pair[0]).intersection(vertex_pair[2]) == 3:
                vertex_pair[0] = choice(vertices)
                vertex_pair[1] = choice(vertices)
                vertex_pair[2] = choice(vertices)
            else:
                break

        area = self.area(vertex_pair)
        return area * 10000

    def show_cubes(self):
        print("in show cubes")
        with open('./model/hist_data.csv', 'r') as data:
            file_data = pd.read_csv(data, header=None)
            list_val = list(file_data.values)

        big_list = []
        for each in list_val:
            if each[0] == 'Cube':

                compared_list = np.asarray(each)
                just_nums = []
                for i in compared_list[1:]:
                    just_nums.append(i)
                big_list.append(just_nums)
        np_array_big = []
        np_array_big.append(np.asarray(big_list[0]))
        np_array_big.append(np.asarray(big_list[1]))
        np_array_big.append(np.asarray(big_list[2]))
        np_array_big.append(np.asarray(big_list[3]))
        np_array_big.append(np.asarray(big_list[4]))

        print('big list is ', np_array_big[0])
        print('big list is ', type(np_array_big[0]))

        for each in np_array_big:
            self.big_list.append(each)
        print(big_list)

        # self.show_histogram(big_list[0], big_list[1], big_list[2], big_list[3], big_list[4])

    # determinant of matrix a
    def det(self, a):
        return a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] - a[0][2] * a[1][
            1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1]

    # unit normal vector of plane defined by points a, b, and c
    def unit_normal(self, a, b, c):
        x = self.det([[1, a[1], a[2]],
                      [1, b[1], b[2]],
                      [1, c[1], c[2]]])
        y = self.det([[a[0], 1, a[2]],
                      [b[0], 1, b[2]],
                      [c[0], 1, c[2]]])
        z = self.det([[a[0], a[1], 1],
                      [b[0], b[1], 1],
                      [c[0], c[1], 1]])

        magnitude = (x ** 2 + y ** 2 + z ** 2) ** .5

        if magnitude == 0:
            magnitude = 1
        return (x / magnitude, y / magnitude, z / magnitude)

    # dot product of vectors a and b
    def dot(self, a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    # cross product of vectors a and b
    def cross(self, a, b):
        x = a[1] * b[2] - a[2] * b[1]
        y = a[2] * b[0] - a[0] * b[2]
        z = a[0] * b[1] - a[1] * b[0]
        return (x, y, z)

    # area of polygon poly
    def area(self, poly):
        if len(poly) < 3:  # not a plane - no area
            return 0

        # mask = np.all(np.isnan(poly), axis=0) | np.all(poly == 0, axis=0)
        # poly = poly[~mask]

        total = [0, 0, 0]
        for i in range(len(poly)):
            vi1 = poly[i]

            if i is len(poly) - 1:
                vi2 = poly[0]
            else:
                vi2 = poly[i + 1]
            prod = self.cross(vi1, vi2)
            total[0] += prod[0]
            total[1] += prod[1]
            total[2] += prod[2]
        result = self.dot(total, self.unit_normal(poly[0], poly[1], poly[2]))
        return abs(result / 2)

    @staticmethod
    def _get_shape_data():
        """ Opens a file containing dimensions of previously scanned objects

        Returns:
            List -- contains list data of previous objects created from generate_distribution_data
        """
        try:
            with open(os.path.join(os.path.dirname(__file__), "hist_data.csv"), 'r') as data:
                file_data = pd.read_csv(data, header=None)

                return list(file_data.values)
        except FileNotFoundError:
            zip_ref = zipfile.ZipFile(os.path.join(
                os.path.dirname(__file__), "object_data.zip"), "r")
            zip_ref.extractall(os.path.dirname(__file__))
            zip_ref.close()
            with open(os.path.join(os.path.dirname(__file__), "object_data.csv"), 'r') as data:
                file_data = pd.read_csv(data, header=None)
                return list(file_data.values)

    @staticmethod
    def show_histogram(data1, data2, data3, data4, data5):
        """ Displays a histogram that visualizes the comparison between the two
        histograms

        Arguments:
            data1 {List} -- Existing Data: contains list data of previous objects created from generate_distribution_data
            data2 {List} -- New Input Data: contains list data of previous objects created from generate_distribution_data
            shape {String} -- Name of the object the input scan is being compared to
        """

        sns.kdeplot(data1, color='blue', label='Cube 1')
        sns.kdeplot(data2, color='red', label='Cube 2')
        sns.kdeplot(data3, color='green', label='Cube 3')
        sns.kdeplot(data4, color='orange', label='Cube 4')
        sns.kdeplot(data5, color='yellow',  label='Cube 5')
        plt.title('Shape Distribution Graph')
        plt.ylabel('Probability')
        plt.xlabel('Distance')
        plt.legend()
        plt.show()

    @staticmethod
    def _get_average(lst):
        """ Returns the average of a List

        Arguments:
            lst {List} -- a 1 dimensional list containing numbers

        Returns:
            Float -- average number of the input list
        """
        return sum(lst) / len(lst)
