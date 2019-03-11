import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class ShowHistogram:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
        numpy is used to measure distances between any two points in 3 dimensional space as well as
        to compare histograms for classification
    """

    def __init__(self, emp):
        """ Loads the model file for processing
            Currently compatible with .obj and .ply files

        Arguments:
            model {file path} -- file path of the model file
        """
        self.string = emp
        self.highest = []
        self.big_list = []

        with open('./model/hist_data.csv', 'r') as data:
            file_data = pd.read_csv(data, header=None)
            self.list_val = list(file_data.values)

    def find_shapes(self):
        counts = []
        for each in self.list_val:
            if each[0] not in counts:
                counts.append(each[0])
        return counts

    def pop_histo(self, shape):

        big_list = []
        big_list1 = []
        for each in self.list_val:
            if each[0] == shape:

                compared_list = np.asarray(each)
                just_nums = []
                for i in compared_list[1:]:
                    just_nums.append(i)
                big_list.append(just_nums)
        np_array_big = []

        for each in big_list:
            new_np_arr = np.asarray(each)
            np_array_big.append(new_np_arr)

        for each in np_array_big:
            self.big_list.append(each)
            big_list1.append(each)
        return big_list

    def compare_histogram(self):
        """ Displays a histogram that visualizes the comparison between the two
        histograms

        Arguments:
            data1 {List} -- Existing Data: contains list data of previous objects created from generate_distribution_data
            data2 {List} -- New Input Data: contains list data of previous objects created from generate_distribution_data
            shape {String} -- Name of the object the input scan is being compared to
        """

        color = ['orange', 'red', 'blue', 'green', 'black', 'grey', 'pink', 'olive', 'lime', 'navy', 'silver', 'yellow',
                 'grey', 'pink', 'olive', 'lime', '#BC8F8F',
                 'teal', '#AFEEEE', 'green', 'black', 'grey', 'pink', 'olive', 'lime', 'navy', 'silver', 'black',
                 'grey', 'pink', 'olive', 'lime', 'navy',
                 'teal',  'red', 'blue', 'green', 'black', 'grey', 'pink', 'olive', 'lime', 'navy', 'silver', 'black',
                 'grey', '#8FBC8F', 'olive', '#8B4513', '#FA8072',
                 'teal', 'blue', 'green', 'black', 'grey', 'pink', 'olive', 'lime', 'navy', 'silver', 'black',
                 'grey', 'pink', 'olive', '#A52A2A', '#8B0000',
                 'teal']
        counter = 0

        list_shapes = self.find_shapes()
        print(list_shapes)
        for each_shape in list_shapes:
            print(each_shape)
            data_shape = self.pop_histo(each_shape)
            for each in data_shape:
                counter = counter + 1
                sns.kdeplot(each, color=color[counter], label= each_shape + str(counter))
            counter = 0

            plt.title('Shape Distribution Graph')
            plt.ylabel('Probability')
            plt.xlabel('Area')
            plt.legend()
            plt.show()
