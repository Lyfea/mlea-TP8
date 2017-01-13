class MushroomData:

    def __init__(self, label, cap_shape, cap_surface, cap_color, bruises, odor,
                 gill_attachment, gill_spacing, gill_size, gill_color,
                 stalk_shape, stalk_root, stalk_surface_ar, stalk_surface_br,
                 stalk_color_ar, stalk_color_br, veil_type, veil_color,
                 ring_number, ring_type, spore_print_color, population, habitat):
        self.label = 1 if label == 'e' else 0
        self.cap_shape = cap_shape
        self.cap_surface = cap_surface
        self.cap_color = cap_color
        self.bruises = bruises 
        self.odor = odor 
        self.gill_attachment = odor 
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.stalk_surface_ar = stalk_surface_ar
        self.stalk_surface_br = stalk_surface_br
        self.stalk_color_ar = stalk_color_ar
        self.stalk_color_br = stalk_color_br
        self.veil_type = veil_type
        self.veil_color = veil_color
        self.ring_number = ring_number
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat

    def __str__(self):
        return str(self.label) + " " + self.cap_shape + " " + self.cap_surface +\
               " " + self.cap_color + " " + self.bruises + " " + self.odor +\
               " " + self.gill_attachment + " " + self.gill_spacing + " " +\
               self.gill_size + " " + self.gill_color + " " + self.stalk_shape +\
               " " + self.stalk_root + " " + self.stalk_surface_ar + " " +\
               self.stalk_surface_br + " " + self.stalk_color_ar + " " +\
               self.stalk_color_br + " " + self.veil_type + " " +\
               self.veil_color + " " + self.ring_number + " " + self.ring_type +\
               " " + self.spore_print_color + " " + self.population + " " +\
               self.habitat

def get_mushroom_data_from_file(f):
    fd = open(f)
    mushroom_datas = []
    for line in fd.readlines():
        data_line = line.split(',')
        data_line[-1] = data_line[-1][0]
        mushroom_data = MushroomData(data_line[0], data_line[1], data_line[2],\
                                     data_line[3], data_line[4], data_line[5],\
                                     data_line[6], data_line[7], data_line[8],\
                                     data_line[9], data_line[10], data_line[11],\
                                     data_line[12], data_line[13], data_line[14],\
                                     data_line[15], data_line[16], data_line[17],\
                                     data_line[18], data_line[19], data_line[20],\
                                     data_line[21], data_line[22])
        mushroom_datas.append(mushroom_data)
    fd.close()
    return mushroom_datas


if __name__ == "__main__":
    mushroom_datas = get_mushroom_data_from_file("../data/mushroom")
    print(len(mushroom_datas))
    print(str(mushroom_datas[0]))
    print(str(mushroom_datas[-1]))
