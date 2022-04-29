import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import names as nm
from functions import *
from  names import *
import time


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('사주팔자', self)
        self.lbl.move(30, 30)

        self.sex = 1
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

        # 라벨
        self.lsex = QLabel('성별 선택: ', self)
        self.lsex.move(30, 60)
        self.lyear = QLabel('생년 입력', self)
        self.lyear.move(30 ,90)
        self.lmonth = QLabel('생월 입력', self)
        self.lmonth.move(30 ,120)
        self.lday = QLabel('생일 입력', self)
        self.lday.move(30 ,150)
        self.lhour = QLabel('생시 입력', self)
        self.lhour.move(30 ,180)
        self.lmin = QLabel('생분 입력', self)
        self.lmin.move(30 ,210)


        # 입력부
        self.imale = QRadioButton('남자', self)
        self.ifemale = QRadioButton('여자', self)
        self.imale.move(120, 60)
        self.ifemale.move(200, 60)
        self.imale.setChecked(True)
        self.imale.clicked.connect(self.radioBtn)
        self.ifemale.clicked.connect(self.radioBtn)

        self.iyear = QLineEdit(self)
        self.iyear.move(100, 90)
        # self.iyear.textChanged[str].connect(self.btn)
        self.imonth = QLineEdit(self)
        self.imonth.move(100, 120)
        self.iday = QLineEdit(self)
        self.iday.move(100, 150)
        self.ihour = QLineEdit(self)
        self.ihour.move(100, 180)
        self.imin = QLineEdit(self)
        self.imin.move(100, 210)

        # 버튼
        self.button = QPushButton("조회", self)
        self.button.move(30, 300)
        self.button.clicked.connect(self.btn)

        # 사주 원국 출력
        self.out0 = QLabel(self)
        self.out0.move(50, 340)
        self.out0.setFont(QFont('Arial', 10))
        self.out0.setAlignment(Qt.AlignVCenter)
        self.out0.setFixedWidth(30)

        self.outS = QLabel(self)
        self.outS.move(100, 340)
        self.outS.setFont(QFont('Arial', 10, QFont.Bold))
        self.outS.setAlignment(Qt.AlignVCenter)
        self.outS.setFixedWidth(50)

        self.pivot = QLabel(self)
        self.pivot.move(100, 360)
        self.pivot.setFont(QFont('Arial', 20, QFont.Bold))
        self.pivot.setAlignment(Qt.AlignVCenter)
        self.pivot.setFixedWidth(300)
        self.pivot.setFixedHeight(75)

        self.out1 = QLabel(self)
        self.out1.move(300, 340)
        self.out1.setFont(QFont('Arial', 10))
        self.out1.setAlignment(Qt.AlignVCenter)
        self.out1.setFixedWidth(50)

        self.weather = QLabel(self)
        self.weather.move(300, 350)
        self.weather.setFont(QFont('Arial', 10, QFont.Bold))
        self.weather.setAlignment(Qt.AlignVCenter)
        self.weather.setFixedWidth(100)
        self.weather.setFixedHeight(75)

        self.out2 = QLabel(self)
        self.out2.move(460, 340)
        self.out2.setFont(QFont('Arial', 10))
        self.out2.setAlignment(Qt.AlignVCenter)
        self.out2.setFixedWidth(50)

        self.form = QLabel(self)
        self.form.move(460, 350)
        self.form.setFont(QFont('Arial', 10, QFont.Bold))
        self.form.setAlignment(Qt.AlignVCenter)
        self.form.setFixedWidth(200)
        self.form.setFixedHeight(75)

        self.outA = QLabel(self)
        self.outA.move(50, 440)
        self.outA.setFont(QFont('Arial', 10))
        self.outA.setAlignment(Qt.AlignVCenter)
        self.outA.setFixedWidth(30)

        self.luck1 = QLabel(self)
        self.luck1.move(100, 440)
        self.luck1.setFont(QFont('Arial', 10, QFont.Bold))
        self.luck1.setAlignment(Qt.AlignVCenter)
        self.luck1.setFixedWidth(800)
        self.luck1.setFixedHeight(100)

        self.outB = QLabel(self)
        self.outB.move(50, 540)
        self.outB.setFont(QFont('Arial', 10))
        self.outB.setAlignment(Qt.AlignVCenter)
        self.outB.setFixedWidth(30)

        self.luck2 = QLabel(self)
        self.luck2.move(100, 540)
        self.luck2.setFont(QFont('Arial', 10, QFont.Bold))
        self.luck2.setAlignment(Qt.AlignVCenter)
        self.luck2.setFixedWidth(800)
        self.luck2.setFixedHeight(100)


        self.setWindowTitle('四柱八字')
        self.setWindowIcon(QIcon('yy-01.png'))
        self.setGeometry(300, 300, 300, 200)
        self.move(400, 150)
        self.resize(800, 800)
        self.show()


    def radioBtn(self):
        if self.imale.isChecked():
            self.sex = 1
        if self.ifemale.isChecked():
            self.sex = 0

    def btn(self, text):
        this = int((time.localtime().tm_year)%100)
        year = int(self.iyear.text())
        month = int(self.imonth.text())
        day = int(self.iday.text())
        hour = int(self.ihour.text())
        min = int(self.imin.text())
        sex = str(Sex(self.sex).name) + '命'

        f = Destiny.fortune(year, month, day, hour, min)
        luck = Base.lucks(f=f, born_year= year, born_month= month, born_day= day, sex=self.sex)
        lunar = f[3]
        lord = f[4]
        element = Fives.stemfives(f[4])

        out_origin = ''
        for x in range(4):
            out_origin += str(Stem(int(f[6-(2*x)])).name) + '  '
        out_origin += '\n'
        for x in range(4):
            out_origin += str(Branch(int(f[7-(2*x)])).name) + '  '

        out_weather = str(Branch(lunar).name) + '월의 ' + str(Stem(lord).name) + str(Five(element).name)

        out_form = ''
        if len(Format.formula(f)[0]) != 0:
            for idx, x in enumerate(Format.formula(f)[0]):
                out_form += Deity(x).name + '를 용하는 ' + Deity(Format.formula(f)[1]).name + '격\n'
        else:
            out_form += Deity(Format.formula(f)[1]).name + '격'


        out_luck1 = ''
        for x in range(10):
            out_luck1 += str(luck[2][2*x]) + '\t'
        out_luck1 += '\n'
        for x in range(10):
            out_luck1 += str('%02d'%(luck[0][9-x][0])) + '\t'
        out_luck1 += '\n'
        for x in range(10):
            out_luck1 += str(Stem(luck[0][9-x][1]).name) + '\t'
        out_luck1 += '\n'
        for x in range(10):
            out_luck1 += str(Branch(luck[0][9-x][2]).name) + '\t'

        out_luck2 =''
        for x in range(10):
            out_luck2 += str(luck[3][(2*x)]) + '\t'
        out_luck2 += '\n'
        for x in range(10):
            out_luck2 += str('%02d'%(luck[1][9 - x][0])) + '\t'
        out_luck2 += '\n'
        for x in range(10):
            out_luck2 += str(Stem(luck[1][9 - x][1]).name) + '\t'
        out_luck2 += '\n'
        for x in range(10):
            out_luck2 += str(Branch(luck[1][9-x][2]).name) + '\t'


        self.out0.setText('元局')
        self.pivot.setText(out_origin)
        self.out1.setText('季節')
        self.weather.setText(out_weather)
        self.out2.setText('格用神')
        self.form.setText(out_form)
        self.outS.setText(sex)
        self.outA.setText('大運')
        self.luck1.setText(out_luck1)
        self.outB.setText('歲運')
        self.luck2.setText(out_luck2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())