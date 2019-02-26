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

    def classify(self):

        """ Main function to generate user input data which is then compared to existing data
            from the object_data.csv file

            More data can be added to improve the number of classifications.
            A real database should be implemented for more robust data storage.
        """

        self.data = preprocessing.scale(self.generate_distribution_data(self.mesh_object.vertices))
        print("printing self.data ", self.data)

        self.results = self.compare_models(self.data)

    def compare_models(self, data):
        print("in compare models")

        """ Compares histograms by determining how much the two graphs intersect

        Arguments:
            data {List} -- contains a list of various distances taken between numerous random points
        Returns:
            Tuple -- a tuple containing the final results of the comparisons
        """

        # Loads data from object_data.csv file
        file_data = self._get_shape_data()
        match_data = [[], []]

        # Loop through file_data to find the best matching shape for the input scan
        for shape in file_data:

            # Convert list entries to float from strings
            compared_data = preprocessing.scale([float(i.strip()) for i in shape[1].split(',')])
            # Create histograms
            print('getting data ', len(compared_data))
            compared_data1 = [x for x in compared_data if str(x) != 'nan']

            classify_data, _ = np.histogram(compared_data1, bins=40)
            print('loaded histograms', classify_data)
            print('getting data ', len(data))

            data1 = [x for x in data if str(x) != 'nan']

            loaded_file_data, _ = np.histogram(data1, bins=40)
            print('success loaded_file_data ', loaded_file_data)

            # Compare histograms
            # Get the minimum data points between two Lists for each index
            print('getting minima')

            minima = np.minimum(classify_data, loaded_file_data)
            # Calculate the percentage of overlap between the two sets of data
            print('minima is ', minima)
            print('getting intersection')

            intersection = np.true_divide(np.sum(minima), np.sum(loaded_file_data))

            if shape[0] not in match_data[0]:
                match_data[0].append(shape[0])
                match_data[1].append(intersection * 100)
                print("shape 0", shape[0])
                print("match data 0", match_data[0])

            elif intersection * 100 >= match_data[1][match_data[0].index(shape[0])]:
                match_data[1][match_data[0].index(shape[0])] = intersection * 100

            if intersection * 100 >= max(match_data[1]):
                self.matching_shape = shape[0]
                self.existing_data = compared_data

            print('intersection is ', intersection)
        return match_data

    def generate_distribution_data(self, vertices):
        print("in gen dist data")

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
            with open(os.path.join(os.path.dirname(__file__), "object_data.csv"), 'r') as data:
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
    def show_histogram(data1, data2, shape):
        """ Displays a histogram that visualizes the comparison between the two
        histograms

        Arguments:
            data1 {List} -- Existing Data: contains list data of previous objects created from generate_distribution_data
            data2 {List} -- New Input Data: contains list data of previous objects created from generate_distribution_data
            shape {String} -- Name of the object the input scan is being compared to
        """

        sns.distplot(data1, bins=40, color='blue', label=shape)
        sns.distplot(data2, bins=40, color='red', label='Input Scan')
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


if __name__ == "__main__":
    mesh = ModelClassifier(
        './scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
