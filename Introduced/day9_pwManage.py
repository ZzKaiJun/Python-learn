#密碼管理器

#讀取、寫入 檔案

# r 讀取
# w 覆寫
# a 在原先資料後加東西

# file = open("123.txt", "r")
# print(file.read())
# print(file.readline())
# for line in file:
#     print(line)

#覆寫檔案
# file = open("123.txt", "w")
# file.write("123")

#添加
# file = open("123.txt", "a")
# file.write(" hello")

#選擇編碼模式，預設是不支援中文的
# file = open("123.txt", "a" , encoding="utf-8")
# file.write("\n小黑")
# file.close()

#另一種寫法，不用每次都file.close()
# with open("123.txt","a",encoding="utf-8") as file:
#     file.write("\n小黑")


#測驗1 把123.txt裡的數字相加
# sum = 0
# with open("123.txt", "r") as file:
#     for line in file:
#         sum += int(line)
# print(f"總合為:{sum}")


#絕對路徑 、 相對路徑
#絕對路徑 : ex:C:/Users/riderheg6411/PycharmProjects/Introduced/123.txt
#相對路徑 : 根據目前程式的位置做延伸  ex:123.txt

#絕對路徑
# with open("C:/Users/riderheg6411/PycharmProjects/Introduced/123.txt", "r") as file:
#     print(file.read())

#相對路徑
# with open("123.txt", "r") as file:
#     print(file.read())

# ../ 代表上一個資料夾
# with open("../456.txt", "r") as file:
#     print(file.read())


#json模組
#把資料轉換成json格式的字串、列表、字典
#把json格式的字串、列表、字典轉換回來

import json
data = {
    "name":"JJ",
    "age":25
}

# with open("password.json", "w") as file:
#     # json_data = json.dumps(data)            #轉換成字串
#     json_data = json.dumps(data, indent=4)    #indent:縮排的格子數
#     file.write(json_data)

# with open("password.json", "r") as file:
#     data = json.loads(file.read())
#     print(data)
#     print(data["name"])
#     print(data["age"])



#專案  密碼管理器
import json

def get_password_dic():
    with open("password_project.json", "r") as f:
        #如果檔案是空的話，沒辦法用json.loads轉成字串，要先判斷是否為""
        password_str = f.read()
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)

def check_name(name):
    with open("password_project.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            return True         #沒有帳號名稱重複
        else:
            data = json.loads(password_str)
            if name in list(data.keys()):
                return False    #有帳號名稱重複
            else:
                return True   #沒有帳號名稱重複

def add_password(name, account, password):
    is_nameOK = check_name(name)        #檢查帳號名稱是否重複
    password_dic = get_password_dic()

    if is_nameOK == True:
        password_dic[name] = {
            "account": account,
            "password": password
        }
        with open("password_project.json", "w") as f:
            f.write(json.dumps(password_dic))
        print("新增成功!")
    else:
        print("帳號名稱重複!")


is_retry = True
print("歡迎使用密碼管理器")

while is_retry:
    user_choice = input("請選擇要使用的功能 (r:查詢  a:新增  q:離開)")
    if user_choice == "r":
        with open("password_project.json","r") as f:
            # 如果檔案是空的話，沒辦法用json.loads轉成字串，要先判斷是否為""
            password_str = f.read()
            if password_str == "":
                data = {}
            else:
                data = json.loads(password_str)

            name = input("請輸入想查詢的帳號名稱:")

            if name in data:
                print("帳號名稱:" + name)
                print("帳號:" + data[name]["account"])
                print("密碼:" + data[name]["password"])
            else:
                "輸入錯誤!"

    elif user_choice == "a":
        name = input("請輸入帳號名稱:")
        account = input("請輸入帳號:")
        password = input("請輸入密碼:")
        add_password(name, account, password)

    else:
        is_retry = False
        print("感謝使用")






