# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:53:53 2018

@author: SSG_Share_1/Natsu

Loging distand of righte clicks.
output is cmd and "????.csv" 

It is same with distanbt-10.py
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
        
    epoc.append(i) 
    div_s.append(d)
    global sig
    sig=sum(div_s)    
    kyori=div_s[-1]
    if i == 1:
        print("Zero point was set!")
        time.sleep(0.3)
        print("Start! When finish Press ESC key!")
    elif ((i-1) % 10) == 0:
        print(i-1,",",kyori)
        file_output()              
    else:
         print(i-1,",",kyori)
         

    #print("総距離",round(sig,4))
    #print(epoc,"\n",div_s) 
##################################################################
 #平均値を計算
def average():
    ave = sig/(len(div_s))
    #print(ave,sig,div_s) 
    return(ave)
################################################################

#csvファイル出力
def file_output():
    print("save ?  Type & Press Enter key.")
    state_enter = win32api.GetKeyState(0x0D)
    while True:
        line=input() 
        if win32api.GetAsyncKeyState(0x02) != 0:
            pass           
        elif win32api.GetAsyncKeyState(0x0D) != 0:
            try:
                with open(line + ".csv", 'x',newline='') as f:                
                    del div_s[0]
                    del epoc[-1]
                    writer = csv.writer(f)
                    writer.writerows([epoc])
                    writer.writerows([div_s])
                    ave=str(average())
                    f.write(ave)
                    print(line+ ".csv is saved.")
                    print("You can continue Right Click.")
                    print("If you want to finish, press close button")
                    break
        
                #10個に連続適用するため、変数を初期化
                div_s.clear()
                sig=0
                epoc.clear()
            except FileExistsError:
                print("this file is allready exist! rename and try save again!")    
        else:
            print("This maniplate is not define! One possibility is same name file exist.\n")

          
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
                #print(div_s) 
            else:
                pass
        elif  c != 0 :
                #print(div_s) 
                file_output()
                break
    time.sleep(0.2)



def measur():
    while True:
        loop()
        
print("Don`t press Right click on this window")
time.sleep(0.3)
print("Click start position(Right click)")
measur()        
