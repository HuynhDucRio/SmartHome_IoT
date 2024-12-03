import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from MainWindow import Ui_MainWindow  # import GUI file

import psutil
import firebase_admin
from firebase_admin import credentials, db

# Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate("Source Codes\smart-city-60734-firebase-adminsdk-5nacl-25edaaf2ce.json")  # Đường dẫn đến tệp chứng thực
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-city-60734-default-rtdb.asia-southeast1.firebasedatabase.app'  # Thay đổi thành URL của database
})

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up references to Firebase paths
        self.humidity_ref = db.reference('sensor/humidity')
        self.temperature_ref = db.reference('sensor/temperature')
        self.dust_ref = db.reference('sensor/dust')
        self.device_status_ref = db.reference('device')  # Đường dẫn cho trạng thái thiết bị
        
        # Initialize UI with current values
        self.update_data()

        # Set up a listener for real-time updates
        self.humidity_ref.listen(self.on_humidity_change)
        self.temperature_ref.listen(self.on_temperature_change)
        self.dust_ref.listen(self.on_dust_change)
        self.device_status_ref.listen(self.on_device_status_change)  # Lắng nghe thay đổi trạng thái thiết bị
        
        # Timer to refresh values that aren’t updated by Firebase
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_static_values)
        self.timer.start(5000)  # Cập nhật mỗi 5 giây

        # Connect button signals to their respective methods
        self.ui.LightButtonON.clicked.connect(self.turn_on_light)
        self.ui.LightButtonOFF.clicked.connect(self.turn_off_light)
        self.ui.AirPurButtonON.clicked.connect(self.turn_on_air_purifier)
        self.ui.AirPurButtonOFF.clicked.connect(self.turn_off_air_purifier)
        self.ui.AirConButtonON.clicked.connect(self.turn_on_air_conditioner)
        self.ui.AirConButtonOFF.clicked.connect(self.turn_off_air_conditioner)

    def update_data(self):
        # Get the current value from the Firebase
        humidity_value = self.humidity_ref.get()
        if humidity_value:
            self.humidityValue(humidity_value)

        temperature_value = self.temperature_ref.get()
        if temperature_value:
            self.temperatureValue(temperature_value)

        dust_value = self.dust_ref.get()
        if dust_value:
            self.dustValue(dust_value)

        # Retrieve battery status
        battery = psutil.sensors_battery()
        if battery:
            self.BatteryValue(battery.percent)

        # Load initial device status from Firebase
        device_status = self.device_status_ref.get()
        if device_status:
            self.update_device_ui(device_status)

    def on_humidity_change(self, event):
        if event.data:
            humidity_value = event.data
            self.humidityValue(humidity_value)

    def on_temperature_change(self, event):
        if event.data:
            temperature_value = event.data
            self.temperatureValue(temperature_value)

    def on_dust_change(self, event):
        if event.data:
            dust_value = event.data
            self.dustValue(dust_value)

    def on_device_status_change(self, event):
        if event.data:
            device_status = event.data
            self.update_device_ui(device_status)

    def update_static_values(self):
        battery = psutil.sensors_battery()
        if battery:
            self.BatteryValue(battery.percent)

    def update_device_ui(self, device_status):
        # Update UI based on device status from Firebase
        if 'Light' in device_status:
            light_status = device_status['Light']
            if light_status:
                self.ui.Light.setPixmap(QPixmap("den1.gif"))
            else:
                self.ui.Light.setPixmap(QPixmap("den0.png"))

        if 'AirPur' in device_status:
            purifier_status = device_status['AirPur']
            if purifier_status:
                self.ui.AirPur.setPixmap(QPixmap("kk1.gif"))
            else:
                self.ui.AirPur.setPixmap(QPixmap("kk0.png"))

        if 'AirCon' in device_status:
            ac_status = device_status['AirCon']
            if ac_status:
                self.ui.AirCon.setPixmap(QPixmap("dh1.png"))
            else:
                self.ui.AirCon.setPixmap(QPixmap("dh0.png"))

    def temperatureValue(self, value):
        temp = 600 - value * 6
        self.ui.tempValue.setFixedHeight(int(temp))
        labelText = '''<html><head/><body><span style=" font-size:31pt;">{VALUE}</span><span style=" font-size:31pt; vertical-align:super;">°</span><span style=" font-size:31pt;">C</span></p></body></html>'''
        newText = labelText.replace("{VALUE}", str(int(value)))
        self.ui.labelTemperature.setText(newText)

    def humidityValue(self, value):
        styleSheet = ''' 
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(85, 0, 255, 0), stop:{STOP_2} rgba(255, 255, 0, 255));
        }
        '''
        highestScale = 100.0
        progress = (highestScale - value) / highestScale
        stop_1 = str(progress - 0.001 if progress != 0 else progress)
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.ProgressCircularDS.setStyleSheet(newStylesheet)
        
        labelText = '''<p><span style=" font-size:30pt;">{VALUE}</span><span style=" font-size:30pt; vertical-align:super;">%</span></p>'''
        newText = labelText.replace("{VALUE}", str(int(value)))
        self.ui.labelDSValue.setText(newText)

    def dustValue(self, value):
        styleSheet = ''' 
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(85, 0, 255, 0), stop:{STOP_2} rgba(100, 255, 0, 255));
        }
        '''
        highestScale = 500.0 
        progress = (highestScale - value) / highestScale
        stop_1 = str(progress - 0.001 if progress != 0 else progress)
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.ProgressCircularUS.setStyleSheet(newStylesheet)

        labelText = '''<p><span style=" font-size:30pt;">{VALUE}</span><span style=" font-size:30pt; vertical-align:super;">mg/m3</span></p>'''
        newText = labelText.replace("{VALUE}", str(int(value)))
        self.ui.labelUSValue.setText(newText)

    def BatteryValue(self, value):
        self.ui.BatteryValue.setValue(value)
        labelText = '''<p><span style=" font-size:16pt;">{VALUE}</span><span style=" font-size:16pt; vertical-align:super;">%</span></p>'''
        newText = labelText.replace("{VALUE}", str(int(value)))
        self.ui.labelBatteryPercentage.setText(newText)

    def turn_on_light(self):
        print("Turning on the light...")
        self.ui.Light.setPixmap(QPixmap("den1.gif"))  # Update with your image path
        self.device_status_ref.update({'Light': 1})  # Cập nhật Firebase

    def turn_off_light(self):
        print("Turning off the light...")
        self.ui.Light.setPixmap(QPixmap("den0.png"))  # Update with your image path
        self.device_status_ref.update({'Light': 0})  # Cập nhật Firebase

    def turn_on_air_purifier(self):
        print("Turning on the air purifier...")
        self.ui.AirPur.setPixmap(QPixmap("kk1.gif"))  # Update with your image path
        self.device_status_ref.update({'AirPur': 1})  # Cập nhật Firebase

    def turn_off_air_purifier(self):
        print("Turning off the air purifier...")
        self.ui.AirPur.setPixmap(QPixmap("kk0.png"))  # Update with your image path
        self.device_status_ref.update({'AirPur': 0})  # Cập nhật Firebase

    def turn_on_air_conditioner(self):
        print("Turning on the air conditioner...")
        self.ui.AirCon.setPixmap(QPixmap("dh1.png"))  # Update with your image path
        self.device_status_ref.update({'AirCon': 1})  # Cập nhật Firebase

    def turn_off_air_conditioner(self):
        print("Turning off the air conditioner...")
        self.ui.AirCon.setPixmap(QPixmap("dh0.png"))  # Update with your image path
        self.device_status_ref.update({'AirCon': 0})  # Cập nhật Firebase

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())