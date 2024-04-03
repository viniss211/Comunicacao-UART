import serial
import time

# Iniciando a conexão serial
try:
    arduino = serial.Serial('COM15', baudrate=9600, timeout=1)

    try:
        while True:
            # Solicita ao usuário para digitar uma mensagem para enviar ao Arduino
            message = input("Digite uma mensagem para enviar ao Arduino (ou digite 'sair' para encerrar): ")
            
            if message.lower() == 'sair':
                break  # Sai do loop se o usuário digitar 'sair'
            
            # Envia a mensagem para o Arduino
            arduino.write(message.encode() + b'\n')
            print("Enviado para Arduino:", message)
            
            # Espera pela resposta do Arduino e imprime-a
            resposta = arduino.readline().decode().strip()
            print("Resposta do Arduino:", resposta)
            time.sleep(1)

    finally:
        arduino.close()  # Fecha a conexão serial ao sair do loop

except serial.SerialException as e:
    print("Erro ao abrir a porta serial:", e) # Imprime o erro de exceção