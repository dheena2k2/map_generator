from .map import Map
import yaml


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

    def generate_custom_map(self, parameters):
        """
        Method to add shapes from custom parameters
        :param parameters: custom map parameters
        :return: None
        """
        for shape in parameters:
            for parameter in parameters[shape]:
                params = tuple(parameter)
                if shape == 'circle':
                    self.map.add_circle(*params)
                elif shape == 'rectangle':
                    self.map.add_rectangle(*params)
                elif shape == 'polygon':
                    tuple_params = [tuple(x) for x in params]
                    self.map.add_polygon(tuple_params)
