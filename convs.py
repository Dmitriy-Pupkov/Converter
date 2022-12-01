import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from conv import Ui_MainWindow


class Conv(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.last_conv = None
        self.text_num1 = None
        self.fav_list = []
        self.setupUi(self)
        self.action_9.triggered.connect(self.add_favourites)
        self.action_11.triggered.connect(self.conv_base_mass)
        self.action_12.triggered.connect(self.conv_base_length)
        self.action_13.triggered.connect(self.conv_base_ed_v)
        self.action_14.triggered.connect(self.conv_base_s)
        self.action_15.triggered.connect(self.conv_base_speed)
        self.action_16.triggered.connect(self.conv_base_ed_temp)
        self.action_18.triggered.connect(self.conv_base_ed_time)
        self.action_23.triggered.connect(self.conv_ing_p)
        self.action_24.triggered.connect(self.conv_ing_fp)
        self.action_25.triggered.connect(self.conv_ing_f)
        self.action_26.triggered.connect(self.conv_ing_q)
        self.action_19.triggered.connect(self.conv_old_ed_length)
        self.action_22.triggered.connect(self.conv_old_ed_s)
        self.action_21.triggered.connect(self.conv_old_ed_v)
        self.action_32.triggered.connect(self.conv_sea_ed_length)
        self.action_33.triggered.connect(self.conv_sea_ed_speed)
        self.action_8.triggered.connect(self.conv_comp_v_dates)
        self.pushButton.clicked.connect(self.translate)

    def conv_base_mass(self):
        try:
            self.last_conv = 'conv_base_mass'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_mass''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_mass''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_length(self):
        try:
            self.last_conv = 'conv_base_ed_length'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_length''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_length''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_s(self):
        try:
            self.last_conv = 'conv_base_ed_S'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_S''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_S''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_speed(self):
        try:
            self.last_conv = 'conv_base_ed_speed'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_speed''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_speed''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_ed_temp(self):
        try:
            self.last_conv = 'conv_base_ed_temp'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_temp''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_temp''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_ed_time(self):
        try:
            self.last_conv = 'conv_base_ed_time'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_time''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_time''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_base_ed_v(self):
        try:
            self.last_conv = 'conv_base_ed_V'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_V''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_base_ed_V''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_ing_p(self):
        try:
            self.last_conv = 'conv_ing_p'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_p''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_p''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_ing_fp(self):
        try:
            self.last_conv = 'conv_ind_P'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ind_P''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ind_P''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_ing_f(self):
        try:
            self.last_conv = 'conv_ing_F'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_F''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_F''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_ing_q(self):
        try:
            self.last_conv = 'conv_ing_Q'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_Q''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_ing_Q''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_old_ed_length(self):
        try:
            self.last_conv = 'conv_old_ed_length'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_length''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_length''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_old_ed_s(self):
        try:
            self.last_conv = 'conv_old_ed_S'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_S''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_S''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_old_ed_v(self):
        try:
            self.last_conv = 'conv_old_ed_V'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_V''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_old_ed_V''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_sea_ed_length(self):
        try:
            self.last_conv = 'conv_sea_ed_length'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_sea_ed_length''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_sea_ed_length''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_sea_ed_speed(self):
        try:
            self.last_conv = 'conv_sea_ed_speed'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_sea_ed_speed''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_sea_ed_speed''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def conv_comp_v_dates(self):
        try:
            self.last_conv = 'conv_comp_V_dates'
            con = sqlite3.connect("calc_conv.sqlite")
            cur = con.cursor()
            self.comboBox_3.clear()
            self.comboBox_4.clear()
            self.comboBox_3.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_comp_V_dates''').fetchall()])
            self.comboBox_4.addItems(
                [item[0] for item in cur.execute('''SELECT name FROM conv_comp_V_dates''').fetchall()])
            self.fav_list.remove(None)
        except ValueError:
            pass

    def add_favourites(self):
        if self.last_conv not in self.fav_list:
            self.fav_list.append(self.last_conv)
            print(self.fav_list)
        con = sqlite3.connect("calc_conv.sqlite")
        cur = con.cursor()
        cur.execute('''INSERT INTO favourites (name) VALUES (?)''', [self.last_conv])
        con.commit()

    def favourites_convs(self):
        con = sqlite3.connect("calc_conv.sqlite")
        cur = con.cursor()
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        self.comboBox_3.addItems(
            [item[0] for item in cur.execute(f'''SELECT name FROM {self.last_conv}''').fetchall()])
        self.comboBox_4.addItems(
            [item[0] for item in cur.execute(f'''SELECT name FROM {self.last_conv}''').fetchall()])

    def translate(self):
        for i in range(self.comboBox_3.count()):
            if self.comboBox_3.currentText() == self.comboBox_4.currentText():
                self.number2.setText(self.number1.text())
            if self.comboBox_3.itemText(i) == 'Центиграмм':
                if (self.comboBox_3.currentText() == 'Килотонна') and (self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килотонна') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Килотонна') and (
                        self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Килотонна') and (
                        self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000000))
                elif (self.comboBox_3.currentText() == 'Килотонна') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000000))
                elif (self.comboBox_3.currentText() == 'Килотонна') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000000000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Тонна (т)') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Килограмм (кг)') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Грамм (г)') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 100000000000))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000000))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Центиграмм') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000000))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Миллиграмм (мг)') and (
                        self.comboBox_4.currentText() == 'Микрограмм (мкг)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Килотонна'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000000000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Тонна (т)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Килограмм (кг)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Грамм (г)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Центиграмм'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Микрограмм (мкг)') and (
                        self.comboBox_4.currentText() == 'Миллиграмм (мг)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
            elif self.comboBox_3.itemText(i) == 'Нанометр (нм)':
                if (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000000))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Дециметр (дм)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000000))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Миллиметр (мм)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Микрометр (микрон)') and (
                        self.comboBox_4.currentText() == 'Нанометр (нм)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Дециметр (дм)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Миллиметр (мм)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Нанометр (нм)') and (
                        self.comboBox_4.currentText() == 'Микрометр (микрон)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
            elif self.comboBox_3.itemText(i) == 'Квадратный миллиметр (мм²)':
                if (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Декар'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Ар (а)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000000000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Декар'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Ар (а)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000000000))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Ар (а)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000000))
                elif (self.comboBox_3.currentText() == 'Декар') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Декар'):
                    self.number2.setText(str(float(self.number1.text()) / 10))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Ар (а)') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Декар'):
                    self.number2.setText(str(float(self.number1.text()) / 1000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Ар (а)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дециметр (дм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) / 100000000))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) / 1000000))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Декар'):
                    self.number2.setText(str(float(self.number1.text()) / 100000))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Ар (а)'):
                    self.number2.setText(str(float(self.number1.text()) / 10000))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) / 100))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Квадратный дециметр (дм²)') and (
                        self.comboBox_4.currentText() == 'Квадратный миллиметр (мм²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
            elif self.comboBox_3.itemText(i) == 'Километр в минуту':
                if (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Километр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01667))
                elif (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Километр в секунду (км/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0002778))
                elif (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Метр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 16.67))
                elif (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.2778))
                elif (self.comboBox_3.currentText() == 'Километр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
                elif (self.comboBox_3.currentText() == 'Километр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
                elif (self.comboBox_3.currentText() == 'Километр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в секунду (км/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01667))
                elif (self.comboBox_3.currentText() == 'Километр в минуту') and (
                        self.comboBox_4.currentText() == 'Метр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Километр в минуту') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 16.67))
                elif (self.comboBox_3.currentText() == 'Километр в секунду (км/с)') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 3600))
                elif (self.comboBox_3.currentText() == 'Километр в секунду (км/с)') and (
                        self.comboBox_4.currentText() == 'Километр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
                elif (self.comboBox_3.currentText() == 'Километр в секунду (км/с)') and (
                        self.comboBox_4.currentText() == 'Метр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 60000))
                elif (self.comboBox_3.currentText() == 'Километр в секунду (км/с)') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Метр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.06))
                elif (self.comboBox_3.currentText() == 'Метр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Метр в минуту') and (
                        self.comboBox_4.currentText() == 'Километр в секунду (км/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001667))
                elif (self.comboBox_3.currentText() == 'Метр в минуту') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01667))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 3.6))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Километр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 0.06))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Километр в секунду (км/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Метр в минуту'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
            elif self.comboBox_3.itemText(i) == 'Градус Фаренгейта (°F)':
                if (self.comboBox_3.currentText() == 'Градус Цельсия (°C)') and (
                        self.comboBox_4.currentText() == 'Градус Фаренгейта (°F)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.8 + 32))
                elif (self.comboBox_3.currentText() == 'Градус Цельсия (°C)') and (
                        self.comboBox_4.currentText() == 'Кельвин (K)'):
                    self.number2.setText(str(float(self.number1.text()) + 273.15))
                elif (self.comboBox_3.currentText() == 'Градус Фаренгейта (°F)') and (
                        self.comboBox_4.currentText() == 'Градус Цельсия (°C)'):
                    self.number2.setText(str((float(self.number1.text()) - 32) / 1.8))
                elif (self.comboBox_3.currentText() == 'Градус Фаренгейта (°F)') and (
                        self.comboBox_4.currentText() == 'Кельвин (K)'):
                    self.number2.setText(str((float(self.number1.text()) - 32) / 1.8 + 273.15))
                elif (self.comboBox_3.currentText() == 'Кельвин (K)') and (
                        self.comboBox_4.currentText() == 'Градус Цельсия (°C)'):
                    self.number2.setText(str(float(self.number1.text()) - 273.15))
                elif (self.comboBox_3.currentText() == 'Кельвин (K)') and (
                        self.comboBox_4.currentText() == 'Градус Фаренгейта (°F)'):
                    self.number2.setText(str((float(self.number1.text()) - 273.15) * 1.8 + 32))
            elif self.comboBox_3.itemText(i) == 'Сутки':
                if (self.comboBox_3.currentText() == 'Сутки') and (
                        self.comboBox_4.currentText() == 'Часы'):
                    self.number2.setText(str(float(self.number1.text()) * 24))
                elif (self.comboBox_3.currentText() == 'Сутки') and (
                        self.comboBox_4.currentText() == 'Минуты (мин)'):
                    self.number2.setText(str(float(self.number1.text()) * 1440))
                elif (self.comboBox_3.currentText() == 'Сутки') and (
                        self.comboBox_4.currentText() == 'Секунды (с)'):
                    self.number2.setText(str(float(self.number1.text()) * 86400))
                elif (self.comboBox_3.currentText() == 'Сутки') and (
                        self.comboBox_4.currentText() == 'Миллисекунды (ms)'):
                    self.number2.setText(str(float(self.number1.text()) * 86400000))
                elif (self.comboBox_3.currentText() == 'Сутки') and (
                        self.comboBox_4.currentText() == 'Наносекунда (ns)'):
                    self.number2.setText(str(float(self.number1.text()) * 86400000000000))
                elif (self.comboBox_3.currentText() == 'Часы') and (
                        self.comboBox_4.currentText() == 'Сутки'):
                    self.number2.setText(str(float(self.number1.text()) * 0.04167))
                elif (self.comboBox_3.currentText() == 'Часы') and (
                        self.comboBox_4.currentText() == 'Минуты (мин)'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
                elif (self.comboBox_3.currentText() == 'Часы') and (
                        self.comboBox_4.currentText() == 'Секунды (с)'):
                    self.number2.setText(str(float(self.number1.text()) * 3600))
                elif (self.comboBox_3.currentText() == 'Часы') and (
                        self.comboBox_4.currentText() == 'Миллисекунды (ms)'):
                    self.number2.setText(str(float(self.number1.text()) * 3600000))
                elif (self.comboBox_3.currentText() == 'Часы') and (
                        self.comboBox_4.currentText() == 'Наносекунда (ns)'):
                    self.number2.setText(str(float(self.number1.text()) * 3600000000000))
                elif (self.comboBox_3.currentText() == 'Минуты (мин)') and (
                        self.comboBox_4.currentText() == 'Сутки'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0006944))
                elif (self.comboBox_3.currentText() == 'Минуты (мин)') and (
                        self.comboBox_4.currentText() == 'Часы'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01667))
                elif (self.comboBox_3.currentText() == 'Минуты (мин)') and (
                        self.comboBox_4.currentText() == 'Секунды (с)'):
                    self.number2.setText(str(float(self.number1.text()) * 60))
                elif (self.comboBox_3.currentText() == 'Минуты (мин)') and (
                        self.comboBox_4.currentText() == 'Миллисекунды (ms)'):
                    self.number2.setText(str(float(self.number1.text()) * 60000))
                elif (self.comboBox_3.currentText() == 'Минуты (мин)') and (
                        self.comboBox_4.currentText() == 'Наносекунда (ns)'):
                    self.number2.setText(str(float(self.number1.text()) * 60000000000))
                elif (self.comboBox_3.currentText() == 'Секунды (с)') and (
                        self.comboBox_4.currentText() == 'Сутки'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001157))
                elif (self.comboBox_3.currentText() == 'Секунды (с)') and (
                        self.comboBox_4.currentText() == 'Часы'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0002778))
                elif (self.comboBox_3.currentText() == 'Секунды (с)') and (
                        self.comboBox_4.currentText() == 'Минуты (мин)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01667))
                elif (self.comboBox_3.currentText() == 'Секунды (с)') and (
                        self.comboBox_4.currentText() == 'Миллисекунды (ms)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Секунды (с)') and (
                        self.comboBox_4.currentText() == 'Наносекунда (ns)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Миллисекунды (ms)') and (
                        self.comboBox_4.currentText() == 'Сутки'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000001157))
                elif (self.comboBox_3.currentText() == 'Миллисекунды (ms)') and (
                        self.comboBox_4.currentText() == 'Часы'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000002778))
                elif (self.comboBox_3.currentText() == 'Миллисекунды (ms)') and (
                        self.comboBox_4.currentText() == 'Минуты (мин)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001667))
                elif (self.comboBox_3.currentText() == 'Миллисекунды (ms)') and (
                        self.comboBox_4.currentText() == 'Секунды (с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Миллисекунды (ms)') and (
                        self.comboBox_4.currentText() == 'Наносекунда (ns)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Наносекунда (ns)') and (
                        self.comboBox_4.currentText() == 'Сутки'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000000000001157))
                elif (self.comboBox_3.currentText() == 'Наносекунда (ns)') and (
                        self.comboBox_4.currentText() == 'Часы'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000002778))
                elif (self.comboBox_3.currentText() == 'Наносекунда (ns)') and (
                        self.comboBox_4.currentText() == 'Минуты (мин)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000000001667))
                elif (self.comboBox_3.currentText() == 'Наносекунда (ns)') and (
                        self.comboBox_4.currentText() == 'Секунды (с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000001))
                elif (self.comboBox_3.currentText() == 'Наносекунда (ns)') and (
                        self.comboBox_4.currentText() == 'Миллисекунды (ms)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
            elif self.comboBox_3.itemText(i) == 'Гектолитр (hl)':
                if (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Кубический дециметр (дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Гектолитр (hl)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Декалитр'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Кубический дециметр (дм³)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Кубический дециметр (дм³)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Кубический дециметр (дм³)') and (
                        self.comboBox_4.currentText() == 'Гектолитр (hl)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Кубический дециметр (дм³)') and (
                        self.comboBox_4.currentText() == 'Декалитр'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Кубический дециметр (дм³)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Кубический дециметр (дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Гектолитр (hl)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Декалитр'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Гектолитр (hl)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Гектолитр (hl)') and (
                        self.comboBox_4.currentText() == 'Кубический дециметр (дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Гектолитр (hl)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Гектолитр (hl)') and (
                        self.comboBox_4.currentText() == 'Декалитр'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Гектолитр (hl)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Декалитр') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Декалитр') and (
                        self.comboBox_4.currentText() == 'Кубический дециметр (дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Декалитр') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Декалитр') and (
                        self.comboBox_4.currentText() == 'Гектолитр (hl)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Декалитр') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Кубический дециметр (дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Гектолитр (hl)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Декалитр'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
            elif self.comboBox_3.itemText(i) == 'Мегапаскаль (МПа)':
                if (self.comboBox_3.currentText() == 'Килопаскаль (кПа)') and (
                        self.comboBox_4.currentText() == 'Мегапаскаль (МПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Килопаскаль (кПа)') and (
                        self.comboBox_4.currentText() == 'Паскаль (Па)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килопаскаль (кПа)') and (
                        self.comboBox_4.currentText() == 'Гектопаскаль (гПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Килопаскаль (кПа)') and (
                        self.comboBox_4.currentText() == 'Бар'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Килопаскаль (кПа)') and (
                        self.comboBox_4.currentText() == 'Миллибар'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Мегапаскаль (МПа)') and (
                        self.comboBox_4.currentText() == 'Килопаскаль (кПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Мегапаскаль (МПа)') and (
                        self.comboBox_4.currentText() == 'Паскаль (Па)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Мегапаскаль (МПа)') and (
                        self.comboBox_4.currentText() == 'Гектопаскаль (гПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Мегапаскаль (МПа)') and (
                        self.comboBox_4.currentText() == 'Бар'):
                    self.number2.setText(str(float(self.number1.text()) * 10))
                elif (self.comboBox_3.currentText() == 'Мегапаскаль (МПа)') and (
                        self.comboBox_4.currentText() == 'Миллибар'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Паскаль (Па)') and (
                        self.comboBox_4.currentText() == 'Килопаскаль (кПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Паскаль (Па)') and (
                        self.comboBox_4.currentText() == 'Мегапаскаль (МПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Паскаль (Па)') and (
                        self.comboBox_4.currentText() == 'Гектопаскаль (гПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Паскаль (Па)') and (
                        self.comboBox_4.currentText() == 'Бар'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001))
                elif (self.comboBox_3.currentText() == 'Паскаль (Па)') and (
                        self.comboBox_4.currentText() == 'Миллибар'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Гектопаскаль (гПа)') and (
                        self.comboBox_4.currentText() == 'Килопаскаль (кПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Гектопаскаль (гПа)') and (
                        self.comboBox_4.currentText() == 'Мегапаскаль (МПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001))
                elif (self.comboBox_3.currentText() == 'Гектопаскаль (гПа)') and (
                        self.comboBox_4.currentText() == 'Паскаль (Па)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Гектопаскаль (гПа)') and (
                        self.comboBox_4.currentText() == 'Бар'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Гектопаскаль (гПа)') and (
                        self.comboBox_4.currentText() == 'Миллибар'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Бар') and (
                        self.comboBox_4.currentText() == 'Килопаскаль (кПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Бар') and (
                        self.comboBox_4.currentText() == 'Мегапаскаль (МПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Бар') and (
                        self.comboBox_4.currentText() == 'Гектопаскаль (гПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Бар') and (
                        self.comboBox_4.currentText() == 'Паскаль (Па)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Бар') and (
                        self.comboBox_4.currentText() == 'Миллибар'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Миллибар') and (
                        self.comboBox_4.currentText() == 'Килопаскаль (кПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1))
                elif (self.comboBox_3.currentText() == 'Миллибар') and (
                        self.comboBox_4.currentText() == 'Мегапаскаль (МПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001))
                elif (self.comboBox_3.currentText() == 'Миллибар') and (
                        self.comboBox_4.currentText() == 'Паскаль (Па)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Миллибар') and (
                        self.comboBox_4.currentText() == 'Гектопаскаль (гПа)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Миллибар') and (
                        self.comboBox_4.currentText() == 'Бар'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
            elif self.comboBox_3.itemText(i) == 'Меганьютон (МН)':
                if (self.comboBox_3.currentText() == 'Меганьютон (МН)') and (
                        self.comboBox_4.currentText() == 'Килоньютон (кН)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Меганьютон (МН)') and (
                        self.comboBox_4.currentText() == 'Ньютон (Н)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Меганьютон (МН)') and (
                        self.comboBox_4.currentText() == 'Миллиньютон (мН)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000000))
                elif (self.comboBox_3.currentText() == 'Килоньютон (кН)') and (
                        self.comboBox_4.currentText() == 'Меганьютон (МН)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Килоньютон (кН)') and (
                        self.comboBox_4.currentText() == 'Ньютон (Н)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килоньютон (кН)') and (
                        self.comboBox_4.currentText() == 'Миллиньютон (мН)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Ньютон (Н)') and (
                        self.comboBox_4.currentText() == 'Меганьютон (МН)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Ньютон (Н)') and (
                        self.comboBox_4.currentText() == 'Килоньютон (кН)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Ньютон (Н)') and (
                        self.comboBox_4.currentText() == 'Миллиньютон (мН)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Миллиньютон (мН)') and (
                        self.comboBox_4.currentText() == 'Меганьютон (МН)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000001))
                elif (self.comboBox_3.currentText() == 'Миллиньютон (мН)') and (
                        self.comboBox_4.currentText() == 'Килоньютон (кН)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Миллиньютон (мН)') and (
                        self.comboBox_4.currentText() == 'Ньютон (Н)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
            elif self.comboBox_3.itemText(i) == 'Килограмм на кубометр (кг/м³)':
                if (self.comboBox_3.currentText() == 'Килограмм на кубометр (кг/м³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубометр (г/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килограмм на кубометр (кг/м³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубический дециметр (кг/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Килограмм на кубометр (кг/м³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубический дециметр (г/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Грамм на кубометр (г/м³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубометр (кг/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Грамм на кубометр (г/м³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубический дециметр (кг/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Грамм на кубометр (г/м³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубический дециметр (г/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Килограмм на кубический дециметр (кг/дм³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубометр (кг/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килограмм на кубический дециметр (кг/дм³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубометр (г/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Килограмм на кубический дециметр (кг/дм³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубический дециметр (г/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Грамм на кубический дециметр (г/дм³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубометр (кг/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Грамм на кубический дециметр (г/дм³)') and (
                        self.comboBox_4.currentText() == 'Грамм на кубометр (г/м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Грамм на кубический дециметр (г/дм³)') and (
                        self.comboBox_4.currentText() == 'Килограмм на кубический дециметр (кг/дм³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
            elif self.comboBox_3.itemText(i) == 'Джоуль (дж)':
                if (self.comboBox_3.currentText() == 'Джоуль (дж)') and (
                        self.comboBox_4.currentText() == 'Килоджоуль (кдж)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Джоуль (дж)') and (
                        self.comboBox_4.currentText() == 'Мегаджоуль (Мдж)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Килоджоуль (кдж)') and (
                        self.comboBox_4.currentText() == 'Джоуль (дж)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килоджоуль (кдж)') and (
                        self.comboBox_4.currentText() == 'Джоуль (дж)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Килоджоуль (кдж)') and (
                        self.comboBox_4.currentText() == 'Мегаджоуль (Мдж)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Мегаджоуль (Мдж)') and (
                        self.comboBox_4.currentText() == 'Джоуль (дж)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Мегаджоуль (Мдж)') and (
                        self.comboBox_4.currentText() == 'Килоджоуль (кдж)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
            elif self.comboBox_3.itemText(i) == 'Пядь':
                if (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001667))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.08333))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 4))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1778))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 17.78))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.5833))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001105))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 0.25))
                elif (self.comboBox_3.currentText() == 'Пядь') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001778))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 6000))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 500))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 24000))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 1067))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 106680))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 3500))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.6629))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 1500))
                elif (self.comboBox_3.currentText() == 'Верста') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.067))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 12))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.002))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 48))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 2.134))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 213.4))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 7))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001326))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 3))
                elif (self.comboBox_3.currentText() == 'Сажень') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.002134))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 0.25))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00004167))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.02083))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.04445))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 4.445))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1458))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0625))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00002762))
                elif (self.comboBox_3.currentText() == 'Вершок') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00004445))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 5.624))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009374))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.4687))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 22.5))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 3.281))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0006214))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 1.406))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 0.05624))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000009374))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.004687))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 0.225))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.03281))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000006214))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01406))
                elif (self.comboBox_3.currentText() == 'Сантиметр (см)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00001))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 1.714))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0002857))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1429))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 6.857))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.3048))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 30.48))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001894))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 0.4286))
                elif (self.comboBox_3.currentText() == 'Фут (ft)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0003048))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 9051))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 1.509))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 754.3))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 36206))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 1609))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 160934))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 5280))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 2263))
                elif (self.comboBox_3.currentText() == 'Миля (mi)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.609))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 4))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0006667))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 0.3333))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 16))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.7112))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 71.12))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 2.333))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0004419))
                elif (self.comboBox_3.currentText() == 'Аршин') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0007112))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Пядь'):
                    self.number2.setText(str(float(self.number1.text()) * 5624))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.9374))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Сажень'):
                    self.number2.setText(str(float(self.number1.text()) * 468.7))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Вершок'):
                    self.number2.setText(str(float(self.number1.text()) * 22497))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Сантиметр (см)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Фут (ft)'):
                    self.number2.setText(str(float(self.number1.text()) * 3281))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Миля (mi)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.6214))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Аршин'):
                    self.number2.setText(str(float(self.number1.text()) * 1406))
            elif self.comboBox_3.itemText(i) == 'Квадратная миля':
                if (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 27878400))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 2.276))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 259))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 2589988))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 25899881006))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 2.59))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 3097600))
                elif (self.comboBox_3.currentText() == 'Квадратная миля') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 4014489600))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000003587))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000008163))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000929))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0929))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 929))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000929))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1111))
                elif (self.comboBox_3.currentText() == 'Квадратный фут (ft²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 144))
                elif (self.comboBox_3.currentText() == 'Квадратная верста') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1138062))
                elif (self.comboBox_3.currentText() == 'Квадратная верста') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 11380621942))
                elif (self.comboBox_3.currentText() == 'Квадратная верста') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.138))
                elif (self.comboBox_3.currentText() == 'Квадратная верста') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1361111))
                elif (self.comboBox_3.currentText() == 'Квадратная верста') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1763999950))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.003861))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 107639))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.008787))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 100000000))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.01))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 11960))
                elif (self.comboBox_3.currentText() == 'Гектар (га)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 15500031))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000003861))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10.76))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000008787))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.196))
                elif (self.comboBox_3.currentText() == 'Квадратный метр (м²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1550))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000000003861))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001076))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000000008787))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000001))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000001))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001196))
                elif (self.comboBox_3.currentText() == 'Квадратный сантиметр (см²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.155))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.3861))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10763910))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.8787))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 100))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 10000000000))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1195990))
                elif (self.comboBox_3.currentText() == 'Квадратный километр (км²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1550003100))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000003228))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 9))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000007347))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00008361))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.8361))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 8361))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000008361))
                elif (self.comboBox_3.currentText() == 'Квадратный ярд (yd²)') and (
                        self.comboBox_4.currentText() == 'Квадратный дюйм (in²)'):
                    self.number2.setText(str(float(self.number1.text()) * 1296))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратная миля'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000002491))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратный фут (ft²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.006944))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратная верста'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000005669))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Гектар (га)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000006452))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратный метр (м²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0006452))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратный сантиметр (см²)'):
                    self.number2.setText(str(float(self.number1.text()) * 6.452))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратный километр (км²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000006452))
                elif (self.comboBox_3.currentText() == 'Квадратный дюйм (in²)') and (
                        self.comboBox_4.currentText() == 'Квадратный ярд (yd²)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0007716))
            elif self.comboBox_3.itemText(i) == 'Галлон (жидкости) (gal)':
                if (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.02381))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.003785))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 3785))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 3785))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 3.785))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 3.785))
                elif (self.comboBox_3.currentText() == 'Галлон (жидкости) (gal)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 3785))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000186))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00002957))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 29.57))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.02957))
                elif (self.comboBox_3.currentText() == 'Жидкая унция (oz)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 29.57))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 42))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 5376))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.159))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 158987))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 159))
                elif (self.comboBox_3.currentText() == 'Баррель (жидкости)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 158987))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 1264.2))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 33814))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 6.29))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Кубический метр (м³)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000000))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0002642))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.03381))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000629))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Кубический сантиметр (см³)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.2642))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 33.81))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00629))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Литр (л)') and (
                        self.comboBox_4.currentText() == 'Миллилитр (мл)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Галлон (жидкости) (gal)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0002642))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Жидкая унция (oz)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.03381))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Баррель (жидкости)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.00000629))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Кубический метр (м³)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000001))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Кубический сантиметр (см³)'):
                    self.number2.setText(str(float(self.number1.text()) * 1))
                elif (self.comboBox_3.currentText() == 'Миллилитр (мл)') and (
                        self.comboBox_4.currentText() == 'Литр (л)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
            elif self.comboBox_3.itemText(i) == 'Кабельт':
                if (self.comboBox_3.currentText() == 'Кабельт') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.1852))
                elif (self.comboBox_3.currentText() == 'Кабельт') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 185.2))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Кабельт'):
                    self.number2.setText(str(float(self.number1.text()) * 5.399568034557236))
                elif (self.comboBox_3.currentText() == 'Километр (км)') and (
                        self.comboBox_4.currentText() == 'Метр (м)'):
                    self.number2.setText(str(float(self.number1.text()) * 1000))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Кабельт'):
                    self.number2.setText(str(float(self.number1.text()) * 0.005399568034557236))
                elif (self.comboBox_3.currentText() == 'Метр (м)') and (
                        self.comboBox_4.currentText() == 'Километр (км)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.001))
            elif self.comboBox_3.itemText(i) == 'Узел':
                if (self.comboBox_3.currentText() == 'Узел') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 1.852))
                elif (self.comboBox_3.currentText() == 'Узел') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.5144))
                elif (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Узел'):
                    self.number2.setText(str(float(self.number1.text()) * 0.54))
                elif (self.comboBox_3.currentText() == 'Километр в час (км/ч)') and (
                        self.comboBox_4.currentText() == 'Метр в секунду (м/с)'):
                    self.number2.setText(str(float(self.number1.text()) * 0.2778))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Узел'):
                    self.number2.setText(str(float(self.number1.text()) * 1.944))
                elif (self.comboBox_3.currentText() == 'Метр в секунду (м/с)') and (
                        self.comboBox_4.currentText() == 'Километр в час (км/ч)'):
                    self.number2.setText(str(float(self.number1.text()) * 3.6))
            elif self.comboBox_3.itemText(i) == 'Мегабит [мебибит] (Mbit [Mibit])':
                if (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * (1.1529215 * 10 ** 18)))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 131072))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 134217730))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 137438950000))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 140737490000000))
                elif (self.comboBox_3.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * (1.4411519 * 10 ** 17)))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 131072))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 134217730))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 137438950000))
                elif (self.comboBox_3.currentText() == 'Петабит [пебибит] (Pbit [Pibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 140737490000000))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000001192))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 131072))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 134217730))
                elif (self.comboBox_3.currentText() == 'Терабит [тебибит] (Tbit [Tibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 137438950000))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000001164))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000001192))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 131072))
                elif (self.comboBox_3.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 134217730))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000001137))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000001164))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000001192))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 131072))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8.882 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1.11 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000001137))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000001164))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000001192))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Килобит [кибибит] (Kbit [Kibit])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 128))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 1.084 * 10 ** -19))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8.882 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1.084 * 10 ** -19))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1.11 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000001137))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000001164))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000001192))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0001221))
                elif (self.comboBox_3.currentText() == 'Бит') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 0.125))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8796092845927))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 9007199454524002))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 9.22337180278734 * 10 ** 18))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1.1529215 * 10 ** 18))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8796092845927))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 9007199454524002))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8796092845927))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000007451))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 9007199454524002))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 9.22337180278734 * 10 ** 18))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1.1529215 * 10 ** 18))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8796092845927))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 9007199454524002))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Петабайт [пебибайт] (Pb [PiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1125899900000000))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8796092845927))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Терабайт [тебибайт] (Tb [TiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1099511600000))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000007451))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8589934727))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1073741800))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000000007276))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000007451))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8388608))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1048576))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000000000007105))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000000007276))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000007451))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8192))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 8.882 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))
                elif (self.comboBox_3.currentText() == 'Килобайт [кибибайт] (Kb [KiB])') and (
                        self.comboBox_4.currentText() == 'Байт'):
                    self.number2.setText(str(float(self.number1.text()) * 1024))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Эксабит [эксбибит] (Ebit [Eibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 6.939 * 10 ** -18))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Петабит [пебибит] (Pbit [Pibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000000000007105))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Терабит [тебибит] (Tbit [Tibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000000007276))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Гигабит [гибибит] (Gbit [Gibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000000007451))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Мегабит [мебибит] (Mbit [Mibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.000007629))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Килобит [кибибит] (Kbit [Kibit])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.007813))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Бит'):
                    self.number2.setText(str(float(self.number1.text()) * 8))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Эксабайт [эксбибайт] (Eb [EiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 8.674 * 10 ** -19))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Петабайт [пебибайт] (Pb [PiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 8.882 * 10 ** -16))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Терабайт [тебибайт] (Tb [TiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000000009095))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Гигабайт [гибибайт] (Gb [GiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000000009313))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Мегабайт [мебибайт] (Mb [MiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0000009537))
                elif (self.comboBox_3.currentText() == 'Байт') and (
                        self.comboBox_4.currentText() == 'Килобайт [кибибайт] (Kb [KiB])'):
                    self.number2.setText(str(float(self.number1.text()) * 0.0009766))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Conv()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
