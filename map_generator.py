from .map import Map
import yaml
import numpy as np


def allot_integer(mean_val, std_val, lower_limit=0):
    """
    Method to generate an integer
    :param mean_val: mean value of valid integer distribution
    :param std_val: standard deviation value of valid integer distribution
    :param lower_limit: lowest value the integer can take
    :return:
    """
    curr_val = round(np.random.normal(mean_val, std_val))
    while curr_val < lower_limit:
        curr_val = round(np.random.normal(mean_val, std_val))
    return curr_val


class MapGenerator:
    """
    Class to generate map
    """
    def __init__(self, generator_file_addr):
        """
        Generate map
        :param generator_file_addr: address of generator parameter file
        """
        with open(generator_file_addr, 'r') as file:
            map_data = yaml.safe_load(file)
        map_dimension = tuple(map_data['map_dimension'])
        self.map = Map(map_dimension)
        if map_data['generation_type'] == 'custom':
            self.generate_custom_map(map_data['generation_parameters'])
        elif map_data['generation_type'] == 'random':
            self.generate_random_map(map_data['generation_parameters'])

    def generate_custom_map(self, parameters):
        """
        Method to add shapes from custom parameters
        :param parameters: custom map parameters
        :return: None
        """
        for shape in parameters:
            for parameter in parameters[shape]:
                params = tuple(parameter)
                if 'circle' in shape:
                    self.map.add_circle(*params)
                elif 'rectangle' in shape:
                    self.map.add_rectangle(*params)
                elif 'polygon' in shape:
                    tuple_params = [tuple(x) for x in params]
                    self.map.add_polygon(tuple_params)

    def generate_random_map(self, parameters):
        """
        Method to add shapes randomly from random generation parameters
        :param parameters: custom map parameters
        :return: None
        """
        for shape in parameters:
            curr_parameters = parameters[shape]
            curr_count = allot_integer(
                curr_parameters['mean_count'],
                curr_parameters['std_count']
            )
            for i in range(curr_count):
                if 'circle' in shape:
                    curr_radius = allot_integer(
                        curr_parameters['mean_radius'],
                        curr_parameters['std_radius']
                    )
                    curr_x = np.random.randint(0, self.map.dimension[0])
                    curr_y = np.random.randint(0, self.map.dimension[1])
                    self.map.add_circle(curr_x, curr_y, curr_radius)
                elif 'rectangle' in shape:
                    curr_length = allot_integer(
                        curr_parameters['mean_length'],
                        curr_parameters['std_length']
                    )
                    curr_breadth = allot_integer(
                        curr_parameters['mean_length'],
                        curr_parameters['std_length']
                    )
                    curr_length = int(curr_length / 2)
                    curr_breadth = int(curr_breadth / 2)
                    curr_x = np.random.randint(0, self.map.dimension[0])
                    curr_y = np.random.randint(0, self.map.dimension[1])
                    self.map.add_rectangle(
                        curr_x - curr_length,
                        curr_y - curr_breadth,
                        curr_x + curr_length,
                        curr_y + curr_breadth
                    )
