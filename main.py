import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://firegrados-default-rtdb.firebaseio.com/'
})

serialArduino = serial.Serial("COM7", 9600)



while True:
    ref = db.reference('Grados')
    Datos = str(ref.child('Valor').get())
    print(Datos)
    time.sleep(2)
    serialArduino.write(Datos.encode('ascii'))
