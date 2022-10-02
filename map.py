import numpy as np
from PIL import Image, ImageDraw


class Map:
    """
    Map handling class
    """
    def __init__(self, map_dimension):
        """
        :param map_dimension: dimension of the map to create
        """
        self.map = Image.new('L', map_dimension, 'white')
        self.default_map = self.map.copy()
        self.draw = ImageDraw.Draw(self.map)
        self.dimension = map_dimension

    def add_rectangle(self, x1, y1, x2, y2):
        """
        Add rectangle in map based on diagonally opposite corners
        :param x1: x coordinate of corner 1
        :param y1: y coordinate of corner 1
        :param x2: x coordinate of corner 2
        :param y2: y coordinate of corner 2
        :return: None
        """
        self.draw.rectangle((x1, y1, x2, y2), fill='black')

    def add_circle(self, x, y, r):
        """
        Add Circle in map based on center and radius
        :param x: x coordinate of center
        :param y: y coordinate of center
        :param r: radius
        :return: None
        """
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill='black')

    def add_polygon(self, points):
        """
        Add polygon in map based on collection of points
        :param points: array of (x, y) representing corner points of polygon
        :return: None
        """
        self.draw.polygon(points, fill='black')

    def fix_map(self):
        """
        Fix current map as default map
        :return: None
        """
        self.default_map = self.map.copy()

    def clear_map(self):
        """
        Makes current amp as default map
        :return: None
        """
        self.map = self.default_map.copy()
        self.draw = ImageDraw.Draw(self.map)

    def get_map(self):
        """
        Returns numpy array of current map
        :return: numpy array of map
        """
        return np.array(self.map)
