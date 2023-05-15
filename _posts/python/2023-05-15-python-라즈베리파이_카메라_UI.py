---
title: "python-라즈베리파이_카메라_UI"
categories:
  - python
  - 라즈베리파이
  - 카메라

tags: [python, 라즈베리파이 , 카메라]
toc : true
comments: true
---
# 라즈베리파이 카메라 _UI 샘플 코드

1. 소스코드

 * 라즈베리파이 카메라 영상을 이용하여 촬영하는 코드
 * 코드 중에 시리얼 통신을 통해 카메라 영상 촬영하는 코드 포함
 * 단독 촬영이 아닌 연속 촬영으로 10장 찍음
 * GPIO 관련 사용하지 않는데 사용있으니 추후 해당 부분 삭제 후 활용하면 됩니다.

'''python
import serial
import threading 
from time import sleep
import RPi.GPIO as GPIO 
from picamera import PiCamera
import datetime
import os
import wx
import picamera
import cv2
import time
import ftplib


ABS_PATH = '/home/pi/Desktop/DEV/UICamera/'

WaveLength = [0,850,740,630,605,590,570,525,470,400,370]

def Delay():
    prev = time.time()
    while True:
        now = time.time()
        if now - prev > 0.1:
            break
        else:
            pass

# UI
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        global capture
        frame = wx.Frame.__init__(self, parent, title=title, size=(800,480))
       
        self.Center()


        cap = ShowCapture(self, capture)

#        st = wx.StaticText(self, label ="Staus : Wait")
#        st.SetPosition((670,10))
#        st.SetBackgroundColour((255,255,255))
        self.create_thread(self.TimeSetting)

        self.button1 = wx.Button(self, label="Capture")
        self.button1.SetPosition((670,50))
        self.button1.SetSize((90, 90))
        self.button1.Bind(wx.EVT_BUTTON, self.start_test)

        self.button1 = wx.Button(self, label="Capture_NIR")
        self.button1.SetPosition((670,150))
        self.button1.SetSize((90, 90))
        self.button1.Bind(wx.EVT_BUTTON, self.start_NIR)


        self.button1 = wx.Button(self, label="Time Setting")
        self.button1.SetPosition((650,250))
        self.button1.SetSize((80, 60))
        self.button1.Bind(wx.EVT_BUTTON, self.Test_Time)

        self.text = wx.TextCtrl(self, id=1, value='4000')
        self.text.SetPosition((650,330))

        self.button2 = wx.Button(self, label="UP")
        self.button2.SetPosition((750,300))
        self.button2.SetSize((40,40))
        self.button2.Bind(wx.EVT_BUTTON, self.Setting_LED_UP)

        self.button3 = wx.Button(self, label="DN")
        self.button3.SetPosition((750,350))
        self.button3.SetSize((40,40))
        self.button3.Bind(wx.EVT_BUTTON, self.Setting_LED_DOWN)

        self.button4 = wx.Button(self, label="LED Setting")
        self.button4.SetPosition((650,400))
        self.button4.Bind(wx.EVT_BUTTON, self.SettingLED)
        

  #      self.SetSizer(box)
        self.SetWindowStyle(wx.MAXIMIZE)

        self.Show(True)

    def Test_Time(self, e):
        self.create_thread(self.TimeSetting)
    
    def TimeSetting(self):
        cmd_time = "python3 /home/pi/Desktop/DEV/UICamera/connNTP.py"
        os.system(cmd_time)

    def Capture(self, event=None):
        ret, frame = capture.read()
        cv2.imwrite('image.jpg', frame)              

    def Capture_LED(self, event=None):
        global capture
        print("[Camera Start]")
        self.button1.SetLabel("ACTIVATED")
        for i  in range(1 ,11):
            d = datetime.datetime.now()
            print(d)
            str_number = str(i)
            SendCommand(b"AT+LED="+bytes(str_number).encode("utf-8") +b","+b"1"+b"\r\n")
            self.Delay()

            ret, frame = capture.read()
            cv2.imwrite('test_'+str_number+'.jpg', frame)           
            SendCommand(b"AT+LED="+bytes(str_number).encode("utf-8") +b","+b"0"+b"\r\n")

        print("[Camera End]")  
       # self.st.SetLabel("Staus : Wait")


    def Capture_LED_Thread(self, event=None):
        SaveThread = threading.Thread(target=Save_Image)
        thread.daemon = True
        SaveThread.start()

    def LoadImage(self):
               Img = wx.Image("image.jpg", wx.BITMAP_TYPE_JPEG)

               W = Img.GetWidth()
               H = Img.GetHeight()
 
               Img = Img.Scale(512, 300)

               self.Image.SetBitmap(wx.BitmapFromImage(Img))
               self.Refresh()

    def Setting_LED_UP(self, event=None):
        self.text.SetValue(str(int(self.text.GetValue())+1000))

    def Setting_LED_DOWN(self, event=None):
        self.text.SetValue(str(int(self.text.GetValue())-1000))

    def SettingLED(self, event=None):
        for i in range(1,11):
            str_number = str(i)
            SendCommand(b"AT+LEDPOWER=" +bytes(str_number).encode("utf-8")+b","+bytes(str(int(self.text.GetValue()))).encode("utf-8") +b"r\n") 

    def create_thread(self, target):
        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()

    def start_test(self, e):
        self.create_thread(self.Save_Image)

    def Save_Image(self):
        global capture
        print("[Camera Start]")
#        now = time.localtime()
#       self.button1.SetLabel("ACTIVATED")
#        DataDir= ABS_PATH+ 'Data/'+ str(now.tm_year) + str(now.tm_mon) +str(now.tm_mday)
        
        now = datetime.datetime.now()
        DataDir = ABS_PATH+ 'Data/'+ str(now.strftime("%Y%m%d_%X"))

        if not os.path.exists(DataDir):
            os.mkdir(DataDir)
        print(str(now.strftime("%Y%m%d_%X")))

        cmd_2 = "gpio -g write 4 1"
        os.system(cmd_2)
        Delay()

        for i  in range(1 ,11):
            str_Send_Number = str(i)
            now_file = time.localtime()
            str_number = str(WaveLength[i])
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"1"+b"\r\n")
            Delay()
            ret, frame = capture.read()
            str_SaveFile = str(i)+'_LED('+ str(int(self.text.GetValue()))+')_WL('+str_number+')_'+str(now_file.tm_hour) +str(now_file.tm_min)+str(now_file.tm_sec) +'.jpg'
            cv2.imwrite(DataDir+'/'+str_SaveFile, frame)           
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"0"+b"\r\n")
            fname = DataDir+'/'+str_SaveFile            

            Delay()
        print("[Camera End]") 

#        self.button1.SetLabel("Capture")

    def Test_LED(self, e):
        self.create_thread(self.Test_LED_ON)

    def Test_LED_ON(self):
        for i  in range(1 ,11):
            str_Send_Number = str(i)
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"1"+b"\r\n")
            Delay()
        for i  in range(1 ,11):
            str_Send_Number = str(i)
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"0"+b"\r\n")
            Delay()
        print("[Camera End]") 
        Delay()


    def start_NIR(self, e):
        self.create_thread(self.Save_Image_NIR)

    def Save_Image_NIR(self):
        global capture
        print("[Camera NIR Start]")        
        now = datetime.datetime.now()
        DataDir = ABS_PATH+ 'Data/'+ str(now.strftime("%Y%m%d_%X"))

        if not os.path.exists(DataDir):
            os.mkdir(DataDir)
        
        cmd_3 = "gpio -g write 4 0"
        os.system(cmd_3)
        Delay()

        for i  in range(1 ,11):
            now_file = time.localtime()
            str_number = str(WaveLength[i])
            str_Send_Number = str(i)
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"1"+b"\r\n")
            Delay()
            ret, frame = capture.read()
            str_SaveFile = str(i)+'_LED('+ str(int(self.text.GetValue()))+')_WL('+str_number+')_'+str(now_file.tm_hour) +str(now_file.tm_min)+str(now_file.tm_sec) +'_NOIR.jpg'
            cv2.imwrite(DataDir+'/'+str_SaveFile, frame)           
            SendCommand(b"AT+LED="+bytes(str_Send_Number).encode("utf-8") +b","+b"0"+b"\r\n")
            fname = DataDir+'/'+str_SaveFile                       
            Delay()
        print("[Camera End]") 
        Delay()

class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=15):
        wx.Panel.__init__(self, parent)
 
        self.capture = capture
        ret, frame = self.capture.read()
 
        height, width = frame.shape[:2]
        print(height)
        print(width)
        parent.SetSize((width+161, height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
        self.bmp = wx.BitmapFromBuffer(width, height, frame)
 
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)
 
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)
 
 
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)
 
    def NextFrame(self, event):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()




# Camera
class WriteThread(threading.Thread):
    def _init__(self,name):
         super().__init__()
         self.name = name

    def run(self):
         while True:
             sleep(1)

def SendCommand(cmd):
    print("[Send Command]")
    print(cmd)
    ser.write(cmd)
    print("\n")
    sleep(0.3)

def callback_Cam(channel):  
        global camera
        print("[Camera Active]")
        d = datetime.datetime.now()
#        camera.start_preview()
        sleep(1)
        camera.capture('/home/pi/Desktop/DEV/Serial/Data/image_'\
        +str(d.year) +str(d.month+d.day)+'_'+str(d.hour)+str(d.minute)+str(d.second) +'.jpg')
#        camera.stop_preview()
        print("[Cam close]")

def callback_Cam_CV(channel):
        global capture
    
        print("[Camera Start]")
        for i  in range(1 ,11):
            d = datetime.datetime.now()
            str_number = str(i)
            SendCommand(b"AT+LED="+bytes(str_number).encode("utf-8") +b","+b"1"+b"\r\n")
            ret, frame = capture.read()
            cv2.imwrite('test_'+str_number+'.jpg', frame)           
            SendCommand(b"AT+LED="+bytes(str_number).encode("utf-8") +b","+b"0"+b"\r\n")
        print("[Camera End]")


def callback_OnOff(channel):
        global b_Onoff
        global b_Onoff_array
        global i_LEDNumber
        data_LEDNumber = str(i_LEDNumber)
        print("Current LED "+data_LEDNumber +"\n")
        if  b_Onoff_array[i_LEDNumber-1] == True:
            b_Onoff_array[i_LEDNumber-1] = False
            SendCommand(b"AT+LED="+bytes(data_LEDNumber).encode("utf-8") +b","+b"1"+b"\r\n")
        else:
            b_Onoff_array[i_LEDNumber-1] = True
            SendCommand(b"AT+LED="+bytes(data_LEDNumber).encode("utf-8") +b","+b"0"+b"\r\n")

def callback_LedSwitch(channel):
        global i_LEDNumber
        print("falling edge detected Switch")
        if i_LEDNumber <10 :
            i_LEDNumber = i_LEDNumber +1
        else: 
            i_LEDNumber = 1
        print("Current LED " + str(i_LEDNumber) +"\n")


def callback_Up(channel):
        global i_LedPower
        global i_LedPower_array
        global i_LEDNumber
        if i_LedPower_array[i_LEDNumber-1] < 64000:
            i_LedPower_array[i_LEDNumber-1] = i_LedPower_array[i_LEDNumber-1] + 1000 
        data_LEDNumber = str(i_LEDNumber)
        print("falling edge detected MAX Power")
        data = str(i_LedPower_array[i_LEDNumber-1])
        print("Active LED " + data_LEDNumber +  " Active Power " + data + "\n") 
        SendCommand(b"AT+LEDPOWER="+bytes(data_LEDNumber).encode("utf-8") +b","+bytes(data).encode("utf-8")+b"\r\n")
        SendCommand(b"AT+LED="+bytes(data_LEDNumber).encode("utf-8") +b","+b"1"+b"\r\n")
        b_Onoff_array[i_LEDNumber-1] = True

def callback_Down(channel):
        global i_LedPower
        global i_LedPower_array
        global i_LEDNumber
        if i_LedPower_array[i_LEDNumber-1] >1000:
             i_LedPower_array[i_LEDNumber-1] = i_LedPower_array[i_LEDNumber-1] - 1000 
        data_LEDNumber = str(i_LEDNumber)
        print("falling edge detected Low Power")
        data = str(i_LedPower_array[i_LEDNumber-1])
        print("Active LED " + data_LEDNumber +  " Active Power " + data + "\n")
        SendCommand(b"AT+LEDPOWER="+bytes(data_LEDNumber,'utf-8') +b","+bytes(data,'utf-8')+b"\r\n")
        SendCommand(b"AT+LED="+bytes(data_LEDNumber,'utf-8') +b","+b"1"+b"\r\n")
        b_Onoff_array[i_LEDNumber-1] = True

def Setting_LED_Power():
    for i in range(1,11):
        str_number = str(i)
        SendCommand(b"AT+LEDPOWER=" +bytes(str_number).encode("utf-8")+b",0r\n")


ser = serial.Serial("/dev/ttyAMA0", 9600)    #Open port with baud rate
print("serial Connected !!")
#camera = PiCamera()

capture = cv2.VideoCapture(-1)
#Camera Setting
cmd_1 = "gpio -g mode 4 output"
os.system(cmd_1)


# Vairable
b_Onoff = True
b_Onoff_array = [False,False,False,False,False,False,False,False,False,False]

i_LedPower = 3000
i_LedPower_array =  [0,0,0,0,0,0,0,0,0,0]
i_LEDNumber = 1

#Settin default
Setting_LED_Power()



app = wx.App(False)
frame = MainWindow(None, "Camera Monitor")

app.MainLoop()


while True:
    received_data = ser.read()              #read serial port
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print ("[Receive Data]")
    print (received_data)                   #print received data
    print ("\n")



'''