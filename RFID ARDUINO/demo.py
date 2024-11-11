import serial
import time

# Configura el puerto serial (ajusta a 'COM6')
arduino = serial.Serial('COM6', 9600)
time.sleep(2)  # Espera para que el puerto se inicie

def verificar_uid(uid):
    try:
        with open('permitidos.txt', 'r') as archivo:
            uids_permitidos = archivo.read().splitlines()
        # Imprime los UIDs permitidos y el UID que se compara
        print(f"UID leído: '{uid}'")
        print("UIDs permitidos:")
        for permitido in uids_permitidos:
            print(f"'{permitido}'")
        
        if uid in uids_permitidos:
            return "GRANTED"
        else:
            return "DENIED"
    except FileNotFoundError:
        print("Archivo 'permitidos.txt' no encontrado")
        return "DENIED"

while True:
    if arduino.in_waiting > 0:
        uid = arduino.readline().decode('utf-8').strip()
        if uid:  # Verifica que no esté vacío
            print(f"UID recibido: {uid}")
            
            resultado = verificar_uid(uid)
            arduino.write((resultado + '\n').encode('utf-8'))
            print(f"Resultado enviado: {resultado}")
