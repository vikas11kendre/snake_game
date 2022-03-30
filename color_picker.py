

import colorgram
import random

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

class ColorImagePickerList:
    def __init__(self, image_path, number_of_colors):
        self.image_path = image_path
        self.number_of_colors = number_of_colors
        self.color_import = colorgram.extract(self.image_path, self.number_of_colors)
        self.image_color_list = []
        self.random_color=()
        for i in range(0, len(self.color_import)):
            r = self.color_import[i].rgb.r
            g = self.color_import[i].rgb.g
            b = self.color_import[i].rgb.b
            self.image_color_list.append(rgb2hex(r, g, b))
        self.random_color=self.image_color_list[random.randint(0,len(self.color_import))]
k=ColorImagePickerList("cccc.jpg",22)
