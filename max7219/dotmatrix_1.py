##ex18-1 0~9���� ���

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

DIN = 19
CS = 24
CLK = 23

DOTDATA = [
    [ 0x3E, 0x7F, 0x71, 0x59, 0x4D, 0x7F, 0x3E, 0x00 ],
    [ 0x40, 0x42, 0x7F, 0x7F, 0x40, 0x40, 0x00, 0x00 ],
    [ 0x62, 0x73, 0x59, 0x49, 0x6F, 0x66, 0x00, 0x00 ],
    [ 0x22, 0x63, 0x49, 0x49, 0x7F, 0x36, 0x00, 0x00 ],
    [ 0x18, 0x1C, 0x16, 0x53, 0x7F, 0x7F, 0x50, 0x00 ],
    [ 0x27, 0x67, 0x45, 0x45, 0x7D, 0x39, 0x00, 0x00 ],
    [ 0x3C, 0x7E, 0x4B, 0x49, 0x79, 0x30, 0x00, 0x00 ],
    [ 0x03, 0x03, 0x71, 0x79, 0x0F, 0x07, 0x00, 0x00 ],
    [ 0x36, 0x7F, 0x49, 0x49, 0x7F, 0x36, 0x00, 0x00 ],
    [ 0x06, 0x4F, 0x49, 0x69, 0x3F, 0x1E, 0x00, 0x00 ],
]

def Write_Data_byte(Data) :
    GPIO.output(CS,GPIO.LOW)
    for i in range(0,8) :
        GPIO.output(CLK,GPIO.LOW)
        GPIO.output(DIN,Data&0x80)
        Data = Data << 1
        GPIO.output(CLK,GPIO.HIGH)

def Write_Data(address, dat) :
    GPIO.output(CS,GPIO.LOW)
    Write_Data_byte(address)
    Write_Data_byte(dat)
    GPIO.output(CS,GPIO.HIGH)
    
Write_Data(0x09,0x00)
Write_Data(0x0A,0x03)
Write_Data(0x0B,0x07)
Write_Data(0x0C,0x01)
Write_Data(0x0F,0x00)


while True :
    for i in range(0,10) :
        for j in range(0,8) :
            Write_Data(j+1,DOTDATA[i][j])
            time.sleep(0.1)
        for j in range(0,8) :
            Write_Data(j+1,0)
            time.sleep(0.01)
            
GPIO.cleanup()
