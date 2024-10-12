import serial
arduino_port = 'COM4'
baud = 9600
fileName = "analog-data.csv"
sample = 15
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:", arduino_port)
file = open(fileName, "a")
print("Created file")

line = 0

while line <= sample:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print("Line" + str(line)+ ": writing ...")
    getData = str(ser.readline())
    data=getData[0:][:-2]
    print(data)

    file = open(fileName, "a")
    
    file.write(data + "\n")
    line = line+1
print("Data collectiion  complete!")
    
                
            
