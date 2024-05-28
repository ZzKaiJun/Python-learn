#函式進階用法
#函式參數預設值

# def abc(a,b,c=3):
#     print(a,b,c)
#
# abc(1,2)

# *args 傳入多個參數 (傳入多少個都可以)

# nums 為元組
# def sum(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
# print(sum(1,3,4,5))

# **kwargs 傳入多個指定參數(幾個都可以)
# def add(**nums):
#     print(nums)
#
# add(num1=1,num2=2)


#安裝第三方套件

#使用別人的函式
# from tkinter import *
# from PIL import ImageTk

# window = Tk()
# window.config(padx=10, pady=10)
# window.geometry("400x300")
#
# label = Label(text="你好",font=("標楷體",20), bg="red", fg="blue")
# label.pack()
#
# button = Button(text="按鈕",font=("標楷體",20), bg="#ffafcc", fg="#a2d2ff")
# button.pack()
#
# window.mainloop()


#載入圖片
# window = Tk()
# window.config(bg="yellow")
#
# img = ImageTk.PhotoImage(file = "Saking.jpeg")
# window.iconphoto(True,img)
# canvas = Canvas(width="1080",height="1080",bg="yellow", highlightthickness=0)
# canvas.create_image(540,540,image=img)
# canvas.pack()
#
# window.mainloop()


#columnspan的排版方式

# window = Tk()
#
# label1 = Label(bg="red", width=20, height=5)
# label2 = Label(bg="yellow", width=20, height=5)
# label3 = Label(bg="blue", width=40, height=5)
#
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=1)
# label3.grid(row=2, column=0, columnspan=2)
# window.mainloop()


#-------專案  密碼管理器


from tkinter import *
from PIL import ImageTk
import json

window = Tk()
window.title("密碼管理器")
# window.geometry(width=500,height=500)
# window.config(padx=5,pady=5)
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

def add_password():
    name = entry1.get()
    account = entry2.get()
    password = entry3.get()
    data = {}
    if name != "" and account != "" and password != "":
        with open("password_project.json", "r") as f:
            data_str = f.read()
            if data_str == "":
                data = {}
            else:
                data = json.loads(data_str)
            data[name] = {
                "account":account,
                "password":password
            }

        # 寫入password_project.json
        with open("password_project.json", "w") as f:
            f.write(json.dumps(data))

    else:
        print("不能為空白!")

button = Button(text="新增",command=add_password, width=35, bg="#0066CC", fg="white")

canvas.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1,pady=5)
label2.grid(row=2,column=0)
entry2.grid(row=2,column=1,pady=5)
label3.grid(row=3,column=0)
entry3.grid(row=3,column=1,pady=5)
button.grid(row=4,column=0,columnspan=2)
window.mainloop()







