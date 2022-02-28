
import sys
import zhendongui
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore
import time
# import requests
# import pdb
import socket
# import datetime
# import time
# import numpy as np
# import struct
# import math
# import scipy.fftpack as fftpack
# import scipy.io as scio
# import matplotlib.pyplot as plt
# from tkinter import *  # 从tkinter库中导入所有函数

#服务器ip端口
device_ip='192.168.0.200'
device_port=1000
ip_port=(device_ip,device_port)

connect_flag=0 #连接标志
collect_flag=0 #采集标志
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

device_samp=256.0
fft_num=4096
adc_data1=[0]*fft_num
adc_data2=[0]*fft_num
adc_data1_index=0
adc_data2_index=0

gain1=0
gain2=0
att2_value=0
att1_value=0
LOG_LINE_NUM = 0

class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = zhendongui.Ui_Dialog()
        self.ui.setupUi(self)

    #连接断开设备   20220120
    def connect_device(self):
      global connect_flag #连接标志
      global text_ip
      global text_port
      global device_ip
      global device_port
      global button_connect
      global s

      if connect_flag==0:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        device_ip=self.ui.IPADDR.toPlainText ()
        port=self.ui.IPPORT.toPlainText ()
        device_port=int(port)
        s.connect((device_ip,device_port))
        ll=s.recv(15,socket.MSG_WAITALL)
        print(ll)
        connect_flag=1
        self.ui.CONNECT.setText(QtCore.QCoreApplication.translate("Dialog", "断开设备"))
        self.ui.MESSAGESHOW.append("连接成功！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)  #文本框显示到底部
        self.ui.CONSTA.setText("连接中！\n")
      else:
        s.close()
        connect_flag=0
        self.ui.CONNECT.setText(QtCore.QCoreApplication.translate("Dialog", "连接设备"))
        self.ui.MESSAGESHOW.append("断开成功！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)  #文本框显示到底部
        self.ui.CONSTA.setText("未连接！\n")

    #采样率查询   20220220
    def samp_query(self):
      global text_samp
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        # self.ui.MESSAGESHOW.setText("设备未连接！\n")
        return
      if collect_flag==1:
        self.data_collect_stop()
      inp = 'INPut:SMAPle?\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    # 采样设置   20220220
    def samp_set(self):
        global text_samp
        global device_samp
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志 self.ui.IPADDR.toPlainText ()
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()

        samp = self.ui.SAMDATA.toPlainText ()
        device_samp = float(samp)
        print("samp=%f" % device_samp)
        inp = 'INPut:SMAPle ' + samp + '\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp = ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    #fftnum设置   20220220
    def fftnum_set(self):
      global fft_num
      global text_fftnum
      global adc_data1
      global adc_data2
      global connect_flag #连接标志
      global collect_flag #采集标志 self.ui.IPADDR.toPlainText ()
      if collect_flag==1:
        self.data_collect_stop()
      fft_num=int(self.ui.FFTVAL.toPlainText ())
      adc_data1=[0]*fft_num
      adc_data2=[0]*fft_num
      print ("fft_num=%d" % fft_num)


    #输出通道查询   20220220
    def channelout_query(self):
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()
      inp = 'OUTPut:STATe?;:OUTPut:WAVE?\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    #输出通道开关设置   20220220
    def out_onoff_set(self):
      global out_onoff_value
      global connect_flag #连接标志
      global collect_flag #采集标志

      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()

      coll_type=self.ui.OUTSWITCH.currentText()
      # coll_code=int(self.outswitchcode(coll_type))
      if coll_type == '关闭':
          inp = 'OUTPut:STATe OFF\r\n'
          print("coll_type=%d" % 1)
      elif coll_type == '伪差分输出':
          inp = 'OUTPut:STATe SING\r\n'
          print("coll_type=%d" % 2)
      elif coll_type == '差分输出':
          inp = 'OUTPut:STATe DIFF\r\n'
          print("coll_type=%d" % 3)

      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    # #输出通道开关设置代码转换 20220221  备用
    # def outswitchcode(self,coll_type):
    #     coll_typeDict = {"关闭": "1",
    #                 "伪差分输出": "2",
    #                 "差分输出": "3"}
    #     return coll_typeDict.get(coll_type, '1')

    # 输出波形类型设置 20220221
    # def outtype_set(self):  #20220222 屏蔽此段简化操作
    #     self.ui.MESSAGESHOW.append("点击输出设置使能后下发给设备！")
    #     self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
    #     # self.ui.MESSAGESHOW.setText("点击输出设置使能后下发给设备！\n")

    # 输出设置使能 20220222
    def channelout_set(self):
        global text_outamp
        global text_outfreq
        global text_outscantime
        global outtype_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            # self.ui.MESSAGESHOW.setText("设备未连接！\n") self.ui.SAMDATA.toPlainText ()
            return
        if collect_flag == 1:
            self.data_collect_stop()

        amp = self.ui.OUTVPP.toPlainText ()
        freq = self.ui.OUTFREQ.toPlainText ()
        time = self.ui.OUTTIME.toPlainText ()

        outtype_value=self.ui.WAVESELECT.currentText()
        if outtype_value == '正弦波':
            inp = 'OUTPut:WAVE SIN,' + amp + ',0.0,' + freq + '\r\n'
        elif outtype_value == '随机噪声':
            freq = str(device_samp * 100.0 / 256.0)
            inp = 'OUTPut:WAVE NOISE,' + amp + ',0.0,' + freq + '\r\n'
        elif outtype_value == '正弦波扫频':
            inp = 'OUTPut:WAVE SCANSIN,' + amp + ',0.0,' + freq + ',' + time + '\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        # self.ui.MESSAGESHOW.setText(ll)



    # 通道1查询  20220223
    def channel1_query(self):
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！\n")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            # self.ui.MESSAGESHOW.setText("设备未连接！\n")
            return
        if collect_flag == 1:
            self.data_collect_stop()

        inp = 'INPut1:STATe?;:INPut1:GAIN?\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        inp = 'INPut1:COUPling?;:INPut1:SIGNal?;:INPut1:IEPE?\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        # self.ui.MESSAGESHOW.setText(ll)


    # 通道2查询   20220223
    def channel2_query(self):
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！\n")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()

        inp = 'INPut2:STATe?;:INPut2:GAIN?\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        inp = 'INPut2:COUPling?;:INPut2:SIGNal?;:INPut2:IEPE?\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp = ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

#输出通道一配置 20220223
    def channel_1set(self):
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      self.onoff1_set()
      time.sleep(0.1)
      self.acdc1_set()
      time.sleep(0.1)
      self.signal1_set()
      time.sleep(0.1)
      self.iepe1_set()
      time.sleep(0.1)
      self.gain1_set()

    # 输出通道一配置 20220223
    def channel_2set(self):
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      self.onoff2_set()
      time.sleep(0.1)
      self.acdc2_set()
      time.sleep(0.1)
      self.signal2_set()
      time.sleep(0.1)
      self.iepe2_set()
      time.sleep(0.1)
      self.gain2_set()

    #通道开关设置
    def onoff1_set(self):
      global onoff1_value
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()

      onoff1_value=self.ui.IN1SWITCH.currentText()
      if onoff1_value=='关闭':
        inp = 'INPut1:STATe OFF\r\n'
      elif onoff1_value=='打开':
        inp = 'INPut1:STATe ON\r\n'
      inp = bytes(inp, encoding='utf8')

    def onoff2_set(self):
      global onoff2_value
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()
      onoff2_value=self.ui.IN2SWITCH.currentText()
      if onoff2_value=='关闭':
        inp = 'INPut2:STATe OFF\r\n'
      elif onoff2_value=='打开':
        inp = 'INPut2:STATe ON\r\n'
      inp = bytes(inp, encoding='utf8')

    #增益设置
    def gain1_set(self):
      global gain1_value
      global gain1
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()
      # gain1=gain1_value.get()
      gain1=self.ui.IN1GAIN.currentText()
      gain=self.gain1_value(gain1)
      inp = 'INPut1:GAIN '+gain+'\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    def gain1_value(self,gain1):
        gain1Dict = {"1/16": "0",
                    "1/8": "1",
                    "1/4": "2",
                    "1/2": "3",
                    "1": "4",
                    "2": "5",
                    "4": "6",
                    "8": "7",
                    "16": "8",
                    "32": "9",
                    "64": "10",
                    "128": "11"}
        return gain1Dict.get(gain1, '0')

    def gain2_set(self):
      global gain2_value
      global gain2
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()

      # gain2=gain2_value.get()
      gain2=self.ui.IN2GAIN.currentText()
      gain=self.gain2_value(gain2)
      inp = 'INPut2:GAIN '+gain+'\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    def gain2_value(self,gain2):
        gain2Dict = {"1/16": "0",
                    "1/8": "1",
                    "1/4": "2",
                    "1/2": "3",
                    "1": "4",
                    "2": "5",
                    "4": "6",
                    "8": "7",
                    "16": "8",
                    "32": "9",
                    "64": "10",
                    "128": "11"}
        return gain2Dict.get(gain2, '0')
    #iepe设置
    def iepe1_set(self):
      global iepe1_value
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()
      iepe1_value=self.ui.IN1IEPE.currentText()
      if iepe1_value=='关闭':
        inp = 'INPut1:IEPE OFF\r\n'
      elif iepe1_value=='4mA':
        inp = 'INPut1:IEPE I4MA\r\n'
      elif iepe1_value=='10mA':
        inp = 'INPut1:IEPE I10MA\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    def iepe2_set(self):
        global iepe2_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()
        iepe2_value=self.ui.IN2IEPE.currentText()
        if iepe2_value == '关闭':
            inp = 'INPut2:IEPE OFF\r\n'
        elif iepe2_value == '4mA':
            inp = 'INPut2:IEPE I4MA\r\n'
        elif iepe2_value=='10mA':
            inp = 'INPut2:IEPE I10MA\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    # DC/AC耦合设置
    def acdc1_set(self):
        global acdc1_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()
        acdc1_value=self.ui.IN1ACDC.currentText()
        if acdc1_value == '直流':
            inp = 'INPut1:COUPling DC\r\n'
        elif acdc1_value == '交流':
            inp = 'INPut1:COUPling AC\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    def acdc2_set(self):
      global acdc2_value
      global connect_flag #连接标志
      global collect_flag #采集标志
      if connect_flag==0:
        self.ui.MESSAGESHOW.append("设备未连接！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        return
      if collect_flag==1:
        self.data_collect_stop()
      acdc2_value=self.ui.IN2ACDC.currentText()
      if acdc2_value=='直流':
        inp = 'INPut2:COUPling DC\r\n'
      elif acdc2_value=='交流':
        inp = 'INPut2:COUPling AC\r\n'
      inp = bytes(inp, encoding='utf8')
      s.sendto(inp, ip_port)
      ll=s.recv(1024)
      pp=ll.decode('utf8')
      self.ui.MESSAGESHOW.append(pp)
      self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    # 差分单端设置
    def signal1_set(self):
        global signal1_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()

        signal1_value=self.ui.IN1SW.currentText()
        if signal1_value == '单端':
            inp = 'INPut1:SIGNal SINGLE\r\n'
        elif signal1_value == '差分':
            inp = 'INPut1:SIGNal DIFF\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)


    def signal2_set(self):
        global signal2_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()
        signal2_value=self.ui.IN2SW.currentText()
        if signal2_value == '单端':
            inp = 'INPut2:SIGNal SINGLE\r\n'
        elif signal2_value=='差分':
            inp = 'INPut2:SIGNal DIFF\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    #    暂时无用
    # 前级衰减设置
    def att1_set(self):
        global att1_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()

        if att1_value.get() == 0:
            inp = 'INPut1:ATT OFF\r\n'
        else:
            inp = 'INPut1:ATT ON\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

#    暂时无用
    def att2_set(self):
        global att2_value
        global connect_flag  # 连接标志
        global collect_flag  # 采集标志
        if connect_flag == 0:
            self.ui.MESSAGESHOW.append("设备未连接！")
            self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
            return
        if collect_flag == 1:
            self.data_collect_stop()

        if att2_value.get() == 0:
            inp = 'INPut2:ATT OFF\r\n'
        else:
            inp = 'INPut2:ATT ON\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(1024)
        pp=ll.decode('utf8')
        self.ui.MESSAGESHOW.append(pp)
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)

    # 清除显示框  20220220
    def clearText(self):
        self.ui.MESSAGESHOW.clear()
    # 开始采集并绘图  20220220
    def data_collect_start(self):
        self.ui.MESSAGESHOW.append("功能暂未添加")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
    # 停止采集  20220223
    def data_collect_stop(self):
        global collect_flag  # 采集标志
        global adc_data1_index
        global adc_data2_index
        global ip_port
        global s

        collect_flag = 0
        adc_data1_index = 0
        adc_data2_index = 0

        inp = 'INPut1:ADCUp OFF;:INPut2:ADCUp OFF\r\n'
        inp = bytes(inp, encoding='utf8')
        s.sendto(inp, ip_port)
        ll = s.recv(10240)

        self.ui.MESSAGESHOW.append("停止采集！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        s.close()
        self.ui.MESSAGESHOW.append("连接断开！")
        self.ui.MESSAGESHOW.moveCursor(self.ui.MESSAGESHOW.textCursor().End)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ip_port)
        ll = s.recv(15, socket.MSG_WAITALL)
        print(ll)
        connect_flag = 1
        self.ui.CONNECT.setText(QtCore.QCoreApplication.translate("Dialog", "断开设备"))
        self.ui.MESSAGESHOW.setText("连接成功！\n")

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())