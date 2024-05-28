#密碼管理器 改良版

#tkinter  messagebox
from tkinter import messagebox

# messagebox.showinfo(title="標題", message="12345")
# messagebox.showerror(title="標題", message="12345")
# messagebox.showwarning(title="標題", message="12345")
# print(messagebox.askyesno(title="標題", message="12345"))
# print(messagebox.askokcancel(title="標題", message="12345"))
# print(messagebox.askretrycancel(title="標題", message="12345"))



#測驗1
#加入錯誤訊息、成功訊息、重複訊息

# from tkinter import *
# from PIL import ImageTk
# import json
#
# window = Tk()
# window.title("密碼管理器")
# window.config(padx=50,pady=50)
# #鎖 icon
# img = ImageTk.PhotoImage(file = "lock.png")
# canvas = Canvas(window,width=224,height=225)
# canvas.create_image(112,112,image = img)
#
# label1 = Label(text="名稱")
# entry1 = Entry(width=25)
#
# label2 = Label(text="帳號")
# entry2 = Entry(width=25)
#
# label3 = Label(text="密碼")
# entry3 = Entry(width=25)
#
# def add_password():
#     name = entry1.get()
#     account = entry2.get()
#     password = entry3.get()
#     data = {}
#     if name != "" and account != "" and password != "":
#         with open("password_project.json", "r") as f:
#             data_str = f.read()
#             if data_str == "":
#                 data = {}
#             else:
#                 data = json.loads(data_str)
#
#         # 檢查name是否有重複?
#         if name in list(data):
#             messagebox.showerror(title="錯誤!", message="帳號已重複!")
#         else:
#             data[name] = {
#                 "account": account,
#                 "password": password
#             }
#             # 寫入password_project.json
#             with open("password_project.json", "w") as f:
#                 f.write(json.dumps(data))
#
#             #清除輸入框文字
#             entry1.delete(0, 'end')
#             entry2.delete(0, 'end')
#             entry3.delete(0, 'end')
#
#             messagebox.showinfo(title="成功!", message="新增成功!")
#
#     else:
#         messagebox.showerror(title="新增失敗!", message="不能為空白!")
#
#
# button = Button(text="新增",command=add_password, width=35, bg="#0066CC", fg="white")
#
# canvas.grid(row=0,column=0,columnspan=2)
# label1.grid(row=1,column=0)
# entry1.grid(row=1,column=1,pady=5)
# label2.grid(row=2,column=0)
# entry2.grid(row=2,column=1,pady=5)
# label3.grid(row=3,column=0)
# entry3.grid(row=3,column=1,pady=5)
# button.grid(row=4,column=0,pady=10,columnspan=2)
# window.mainloop()



#錯誤處理

# try:
#     file = open("aaa.txt")
#     print("程式執行成功")
# except:
#     open("aaa.txt","w")
#     print("程式發生錯誤")

# try:
#     file = open("aaaxd.txt")
# except IndexError:
#     print("資料錯誤!")
# except FileNotFoundError or NameError as err:
#     open("aaa.txt", "w")
#     print("開啟檔案發生錯誤")
#     print(err)
# else:
#     #若皆無錯誤產生，會執行else的程式碼
#     print("else成功執行")
# finally:
#     #不管有沒有錯誤，都會執行
#     print("finally執行")


#發起錯誤  raise  exception

# age = input("請輸入年紀:")
# age = int(age)
# if age<0:
#     raise ValueError("年紀不可為負數!")




#測驗2  改良11天的專案，身高體重亂輸入會跳錯誤訊息
# from tkinter import *
# from my_package import health
#
# window = Tk()
# window.config(padx=10,pady=10)
# window.title("BMI計算機")
# window.geometry("500x500")
#
# def cal_bmi():
#     try:
#         height = float(entry_height.get())
#         weight = float(entry_weight.get())
#         if height<0 and weight<0:
#             raise ValueError("不可為負數!")
#     except:
#         messagebox.showerror(title="發生錯誤!", message="亂輸入不計算")
#     else:
#         bmi = health.get_bmi(height, weight)
#         label_bmi["text"] = f"您的BMI:{bmi}"
#
#
#
# label_height = Label(text="身高",font=('標楷體',20))
# entry_height = Entry(width=10,font=('標楷體',20))
# label_heightUnit = Label(text="公分",font=('標楷體',20))
# label_weight = Label(text="體重",font=('標楷體',20))
# entry_weight = Entry(width=10,font=('標楷體',20))
# label_weightUnit = Label(text="公斤",font=('標楷體',20))
# label_bmi = Label(text="您的BMI:",font=('標楷體',20))
# button_cal = Button(text="計算",font=('標楷體',20),command=cal_bmi)
#
# label_height.grid(row=0,column=0)
# entry_height.grid(row=0,column=1)
# label_heightUnit.grid(row=0,column=2)
# label_weight.grid(row=1,column=0)
# entry_weight.grid(row=1,column=1)
# label_weightUnit.grid(row=1,column=2)
# label_bmi.grid(row=2,column=1)
# button_cal.grid(row=3,column=1)
#
# window.mainloop()




#---------專案  密碼管理器 改良版

#若沒有password_project.json ，則會創建一個 不會失敗

from tkinter import *
from PIL import ImageTk
import json

window = Tk()
window.title("密碼管理器")
window.config(padx=50,pady=50)
#鎖 icon
img = ImageTk.PhotoImage(file = "lock.png")
canvas = Canvas(window,width=224,height=225)
canvas.create_image(112,112,image = img)

label1 = Label(text="名稱")
entry1 = Entry(width=25)

label2 = Label(text="帳號")
entry2 = Entry(width=25)

label3 = Label(text="密碼")
entry3 = Entry(width=25)

#查詢密碼
def search_password():
    name = entry1.get()
    data = {}
    try:
        with open("password_project.json", "r") as f:
            data_str = f.read()
            if data_str == "":
                data = {}
            else:
                data = json.loads(data_str)
    except:
        messagebox.showerror(title="查詢失敗!", message="找不到此帳號名稱!")
        with open("password_project.json", "w") as f:
            data = {}
            f.write(json.dumps(data))
    else:
        if name in list(data):
            print()
            messagebox.showinfo(title=name, message=f"帳號:{data[name]["account"]}\n密碼:{data[name]["password"]}")
        else:
            messagebox.showerror(title="查詢失敗!", message="找不到此帳號名稱!")


#新增密碼
def add_password():
    name = entry1.get()
    account = entry2.get()
    password = entry3.get()
    data = {}
    if name != "" and account != "" and password != "":
        try:
            with open("password_project.json", "r") as f:
                data_str = f.read()
                if data_str == "":
                    data = {}
                else:
                    data = json.loads(data_str)
        except:
            with open("password_project.json", "w") as f:
                data = {}

                data[name] = {
                    "account": account,
                    "password": password
                }
                # 寫入password_project.json
                with open("password_project.json", "w") as f:
                    f.write(json.dumps(data))

                # 清除輸入框文字
                entry1.delete(0, 'end')
                entry2.delete(0, 'end')
                entry3.delete(0, 'end')

                messagebox.showinfo(title="成功!", message="新增成功!")
        else:
            # 檢查name是否有重複?
            if name in list(data):
                messagebox.showerror(title="錯誤!", message="帳號已重複!")
            else:
                data[name] = {
                    "account": account,
                    "password": password
                }
                # 寫入password_project.json
                with open("password_project.json", "w") as f:
                    f.write(json.dumps(data))

                #清除輸入框文字
                entry1.delete(0, 'end')
                entry2.delete(0, 'end')
                entry3.delete(0, 'end')

                messagebox.showinfo(title="成功!", message="新增成功!")

    else:
        messagebox.showerror(title="新增失敗!", message="不能為空白!")


button_search = Button(text="查詢",command=search_password, width=35, bg="#b8c0ff", fg="white")
button = Button(text="新增",command=add_password, width=35, bg="#0066CC", fg="white")

canvas.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1,pady=5)
label2.grid(row=2,column=0)
entry2.grid(row=2,column=1,pady=5)
label3.grid(row=3,column=0)
entry3.grid(row=3,column=1,pady=5)
button_search.grid(row=4,column=0,pady=10,columnspan=2)
button.grid(row=5,column=0,pady=5,columnspan=2)
window.mainloop()