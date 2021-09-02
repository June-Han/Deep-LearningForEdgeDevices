import serial
import time

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    status  = 0
    while status < 2:
        if status == 0:
            ser.write(b"Wash\n")
            line = ser.readline().decode('utf-8').rstrip()
			print(line)
            while True:
                #When the washing process starts
                #ser.write(b"Wash\n")
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                #print("Status num is "+ str(status))
                if line == "Completed":
                    ser.flush()
                    break
                time.sleep(2)
        elif status == 1:
            ser.write(b"StartSter\n")
            line = ser.readline().decode('utf-8').rstrip()
            while line != "JCompleted":
                #When the washing process starts
                #ser.write(b"StartSter\n")
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                time.sleep(2)  
        ser.flush()
        status += 1

        '''
        #When the user press continue to sterilisation process after ML
        ser.write(b"StartSter\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(20)

        #For stop button to return to welcome page
        ser.write(b"Abort\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        '''
        #Note for the done function is either time after sterilisation, or only off after user press retrieve