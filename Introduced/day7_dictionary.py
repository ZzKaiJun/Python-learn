#字典 dictionary
# 鍵      值
# key    value
#"蘋果"  "apple"

# eng_dic = {
#     "蘋果":"apple",
#     "香蕉":"banana",
#     "貓":"cat",
#     "0" : 23,
#     "2.5" : "hi",
#     "is_male" : True
# }
# print(eng_dic)
# print(eng_dic["蘋果"])

# for key in eng_dic:
#     print(key)
#     print(eng_dic[key])


#測驗1  把消費金額大於10,000的客戶改為VIP，反之則為一般客戶
# customs_spending = {
#     "小白":2000,
#     "小黃":8000,
#     "JJ":15000,
#     "CCF":12000,
#     "維克多":5000
# }
#
# for key in customs_spending:
#     if customs_spending[key] > 10000:
#         customs_spending[key] = "VIP"
#     else:
#         customs_spending[key] = "一般客戶"
#
# print(customs_spending)


#字典用法

#字典裡面放列表
# student_dic = {
#     "name":["JJ","CCF","AL"],
#     "age":[25,22,19]
# }
#
# print(student_dic["name"][0])
# print(student_dic["age"][2])
#
# #列表裡面放字典
# student_list = [
#     {
#         "name":"JJ",
#         "age":25
#     },
#     {
#         "name":"CCF",
#         "age":22
#     }
# ]
#
# print(student_list[0]["age"])
# print(student_list[1]["name"])

#取得字典裡所有的key、value
# student = {
#     "name":"JJ",
#     "age":25,
#     "sex":"男",
#     "height":171
# }
#
# #列出所有key值  2種寫法一樣
# print(list(student))
# print(list(student.keys()))
#
# #列出所有value值
# print(list(student.values()))


#測驗2  隨機抽一位學生，顯示出他的資料
import random

# students_dic = {
#     "JJ":{
#         "age":25,
#         "height":171,
#         "weight":75
#     },
#     "ccf":{
#         "age":22,
#         "height":183,
#         "weight":65
#     },
#     "AL":{
#         "age":19,
#         "height":165,
#         "weight":65
#     }
# }
#
# #學生的名稱
# students_list = list(students_dic)
# student = students_list[random.randint(0,len(students_list)-1)]
# print(f"你抽到的學生為:{student}")
#
#
# students_info = students_dic[student]
# for info in students_info:
#     if info == "age":
#         print(f"年紀為:{students_info[info]}")
#     elif info == "height":
#         print(f"身高為:{students_info[info]}")
#     elif info == "weight":
#         print(f"體重為:{students_info[info]}")
#



#專案  英文單字練習機
eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

queston_num = int(input("請問總共要練習幾題?"))
eng_list = list(eng_dic)
random_items = random.sample(eng_list, queston_num)
print(random_items)

correct = 0   #答對題數
error = 0     #答錯題數
for i in range(0, queston_num):
    print(f"第{i+1}題:")
    user_input = input(f"請問{random_items[i]}的英文是?")
    if user_input == eng_dic[random_items[i]]:
        print("恭喜答對!")
        correct += 1
    else:
        print(f"答錯了! 正確答案為:{eng_dic[random_items[i]]}")
        error += 1

print(f"總共{queston_num}題。\n答對:{correct}題，答錯:{error}題")

