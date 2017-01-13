class TennisData:

    enum = """Outlook: Sunny=1, Overcast=2, Rain=3
Temperature: Hot=1, Mild=2, Cool=3
Humidity: High=1, Normal=2
Wind: Strong=1, Weak=2
PlayTennis: Yes=1, No=2"""

    def __init__(self, outlook, temp, humidity, wind, label):
        self.outlook = outlook
        self.temp = temp
        self.humidity = humidity
        self.wind = wind
        self.label = label

    def print_enum():
        print(Data.enum)

    def __str__(self):
        return self.outlook + ", " + self.temp + ", " + self.humidity + ", " + self.wind + ", " + str(self.label)


def datas_tennis():
    datas = []
    datas.append(TennisData("Sunny", "Hot", "High", "Weak", 0))
    datas.append(TennisData("Sunny", "Hot", "High", "Strong", 0))
    datas.append(TennisData("Overcast", "Hot", "High", "Weak", 1))
    datas.append(TennisData("Rain", "Mild", "High", "Weak", 1))
    datas.append(TennisData("Rain", "Cool", "Normal", "Weak", 1))
    datas.append(TennisData("Rain", "Cool", "Normal", "Strong", 0))
    datas.append(TennisData("Overcast", "Cool", "Normal", "Strong", 1))
    datas.append(TennisData("Sunny", "Mild", "High", "Weak", 0))
    datas.append(TennisData("Sunny", "Cool", "Normal", "Weak", 1))
    datas.append(TennisData("Rain", "Mild", "Normal", "Weak", 1))
    datas.append(TennisData("Sunny", "Mild", "Normal", "Strong", 1))
    datas.append(TennisData("Overcast", "Mild", "High", "Strong", 1))
    datas.append(TennisData("Overcast", "Hot", "Normal", "Weak", 1))
    datas.append(TennisData("Rain", "Mild", "High", "Strong", 0))
    return datas

if __name__ == "__main__":
    datas_tennis()
