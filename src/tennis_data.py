class TennisData:

    enum = """Outlook: Sunny=1, Overcast=2, Rain=3
Temperature: Hot=1, Mild=2, Cool=3
Humidity: High=1, Normal=2
Wind: Strong=1, Weak=2
PlayTennis: Yes=1, No=2"""

    outlook2str = { 1:"Sunny", 2:"Overcast", 3:"Rain"}
    temp2str = { 1:"Hot", 2:"Mild", 3:"Cool"}
    hum2str = { 1:"High", 2:"Normal"}
    wind2str = { 1:"Strong", 2:"Weak"}
    pt2str = { 0:"Yes", 1:"No"}

    def __init__(self, outlook, temp, humidity, wind, label):
        self.outlook = outlook
        self.temp = temp
        self.humidity = humidity
        self.wind = wind
        self.label = label

    def print_enum():
        print(Data.enum)

    def __str__(self):
        return TennisData.outlook2str[self.outlook] + ", " + TennisData.temp2str[self.temp] + ", " + TennisData.hum2str[self.humidity] + ", " + TennisData.wind2str[self.wind] + ", " + TennisData.pt2str[self.label]


def datas_tennis():
    datas = []
    datas.append(TennisData(1, 1, 1, 2, 1))
    datas.append(TennisData(1, 1, 1, 1, 1))
    datas.append(TennisData(2, 1, 1, 2, 0))
    datas.append(TennisData(3, 2, 1, 2, 0))
    datas.append(TennisData(3, 3, 2, 2, 0))
    datas.append(TennisData(3, 3, 2, 1, 1))
    datas.append(TennisData(2, 3, 2, 1, 0))
    datas.append(TennisData(1, 2, 1, 2, 1))
    datas.append(TennisData(1, 3, 2, 2, 0))
    datas.append(TennisData(3, 2, 2, 2, 0))
    datas.append(TennisData(1, 2, 2, 1, 0))
    datas.append(TennisData(2, 2, 1, 1, 0))
    datas.append(TennisData(2, 1, 2, 2, 0))
    datas.append(TennisData(3, 2, 1, 1, 1))
    return datas

if __name__ == "__main__":
    datas_tennis()
