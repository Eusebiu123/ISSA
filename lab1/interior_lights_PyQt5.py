from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import time
import threading

is_sweep = False
progress = 0
flag = False
number = 0
valoare = 0
avarii = False
flag_avarii = False
flag_stanga = False
flag_dreapta = False


############################### EXERCISE 2 ################################
class MyThread_sweep(QThread):
    sweepLedsSignal = pyqtSignal(int)

    def run(self):
        global is_sweep

        if not is_sweep:
            count = 0
            is_sweep = True
            while is_sweep:
                print("CLASS: emit count: " + str(count))
                self.sweepLedsSignal.emit(count)
                count += 1
                if count == 5:
                    count = 0
                time.sleep(1)
        else:
            is_sweep = False
            self.sweepLedsSignal.emit(0)


############################### EXERCISE 6 #################################
class MyThread_warning(QThread):
    warningLightsSignal = pyqtSignal(int)

    def run(self):
        global flag_avarii
        if not flag_avarii:
            count = 0
            flag_avarii = True
            while flag_avarii:
                print("CLASS: emit count: " + str(count))
                self.warningLightsSignal.emit(count)
                count = count + 1
                if count == 2:
                    count = 0
                time.sleep(0.5)
        else:
            flag_avarii = False
            self.warningLightsSignal.emit(0)


############################### EXERCISE 7 #################################
class MyThread_left(QThread):
    leftLightsSignal = pyqtSignal(int)

    def run(self):
        global flag_stanga
        if not flag_stanga:
            count = 0
            flag_stanga = True
            while flag_stanga:
                print("CLASS: emit count: " + str(count))
                self.leftLightsSignal.emit(count)
                count = count + 1
                if count == 2:
                    count = 0
                time.sleep(0.5)
        else:
            flag_stanga = False
            self.leftLightsSignal.emit(0)


############################### EXERCISE 8 #################################
class MyThread_right(QThread):
    rightLightsSignal = pyqtSignal(int)

    def run(self):
        global flag_dreapta
        if not flag_dreapta:
            count = 0
            flag_dreapta = True
            while flag_dreapta:
                print("CLASS: emit count: " + str(count))
                self.rightLightsSignal.emit(count)
                count = count + 1
                if count == 3:
                    count = 0
                time.sleep(0.5)
        else:
            flag_dreapta = False
            self.rightLightsSignal.emit(0)


############################### EXERCISE 10 ################################
class MyThread_unlockCar(QThread):
    unlockCarSignal = pyqtSignal(int)

    def run(self):
        pass
        ''' complete with necesarry code '''


############################### EXERCISE 11 ################################
class MyThread_lockCar(QThread):
    lockCarSignal = pyqtSignal(int)

    def run(self):
        pass
        ''' complete with necesarry code '''


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 500)
        MainWindow.setWindowTitle("Laborayoty 1 - Interior Lights")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        # Set background application color
        self.centralwidget.setStyleSheet("background-color: white;")

        # Continental image
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 350, 350, 120))
        pixmap = QPixmap("conti.png")
        pixmap = pixmap.scaled(350, 120, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

        # Car image
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(300, 170, 331, 161))
        pixmap1 = QPixmap("car.jpg")
        pixmap1 = pixmap1.scaled(331, 161, QtCore.Qt.KeepAspectRatio)
        self.label_1.setPixmap(pixmap1)

        # Left door button
        self.left_door = QtWidgets.QPushButton(MainWindow)
        self.left_door.setText("Left Door")
        self.left_door.setStyleSheet("font: bold;")
        self.left_door.setGeometry(QtCore.QRect(380, 50, 211, 41))
        self.left_door.clicked.connect(self.open_door_left)

        # Left door slider
        self.left_door_slider = QtWidgets.QSlider(self.centralwidget)
        self.left_door_slider.setGeometry(QtCore.QRect(410, 100, 160, 26))
        self.left_door_slider.setOrientation(QtCore.Qt.Horizontal)
        self.left_door_slider.setRange(0, 100)
        self.left_door_slider.setValue(0)
        self.left_door_slider.valueChanged.connect(self.valuechange_left_slider)

        # Left door spinbox
        self.spinBox_left = QtWidgets.QSpinBox(MainWindow)
        self.spinBox_left.setGeometry(QtCore.QRect(300, 50, 75, 41))
        self.spinBox_left.setKeyboardTracking(False)
        self.spinBox_left.setRange(0, 100)
        self.spinBox_left.valueChanged.connect(self.valuechange)

        # Right door
        self.right_door = QtWidgets.QPushButton(MainWindow)
        self.right_door.setText("Right door")
        self.right_door.setStyleSheet("font: bold;")
        self.right_door.setGeometry(QtCore.QRect(380, 400, 211, 41))
        self.right_door.clicked.connect(self.open_door_right)

        # Right door slider
        self.right_door_slider = QtWidgets.QSlider(self.centralwidget)
        self.right_door_slider.setGeometry(QtCore.QRect(410, 360, 160, 26))
        self.right_door_slider.setOrientation(QtCore.Qt.Horizontal)
        self.right_door_slider.setRange(0, 100)
        self.right_door_slider.setValue(0)
        self.right_door_slider.valueChanged.connect(self.valuechange_right_slider)

        # Right door spinbox
        self.spinBox_right = QtWidgets.QSpinBox(MainWindow)
        self.spinBox_right.setGeometry(QtCore.QRect(300, 400, 75, 41))
        self.spinBox_right.setKeyboardTracking(False)
        self.spinBox_right.setRange(0, 100)
        self.spinBox_right.valueChanged.connect(self.valuechange)

        # Current kl label
        self.current_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.current_kl_label.setGeometry(QtCore.QRect(685, 80, 151, 31))
        self.current_kl_label.setStyleSheet("font: bold;")
        self.current_kl_label.setText("Current KL: no_KL")

        # Previous kl button
        self.prev_kl = QtWidgets.QPushButton(MainWindow)
        self.prev_kl.setText("Previous KL")
        self.prev_kl.setStyleSheet("font: bold;")
        self.prev_kl.setGeometry(QtCore.QRect(680, 40, 101, 31))
        self.prev_kl.clicked.connect(self.prev_kl_function)
        self.prev_kl.setEnabled(False)

        # Prev kl label
        self.prev_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.prev_kl_label.setGeometry(QtCore.QRect(790, 40, 92, 31))
        self.prev_kl_label.setStyleSheet("font: bold;")

        # Next kl button
        self.next_kl = QtWidgets.QPushButton(MainWindow)
        self.next_kl.setText("Next KL")
        self.next_kl.setStyleSheet("font: bold;")
        self.next_kl.setGeometry(QtCore.QRect(680, 120, 101, 31))
        self.next_kl.clicked.connect(self.next_kl_function)

        # Next kl label
        self.next_kl_label = QtWidgets.QLabel(self.centralwidget)
        self.next_kl_label.setGeometry(QtCore.QRect(790, 120, 81, 31))
        self.next_kl_label.setStyleSheet("font: bold;")
        self.next_kl_label.setText("KL_s")

        # green led for interior lights
        self.interiorLightsLabel = QtWidgets.QLabel(self.centralwidget)
        self.interiorLightsLabel.setGeometry(QtCore.QRect(220, 160, 20, 20))

        # inside carLight Button
        self.carLight1 = QtWidgets.QPushButton(MainWindow)
        self.carLight1.setText("Car Light")
        self.carLight1.setStyleSheet("font: bold;")
        self.carLight1.setGeometry(QtCore.QRect(680, 280, 120, 30))
        self.carLight1.clicked.connect(self.carLightSet)

        # inside carLight
        self.carLight = QtWidgets.QLabel(self.centralwidget)
        self.carLight.setGeometry(QtCore.QRect(450, 240, 20, 20))

        # warning Lights Button
        self.warning = QtWidgets.QPushButton(MainWindow)
        self.warning.setText("Warning Lights")
        self.warning.setStyleSheet("font: bold;")
        self.warning.setGeometry(QtCore.QRect(50, 100, 160, 41))
        self.warning.clicked.connect(self.warningLightsButton)

        # left signaling Button
        self.warningLeft = QtWidgets.QPushButton(MainWindow)
        self.warningLeft.setText("Left Signaling")
        self.warningLeft.setStyleSheet("font:bold;")
        self.warningLeft.setGeometry(QtCore.QRect(680, 370, 120, 30))
        self.warningLeft.clicked.connect(self.leftSignaling)

        # right signaling Button
        self.warningRight = QtWidgets.QPushButton(MainWindow)
        self.warningRight.setText("Right Signaling")
        self.warningRight.setStyleSheet("font:bold;")
        self.warningRight.setGeometry(QtCore.QRect(680, 400, 120, 30))
        self.warningRight.clicked.connect(self.rightSignaling)

        # Warning Lights
        self.warningLightLeftRear = QtWidgets.QLabel(self.centralwidget)
        self.warningLightLeftRear.setGeometry(QtCore.QRect(260, 190, 20, 20))

        self.warningLightRightRear = QtWidgets.QLabel(self.centralwidget)
        self.warningLightRightRear.setGeometry(QtCore.QRect(260, 293, 20, 20))

        self.warningLightLeftFront = QtWidgets.QLabel(self.centralwidget)
        self.warningLightLeftFront.setGeometry(QtCore.QRect(650, 190, 20, 20))

        self.warningLightRightFront = QtWidgets.QLabel(self.centralwidget)
        self.warningLightRightFront.setGeometry(QtCore.QRect(650, 293, 20, 20))

        # Lock Car
        self.lockCar1 = QtWidgets.QPushButton(MainWindow)
        self.lockCar1.setText("Lock car")
        self.lockCar1.setStyleSheet("font: bold;")
        self.lockCar1.setGeometry(QtCore.QRect(680, 340, 120, 30))
        self.lockCar1.clicked.connect(self.LockCar)

        # Unlock Car
        self.unlockCar1 = QtWidgets.QPushButton(MainWindow)
        self.unlockCar1.setText("Unlock car")
        self.unlockCar1.setStyleSheet("font: bold;")
        self.unlockCar1.setGeometry(QtCore.QRect(680, 310, 120, 30))
        self.unlockCar1.clicked.connect(self.unlockCar)

        # 4 leds for sweep
        self.led1_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led1_sweep.setGeometry(QtCore.QRect(220, 210, 20, 20))

        self.led2_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led2_sweep.setGeometry(QtCore.QRect(240, 210, 20, 20))

        self.led3_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led3_sweep.setGeometry(QtCore.QRect(260, 210, 20, 20))

        self.led4_sweep = QtWidgets.QLabel(self.centralwidget)
        self.led4_sweep.setGeometry(QtCore.QRect(280, 210, 20, 20))

        # KL_s led
        self.KL_S = QtWidgets.QLabel(self.centralwidget)
        self.KL_S.setGeometry(QtCore.QRect(750, 165, 20, 20))
        # KL_s label
        self.KL_S_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_S_label.setGeometry(QtCore.QRect(700, 165, 40, 20))
        self.KL_S_label.setStyleSheet("font: bold;")
        self.KL_S_label.setText("KL_s")

        # KL_15 led
        self.KL_15 = QtWidgets.QLabel(self.centralwidget)
        self.KL_15.setGeometry(QtCore.QRect(750, 190, 20, 20))
        # KL_15 label
        self.KL_15_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_15_label.setGeometry(QtCore.QRect(700, 190, 40, 20))
        self.KL_15_label.setStyleSheet("font: bold;")
        self.KL_15_label.setText("KL_15")

        # KL_50 led
        self.KL_50 = QtWidgets.QLabel(self.centralwidget)
        self.KL_50.setGeometry(QtCore.QRect(750, 215, 20, 20))
        # KL_50 label
        self.KL_50_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_50_label.setGeometry(QtCore.QRect(700, 215, 40, 20))
        self.KL_50_label.setStyleSheet("font: bold;")
        self.KL_50_label.setText("KL_50")

        # KL_75 led
        self.KL_75 = QtWidgets.QLabel(self.centralwidget)
        self.KL_75.setGeometry(QtCore.QRect(750, 240, 20, 20))
        # KL_75 label
        self.KL_75_label = QtWidgets.QLabel(self.centralwidget)
        self.KL_75_label.setGeometry(QtCore.QRect(700, 240, 40, 20))
        self.KL_75_label.setStyleSheet("font: bold;")
        self.KL_75_label.setText("KL_75")

        # Close all leds button
        self.close_all = QtWidgets.QPushButton(MainWindow)
        self.close_all.setText("Close all leds")
        self.close_all.setStyleSheet("font: bold;color: red")
        self.close_all.setGeometry(QtCore.QRect(50, 50, 120, 35))
        self.close_all.clicked.connect(self.close_all_leds)

        # 1 Led inside
        self.interior_lights = QtWidgets.QPushButton(MainWindow)
        self.interior_lights.setText("Interior lights")
        self.interior_lights.setStyleSheet("font: bold;")
        self.interior_lights.setGeometry(QtCore.QRect(50, 150, 160, 41))
        self.interior_lights.clicked.connect(self.set_interior_lights)

        # Led brightness percentage label
        self.percentage_label = QtWidgets.QLabel(self.centralwidget)
        self.percentage_label.setGeometry(QtCore.QRect(50, 260, 90, 40))
        self.percentage_label.setStyleSheet("font: bold;")
        self.percentage_label.setText("Percentage")

        # Led brightness progress bar
        self.progress_bar = QtWidgets.QProgressBar(MainWindow)
        self.progress_bar.setGeometry(50, 310, 200, 21)
        self.progress_bar.setRange(0, 100)

        # Led brightness spinbox
        self.spinBox = QtWidgets.QSpinBox(MainWindow)
        self.spinBox.setGeometry(QtCore.QRect(150, 260, 75, 41))
        self.spinBox.setKeyboardTracking(True)
        self.spinBox.setRange(0, 100)
        self.spinBox.valueChanged.connect(self.valuechange)

        # Sweep button
        self.sweep = QtWidgets.QPushButton(MainWindow)
        self.sweep.setText("Sweep")
        self.sweep.setStyleSheet("font: bold;")
        self.sweep.setGeometry(QtCore.QRect(50, 200, 160, 41))
        self.sweep.clicked.connect(self.sweep_threads)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    ############################### EXERCISE 1 ###############################
    # Clear all leds and widgtets when the Close all leds is pressed
    def close_all_leds(self):
        self.interior_light_led("white")

    # Open one led when interior lights is pressed  
    def interior_light_led(self, b1):
        self.interiorLightsLabel.setStyleSheet("background-color:" + str(b1) + ";border-radius:5px;")

    # Function called from button handler
    def set_interior_lights(self):
        self.interior_light_led("green")

    ############################### EXERCISE 2 ###############################
    # Sweep Leds thread
    def sweep_threads(self):
        self.thread = MyThread_sweep()
        self.thread.sweepLedsSignal.connect(self.sweep_leds)
        self.thread.start()

    # Sweep Leds function
    def sweep_leds(self, val):
        if val == 1:
            self.set4leds("pink", "white", "white", "white")
        if val == 2:
            self.set4leds("white", "purple", "white", "white")
        if val == 3:
            self.set4leds("white", "white", "brown", "white")
        if val == 4:
            self.set4leds("white", "white", "white", "green")
        if val == 0:
            self.set4leds("white", "white", "white", "white")

    # Sweep Leds
    def set4leds(self, led1, led2, led3, led4):
        self.led1_sweep.setStyleSheet("background-color:" + str(led1) + ";border-radius:5px;")
        self.led2_sweep.setStyleSheet("background-color:" + str(led2) + ";border-radius:5px;")
        self.led3_sweep.setStyleSheet("background-color:" + str(led3) + ";border-radius:5px;")
        self.led4_sweep.setStyleSheet("background-color:" + str(led4) + ";border-radius:5px;")

    ############################### EXERCISE 3 ###############################
    # Change progress bar value when spinbox value is changed
    def valuechange(self):
        global progress
        prog_local = self.spinBox.value()
        if prog_local > progress:
            self.change_pb_down_value(prog_local)
        else:
            self.change_pb_up_value(prog_local)

    # Change led brightness down when the spinbox value (representing led brightness percentage) is less than progress bar value
    def change_pb_down_value(self, value):
        global progress
        while value >= progress:
            self.progress_bar.setValue(progress)
            time.sleep(0.05)
            progress = progress + 1

    # Change led brightness up when the spinbox value (representing led brightness percentage) is bigger than progress bar value
    def change_pb_up_value(self, value):
        global progress
        while value <= progress:
            self.progress_bar.setValue(progress)
            time.sleep(0.05)
            progress = progress - 1

    ############################### EXERCISE 4 ###############################
    # Succesice KL led turn 
    def KL_lights(self, KL):
        global number
        if KL == 1:
            self.set_bg_colors("green", "white", "white", "white")
            self.prev_kl_label.setText("no_KL")
            self.current_kl_label.setText("Current KL:KL_s")
            self.next_kl_label.setText("KL_15")
        elif KL == 0:
            self.set_bg_colors("white", "white", "white", "white")
            self.prev_kl_label.setText(" ")
            self.current_kl_label.setText("Current KL:KL_s")
            self.next_kl_label.setText("KL_15")
            self.set_enable()
        elif KL == 2:
            self.set_bg_colors("green", "blue", "white", "white")
            self.prev_kl_label.setText("KL_s")
            self.current_kl_label.setText("Current KL:KL_15")
            self.next_kl_label.setText("KL_58")
        elif KL == 3:
            self.set_bg_colors("green", "blue", "red", "white")
            self.prev_kl_label.setText("no_15")
            self.current_kl_label.setText("Current KL:KL_50")
            self.next_kl_label.setText("KL_75")
        elif KL == 4:
            self.set_bg_colors("green", "blue", "red", "yellow")
            self.prev_kl_label.setText("no_50")
            self.current_kl_label.setText("Current KL:KL_75")
            self.next_kl_label.setText(" ")
            self.set_enable()

    # Set previous value for KL when previous KL button is pressed
    def prev_kl_function(self):
        global number
        number = number - 1
        self.KL_lights(number)

    # Set next value for KL when next KL button is pressed
    def next_kl_function(self):
        global number
        number = number + 1
        self.KL_lights(number)

    # Set enable KL buttons
    def set_enable(self):
        if self.prev_kl.isEnabled():
            self.prev_kl.setEnabled(False)
            self.next_kl.setEnabled(True)
        else:
            self.prev_kl.setEnabled(True)
            self.next_kl.setEnabled(False)

    # Set KL leds colors
    def set_bg_colors(self, l1, l2, l3, l4):
        self.KL_S.setStyleSheet("background-color:" + str(l1) + ";border-radius:5px;")
        self.KL_15.setStyleSheet("background-color:" + str(l2) + ";border-radius:5px;")
        self.KL_50.setStyleSheet("background-color:" + str(l3) + ";border-radius:5px;")
        self.KL_75.setStyleSheet("background-color:" + str(l4) + ";border-radius:5px;")

    ############################### EXERCISE 5 ##############################
    ################################ BONUS ################################
    # Open left door untill the obstacle is detected
    def open_door_left(self):
        valoare = self.spinBox_left.value()
        self.left_door_slider.setValue(valoare)

    # This function will stop the slider to go to values bigger than the obstacle
    def valuechange_left_slider(self):
        valoare = self.spinBox_left.value()
        if self.left_door_slider.value() > valoare:
            self.left_door_slider.setValue(valoare)
            self.left_door_slider.setStyleSheet("background-color:" + str("red") + ";border-radius:5px;")
        else:
            self.left_door_slider.setStyleSheet("background-color:" + str("white") + ";border-radius:5px;")

    # Open right door untill the obstacle is detected      
    def open_door_right(self):
        valoare = self.spinBox_right.value()
        self.right_door_slider.setValue(valoare)

    # This function will stop the slider to go to values bigger than the obstacle
    def valuechange_right_slider(self):
        valoare = self.spinBox_right.value()
        if self.right_door_slider.value() > valoare:
            self.right_door_slider.setValue(valoare)
            self.right_door_slider.setStyleSheet("background-color:" + str("red") + ";border-radius:5px;")
        else:
            self.right_door_slider.setStyleSheet("background-color:" + str("white") + ";border-radius:5px;")

    #########################################################################
    ############################### USED FUNCTION ###########################
    def setWarningLights(self, warningLightLeftRear, warningLightRightRear, warningLightLeftFront,
                         warningLightRightFront):
        self.warningLightLeftRear.setStyleSheet("background-color:" + str(warningLightLeftRear) + ";border-radius:5px;")
        self.warningLightRightRear.setStyleSheet(
            "background-color:" + str(warningLightRightRear) + ";border-radius:5px;")
        self.warningLightLeftFront.setStyleSheet(
            "background-color:" + str(warningLightLeftFront) + ";border-radius:5px;")
        self.warningLightRightFront.setStyleSheet(
            "background-color:" + str(warningLightRightFront) + ";border-radius:5px;")

    #########################################################################

    ############################### EXERCISE 6 ##############################
    # Warning lights thread
    def warningLightsButton(self):

        self.thread_warning = MyThread_warning()
        self.thread_warning.warningLightsSignal.connect(self.warningLighs)
        self.thread_warning.start()


# Warning Lights function
def warningLighs(self, val):
    if val == 1:
        self.setWarningLights("orange", "orange", "orange", "orange")
    if val == 0:
        self.setWarningLights("white", "white", "white", "white")


############################### EXERCISE 7 ##############################
# Left Signaling Lights
def leftSignaling(self):
    self.thread_left = MyThread_left()
    self.thread_left.leftLightsSignal.connect(self.whileLeft)
    self.thread_left.start()


def whileLeft(self, val):
    if val == 1:
        self.setWarningLights("orange", "white", "orange", "white")
    if val == 0:
        self.setWarningLights("white", "white", "white", "white")


############################### EXERCISE 8 ##############################
# Right Signaling Lights
def rightSignaling(self):
    self.thread_right = MyThread_right()
    self.thread_right.rightLightsSignal.connect(self.whileRight)
    self.thread_right.start()


def whileRight(self, val):
    if val == 1:
        self.setWarningLights("white", "orange", "white", "orange")
    if val == 2:
        self.setWarningLights("white", "white", "white", "white")


######################### Car Light - usefull for next ex ################
def setcarLight(self, color):
    self.carLight.setStyleSheet("background-color:" + str(color) + ";border-radius:5px;")


# Open and close the interior light
def carLightSet(self):
    pass
    ''' complete with necesarry code '''


############################### EXERCISE 9 ##############################
# Unlock car
def unlockCar(self):
    self.thread_unlockCar = MyThread_unlockCar()
    self.thread_unlockCar.unlockCarSignal.connect(self.UnlockCarThread)
    self.thread_unlockCar.start()


def UnlockCarThread(self, val):
    pass
    ''' complete with necesarry code '''


############################### EXERCISE 10 ##############################
# Lock the car
def LockCar(self):
    self.thread_lockCar = MyThread_lockCar()
    self.thread_lockCar.lockCarSignal.connect(self.LockCarThread)
    self.thread_lockCar.start()


def LockCarThread(self, val):
    pass
    ''' complete with necesarry code '''


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

        elif result == QtWidgets.QMessageBox.No:
            event.ignore()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.center()
    sys.exit(app.exec_())
