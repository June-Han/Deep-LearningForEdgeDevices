import serial
import time

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.flush()
    
    while True:
        #When the washing process starts
        ser.write(b"StartWash\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(20)

        #When the user press continue to sterilisation process after ML
        ser.write(b"StartSter\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(20)

        #For stop button to return to welcome page
        ser.write(b"Abort\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

        #Note for the done function is either time after sterilisation, or only off after user press retrieve