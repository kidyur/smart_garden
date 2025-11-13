import sys
from PyQt5 import QtCore, QtWidgets
import requests
import bs4

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Нажмите, чтобы получить погоду в Москве на сегодня")
        self.button.setStyleSheet('font-size: 20px')
        self.text = QtWidgets.QLabel("?°",
                                     alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet('font-size: 72px')

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.getCurrentWeatherInMoscow)

    def getCurrentWeatherInMoscow(self):
        doc = bs4.BeautifulSoup(requests.get('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow').text, "html.parser")
        currentWeather = doc.find("i").text
        self.text.setText(currentWeather + "°")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())