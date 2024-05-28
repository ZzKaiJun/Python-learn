#模組引入
# import question as q
# from question import Question, QuestionGame
# from question import *
import tkinter.font
#套件 package
#將要打包的函式移到同一路徑，在新的路徑裡新增一個 __init__
#之後就能夠使用這個套件了
#ctrl按著  右鍵點套件可以查看套件的初始檔 __init__

# import my_package.health
# import json
# print(my_package.health.get_bmi(167,67))


#tuple  元組
#創建後就無法修改

# scores = (20, 30 ,50 ,36, 85, 90)
# print(scores[0])


#tkinter 模組(套件)    GUI程式 圖形介面程式
#創建視窗、標籤

from tkinter import *



# window = Tk()
# window.title("第一個圖形程式")
# window.geometry("400x300")
# # window.maxsize(width=800,height=600)         #視窗大小最大值
# # window.minsize(width=200,height=150)         #視窗大小最小值
# # window.resizable(False,False)    #是否能調整視窗大小
#
# my_label = Label(text="你好", font=("微軟正黑體", 24))
# print(tkinter.font.families())                 #顯示可用字體
# my_label.pack(side="top")
#
# #改變設定、創建按鈕、輸入框
# #修改Label的兩種方法:
# my_label["text"] = "JJ"
# my_label.config(text="DAJJ", font=("微軟正黑體", 10))
#
# def click():
#     my_label["text"] = my_entry.get()
#     print("被按了")
#
# #按鈕
# my_button = Button(text="按鈕", font=("微軟正黑體", 10), command=click)
# my_button.pack(side="top")
#
# #輸入框
# my_entry = Entry(width=10, font=("微軟正黑體", 10))
# my_entry.pack(side="top")
#
# #其他常用元件:
# #spinbox
# def use_spinbox():
#     print(my_spinbox.get())
# my_spinbox = Spinbox(from_=0,
#                      to=100,
#                      width=20,
#                      command=use_spinbox)
# my_spinbox.pack(side = "top")
#
# #scale 拉桿
# def use_scale(value):
#     print(value)
# my_scale = Scale(from_=0,to=100,command=use_scale)
# my_scale.pack(side="top")
#
# #checkbutton
# def use_checkbutton():
#     print(check.get())
# check = IntVar()       #tkinter裡的變數物件
# my_check = Checkbutton(text="打勾?",font=("微軟正黑體", 10), variable=check, command=use_checkbutton)
# my_check.pack(side="top")
#
#
# #radiobutton
# def use_radio():
#     print(radio.get())
# radio = IntVar()
# my_radio1 = Radiobutton(text="吃飯",font=("微軟正黑體", 10),variable=radio,value=1,command=use_radio)
# my_radio2 = Radiobutton(text="吃麵",font=("微軟正黑體", 10),variable=radio,value=2,command=use_radio)
# my_radio1.pack(side="top")
# my_radio2.pack(side="top")
#
# window.mainloop()



#----排版方式  pack(上下左右)  place(座標)  grid(格子)

#padx、pady x和y的間隔

# window = Tk()
# window.geometry("600x400")
# window.config(padx=50,pady=50)
# my_label = Label(text = "JJ", font=('標楷體',20))
# # my_label.pack(side="top",pady=10, padx=10)
# # my_label.place(anchor="center",x=300, y=200)    #anchor="center"  將座標位置從物件的左上角改至物件中心
# my_label.grid(row=0,column=0)
# def use_button():
#     my_label["text"] = my_entry.get()
#     print(my_label["text"])
# my_button = Button(text="按我", font=('標楷體',20), command=use_button)
# # my_button.pack(side="top",pady=10, padx=10)
#
# my_entry = Entry(font=('標楷體',20))
# # my_entry.pack(side="top",pady=10, padx=10)
#
#
# window.mainloop()



#-------專案  bmi計算機  圖形介面
from my_package import health

window = Tk()
window.config(padx=10,pady=10)
window.title("BMI計算機")
window.geometry("500x500")

def cal_bmi():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = health.get_bmi(height,weight)
    label_bmi["text"] = f"您的BMI:{bmi}"

label_height = Label(text="身高",font=('標楷體',20))
entry_height = Entry(width=10,font=('標楷體',20))
label_heightUnit = Label(text="公分",font=('標楷體',20))
label_weight = Label(text="體重",font=('標楷體',20))
entry_weight = Entry(width=10,font=('標楷體',20))
label_weightUnit = Label(text="公斤",font=('標楷體',20))
label_bmi = Label(text="您的BMI:",font=('標楷體',20))
button_cal = Button(text="計算",font=('標楷體',20),command=cal_bmi)

label_height.grid(row=0,column=0)
entry_height.grid(row=0,column=1)
label_heightUnit.grid(row=0,column=2)
label_weight.grid(row=1,column=0)
entry_weight.grid(row=1,column=1)
label_weightUnit.grid(row=1,column=2)
label_bmi.grid(row=2,column=1)
button_cal.grid(row=3,column=1)

window.mainloop()






