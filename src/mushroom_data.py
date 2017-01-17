class MushroomData:

    name_attrs = ["capshape", " capsurface", " capcolor", " bruises", " odor",
                 "gillattachment", " gillspacing", " gillsize", " gillcolor",\
                 "stalkshape", " stalkroot", " stalksurfacear", " stalksurfacebr",\
                 "stalkcolorar", " stalkcolorbr", " veiltype", " veilcolor",\
                 "ringnumber", " ringtype", " sporeprintcolor", " population", " habitat"]

    def __init__(self, label, capshape, capsurface, capcolor, bruises, odor,
                 gillattachment, gillspacing, gillsize, gillcolor,
                 stalkshape, stalkroot, stalksurfacear, stalksurfacebr,
                 stalkcolorar, stalkcolorbr, veiltype, veilcolor,
                 ringnumber, ringtype, sporeprintcolor, population, habitat):
        self.label = 1 if label == 'e' else 0
        self.capshape = capshape
        self.capsurface = capsurface
        self.capcolor = capcolor
        self.bruises = bruises 
        self.odor = odor 
        self.gillattachment = odor 
        self.gillspacing = gillspacing
        self.gillsize = gillsize
        self.gillcolor = gillcolor
        self.stalkshape = stalkshape
        self.stalkroot = stalkroot
        self.stalksurfacear = stalksurfacear
        self.stalksurfacebr = stalksurfacebr
        self.stalkcolorar = stalkcolorar
        self.stalkcolorbr = stalkcolorbr
        self.veiltype = veiltype
        self.veilcolor = veilcolor
        self.ringnumber = ringnumber
        self.ringtype = ringtype
        self.sporeprintcolor = sporeprintcolor
        self.population = population
        self.habitat = habitat

    def __str__(self):
        return str(self.label) + " " + self.capshape + " " + self.capsurface +\
               " " + self.capcolor + " " + self.bruises + " " + self.odor +\
               " " + self.gillattachment + " " + self.gillspacing + " " +\
               self.gillsize + " " + self.gillcolor + " " + self.stalkshape +\
               " " + self.stalkroot + " " + self.stalksurfacear + " " +\
               self.stalksurfacebr + " " + self.stalkcolorar + " " +\
               self.stalkcolorbr + " " + self.veiltype + " " +\
               self.veilcolor + " " + self.ringnumber + " " + self.ringtype +\
               " " + self.sporeprintcolor + " " + self.population + " " +\
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
    for data in mushroom_datas:
        if data.gillattachment == 'n':
            print(str(data.label))

