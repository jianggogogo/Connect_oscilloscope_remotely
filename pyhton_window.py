#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox  # 要使用messagebox先要导入模块
import visa
import struct

import sys

import numpy as np

#采用python自带的visa驱动
rm = visa.ResourceManager('@py')

#rm = visa.ResourceManager('C:/Windows/System32/visa32.dll')

####!!!!!!!!!!!!!!!!!     这一步要自己改     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#添加自己的示波器的IP或者通过USB连接
inst = rm.get_instrument('TCPIP0::169.254.248.30::INSTR')

inst


#建立窗口window
window = tk.Tk()
 
# 窗口名字
window.title('示波器')
 
# 窗口的大小
window.geometry('1000x850') 

n=0 #通道选择全局变量

#------------------------------------------------------
#----------   标签-------------------------------------
#------------------------------------------------------
 
#在图形界面上设定标签
l = tk.Label(window, text='示波器控制欢迎你', bg='green', font=('Arial', 12), width=20, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.place(x=0,y=0)    # Label内容content区域放置位置，自动调节尺寸

#----------------------------------------------------
#---------按钮---------------------------------------
#----------------------------------------------------
# 选择通道1按钮
set_channel1_var = tk.StringVar()
channel_choose_1= tk.Label(window, textvariable=set_channel1_var, bg='green', fg='white', font=('Arial', 12), width=15, height=2)
channel_choose_1.place(x=0,y=70)

on_hit = False
def channel_choose_1_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        set_channel1_var.set('channel 1')
        inst.write(' :CHAN1:DISP ON\n')
    else:
        on_hit = False
        set_channel1_var.set('')
        inst.write(' :CHAN1:DISP OFF\n')
        n=1
#在窗口界面设置放置Button按键
channel_choose1_botton= tk.Button(window, text='channel1', font=('Arial', 12), width=10, height=1, command=channel_choose_1_fun)
channel_choose1_botton.place(x=0,y=40)

#----------------------------------------------------
#---------按钮---------------------------------------
#----------------------------------------------------
# 选择通道二按钮
set_channel2_var = tk.StringVar()
channel_choose_1= tk.Label(window, textvariable=set_channel2_var, bg='green', fg='white', font=('Arial', 12), width=15, height=2)
channel_choose_1.place(x=0,y=140)

on_hit = False
def channel_choose_2_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        set_channel2_var.set('channel 2')
        inst.write(' :CHAN2:DISP ON\n')
    else:
        on_hit = False
        set_channel2_var.set('')
        inst.write(' :CHAN2:DISP OFF\n')
        n=2

#在窗口界面设置放置Button按键
channel_choose2_botton= tk.Button(window, text='channel2', font=('Arial', 12), width=10, height=1, command=channel_choose_2_fun)
channel_choose2_botton.place(x=0,y=110)

#----------------------------------------------------
#---------按钮---------------------------------------
#----------------------------------------------------
# 选择通道三按钮
set_channel3_var = tk.StringVar()
channel_choose_3= tk.Label(window, textvariable=set_channel3_var, bg='green', fg='white', font=('Arial', 12), width=15, height=2)
channel_choose_3.place(x=0,y=210)

on_hit = False
def channel_choose_3_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        set_channel3_var.set('channel 3')
        inst.write(' :CHAN3:DISP ON\n')
    else:
        on_hit = False
        set_channel3_var.set('')
        n=3
        inst.write(' :CHAN3:DISP OFF\n')

#在窗口界面设置放置Button按键
channel_choose3_botton= tk.Button(window, text='channel3', font=('Arial', 12), width=10, height=1, command=channel_choose_3_fun)
channel_choose3_botton.place(x=0,y=180)

#----------------------------------------------------
#---------按钮---------------------------------------
#----------------------------------------------------
# 选择通道四按钮
set_channel4_var = tk.StringVar()
channel_choose_4= tk.Label(window, textvariable=set_channel4_var, bg='green', fg='white', font=('Arial', 12), width=15, height=2)
channel_choose_4.place(x=0,y=280)

on_hit = False
def channel_choose_4_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        set_channel4_var.set('channel 4')
        inst.write(' :CHAN4:DISP ON\n')
    else:
        on_hit = False
        set_channel4_var.set('')
        n=4
        inst.write(' :CHAN4:DISP OFF\n')


#在窗口界面设置放置Button按键
channel_choose4_botton= tk.Button(window, text='channel4', font=('Arial', 12), width=10, height=1, command=channel_choose_4_fun)
channel_choose4_botton.place(x=0,y=250)

#----------------------------------------------------
#---------按钮---------------------------------------
#----------------------------------------------------
# run和停止按钮
set_run_var= tk.StringVar()
run_set= tk.Label(window, textvariable=set_run_var, bg='green', fg='white', font=('Arial', 12), width=10, height=1)
run_set.place(x=800,y=30)

on_hit = False
def run_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        set_run_var.set('stop')
        inst.write(' :STOP\n')
    else:
        on_hit = False
        set_run_var.set('run')
        inst.write(' :RUN\n')

#在窗口界面设置放置Button按键
run_set_button= tk.Button(window, text='run\stop', font=('Arial', 12), width=10, height=1, command=run_fun)
run_set_button.place(x=800,y=0)


#---------按钮---------------------------------------
#----------------------------------------------------
# Auto按钮
#auto_var= tk.StringVar()
#auto_set= tk.Label(window, textvariable=auto_var, bg='green', fg='white', font=('Arial', 12), width=10, height=1)
#auto_set.place(x=100,y=220)

on_hit = False
def auto_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        #auto_var.set('auto')
        inst.write(':AUToscale\n')
    else:
        on_hit = False
        #auto_var.set('no auto')
        #inst.write(' :AUTO:ITEM ITEM1 \n')

#在窗口界面设置放置Button按键
auto_set_button= tk.Button(window, text='auto', font=('Arial', 12), width=10, height=1, command=auto_fun)
auto_set_button.place(x=700,y=0)


#---------按钮---------------------------------------
#----------------------------------------------------
# clear按钮
on_hit = False
def clear_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        #reset_var.set('clears')
        inst.write(' :CLEar \n')
    else:
        on_hit = False
        #reset_var.set('no auto')
        #inst.write(' :STOP\n')

#在窗口界面设置放置Button按键
reset_set_button= tk.Button(window, text='clear', font=('Arial', 12), width=10, height=1, command=clear_fun)
reset_set_button.place(x=600,y=0)


#---------按钮---------------------------------------
#----------------------------------------------------
# single按钮
on_hit = False
def single_fun():
    global on_hit
    if on_hit == False:
        on_hit = True
        #reset_var.set('single')
        inst.write(' :SINGle\n')
    else:
        on_hit = False
     

#在窗口界面设置放置Button按键
reset_set_button= tk.Button(window, text='single', font=('Arial', 12), width=10, height=1, command=single_fun)
reset_set_button.place(x=900,y=0)

#---------------------------------------------------
#_____________________list_____________________________
#-----------------------------------------
# 在图形界面上创建一个标签label用以显示并放置
var_sele_mode = tk.StringVar()  # 创建变量
lable_sele_mode= tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var_sele_mode)
lable_sele_mode.place(x=900,y=30)
 
# 事件
def print_selection():
    value = lb.get(lb.curselection())   # 获取当前选中的文本
    var_sele_mode.set(value)  # 为label设置值
    #inst_write('NORMal\n')
    #inst.write('SINGle\n')
    inst.write(':TRIGger:SWEep '+value+'\n')
     
# 调用print_selection函数
b1 = tk.Button(window, text='selection', width=15, height=2, command=print_selection)
b1.place(x=900,y=60)
 
# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set(()) # 为变量var2设置值
# 创建Listbox
lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox
# 创建一个list并将值循环添加到Listbox控件中
list_items = ['NORMal','AUTO','SINGle']
for item in list_items:
    lb.insert('end', item)  
lb.insert(1, 'NORMal')      
lb.insert(2, 'AUTO')   
lb.insert(3, 'SINGle')
lb.delete(2)      
lb.delete(2)
lb.delete(4)
lb.delete(1)
# 删除第二个位置的字符
# 删除第二个位置的字符

lb.place(x=900,y=90)

#----------------------scale---------------------
#------------------------------------------------
#------------------------------------------------

# lable position_verctical


position_vertical_var= tk.Label(window, bg='green', fg='white', width=20, text='empty')
position_vertical_var.place(x=400,y=60)
 
# 定义一个触发函数功能
def print_selection(v):
    position_vertical_var.config(text='s - v is:' + v)
    inst.write(' :DECoder1:POSition\n'+v+'\n')

#尺度滑条
scale_posstion_vertical = tk.Scale(window, label='position', from_=0.1, to=100, orient=tk.VERTICAL, length=250, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
scale_posstion_vertical.place(x=200,y=50)

#----------------------scale---------------------
#------------------------------------------------
#------------------------------------------------
# lable scale_verctical

scale_vertical_var= tk.Label(window, bg='green', fg='white', width=20, text='empty')
scale_vertical_var.place(x=400,y=80)
 
# 定义一个触发函数功能
def print_selection(v):
    scale_vertical_var.config(text='p - v is:' + v)
    inst.write(':CHANnel<'+n+'>:SCALe\n' )

#尺度滑条
scale_vertical = tk.Scale(window, label='scale', from_=0.1, to=100, orient=tk.VERTICAL, length=250, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
scale_vertical.place(x=300,y=50)

#----------------------scale---------------------
#------------------------------------------------
#------------------------------------------------

# lable postioon_horizontal


postioon_horizontal_var= tk.Label(window, bg='green', fg='white', width=20, text='empty')
postioon_horizontal_var.place(x=400,y=100)
 
# 定义一个触发函数功能
def print_selection(v):
    postioon_horizontal_var.config(text='p - h is:' + v)
    inst.write(' :CURSor:MANual:AX <'+v+'> \n')

#尺度滑条
postioon_horizontal = tk.Scale(window, label='postion', from_=0.1, to=100, orient=tk.HORIZONTAL, length=250, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
postioon_horizontal.place(x=450,y=150)


#----------------------scale---------------------
#------------------------------------------------
#------------------------------------------------

# lable scale_horizontal


scale_HORIZONTAL_var= tk.Label(window, bg='green', fg='white', width=20, text='empty')
scale_HORIZONTAL_var.place(x=400,y=120)
 
# 定义一个触发函数功能
def print_hor_scale(v):
    scale_HORIZONTAL_var.config(text='s - h is:' + v)
    inst.write(' :MATH:FFT:HSCale'+v+'\n')
#尺度滑条45
scale_HORIZONTAL = tk.Scale(window, label='scale', from_=0.1, to=100, orient=tk.HORIZONTAL, length=250, showvalue=0,tickinterval=2, resolution=0.01, command=print_hor_scale)
scale_HORIZONTAL.place(x=450,y=190)





# 定义并绑定键盘事件处理函数
def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect('key_press_event', on_key_event)


# 按钮单击事件处理函数
def _quit():
    # 结束事件主循环，并销毁应用程序窗口
    root.quit()
    root.destroy()
    button = Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)

#主窗口循环显示
window.mainloop()
