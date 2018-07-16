# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:54:20 2018

@author: SSG_Share_1

Loging distand of righte clicks.
output is cmd and "????.csv" 
"""

import pyautogui 
import win32api
import time
import csv
import sys
#############################################################

loc=[]
#loc.append((0,0))
global div_s
div_s=[]
global sig
sig=0
global epoc
epoc=[] 


def location_log():
    location=pyautogui.position()
    loc.append(location)

    i=0
    for n in loc:#タプル要素ごとの距離計算
        if i<len(loc):
            x=loc[i][0]-loc[i-1][0]
            y=loc[i][1]-loc[i-1][1]
            #print(x,y)
            #print(x**2,y**2)
            d=(x**2+y**2)**(1/2)
            d=round(d,3)
            #print(div_s)            
        i+=1    
        
        
    div_s.append(d)
    
    #sig=sum(div_s)
    
    kyori=div_s[-1]    
    
    print(i,",",kyori)
    epoc.append(i)
    #print("総距離",round(sig,4))
    #print(epoc,div_s)

    
################################################################

#csvファイル出力
def file_output():
    #print("please input filename")
    #global line
    global div_s    
    with open(line + ".csv", 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerows([epoc])
        writer.writerows([div_s])
        #f.writelines(div_s)
################################################################    

#global line
cnt_meta=0
cnt=0
#print("please put log file name")
#line=sys.stdin


def loop():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    #state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    #esc = win32api.GetAsyncKeyState(0x1B)
    while True:
        #a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        c = win32api.GetAsyncKeyState(0x1B)
    
        if b != state_left:  # Button state changed
            state_left = b
            if b < 0:
                location_log()
            else:
                pass
        elif  c != 0 :
                print("!■■■■■■■■■■■■■■■■■■■■■■!")
                #print(div_s)
                file_output()
                print("one line add at" + line +".csv")
                break
    time.sleep(0.2)

def measur():
    while True:
        loop()
print("ready!")
print("Print File name you want to make")
global line 
line=input()
f = open(line+'.csv','w')
if len(line) >0:
    print("click log start !")
    measur()        