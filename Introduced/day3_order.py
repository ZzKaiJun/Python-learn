#if else
# score = 40
# if score > 60:
#     print("今天準備吃好料!")
# else:
#     print("今天準備罰跪!")
#
# name = "林鮭魚"
# if name == "林鮭魚":
#     print("鮭魚吃到飽!")
# else:
#     print("得付錢!")

#test  判斷輸入的整數是奇數還是偶數
"""
num = input("請輸入一個整數:\n")
print(int(num)%2)

if int(num)%2 > 0:
    print(f"{num}為奇數!")
else:
    print(f"{num}為偶數!")
"""

#if elif

# score = 50
# if score > 90:
#     print("我給你100元!")
# elif score > 80:
#     print("我給你70元!")
# elif score > 70:
#     print("我給你30元!")
# else:
#     print("你給我100元!")

#BMI計算器改良
# height = float(input("請輸入您的身高(cm):\n"))
# weight = float(input("請輸入您的體重(kg):\n"))
#
# height = height/100
# BMI = round(weight / (height**2),1)
#
# if BMI < 18.5:
#     print(f"您的BMI為:{BMI}，屬於體重過輕")
# elif 18.5 <= BMI < 24:
#     print(f"您的BMI為:{BMI}，屬於正常體位")
# elif 24 <= BMI < 27:
#     print(f"您的BMI為:{BMI}，屬於體重過重")
# elif 27 <= BMI < 30:
#     print(f"您的BMI為:{BMI}，屬於輕度肥胖")
# elif 30 <= BMI < 35:
#     print(f"您的BMI為:{BMI}，屬於中度肥胖")
# else:
#     print(f"您的BMI為:{BMI}，屬於重度肥胖")

#專案 拉麵點餐系統
print("歡迎使用拉麵點餐系統。")
print("(1)鹽味拉麵 $220")
print("(2)醬油拉麵 $240")
print("(3)豚骨拉麵 $280")
noodle_type = int(input("請選擇拉麵口味 (輸入:1 or 2 or 3)"))
is_Big = input("是否加大，豚骨口味:+50元; 其他口味:+30元 (輸入:Y or N)").upper()  #upper:字串中的英文轉換成大寫   lower:轉換成小寫
is_egg = input("是否加糖心蛋:+30元 (輸入:Y or N)").upper()                     #upper:字串中的英文轉換成大寫   lower:轉換成小寫
is_pork = input("是否加叉燒:+60元 (輸入:Y or N)").upper()                      #upper:字串中的英文轉換成大寫   lower:轉換成小寫

if is_Big == "Y" and  is_egg == "Y" and is_pork == "Y":
    is_Discount = True              #全部加滿有折扣20元
else:
    is_Discount = False             #沒有折扣

SUM=0

if noodle_type == 1:
    #鹽味拉麵
    SUM = 220

    #是否加大
    if is_Big == "Y":
        SUM = SUM + 30

elif noodle_type == 2:
    #醬油拉麵
    SUM = 240

    # 是否加大
    if is_Big == "Y":
        SUM = SUM + 30
elif noodle_type == 3:
    #豚骨拉麵
    SUM = 280

    # 是否加大
    if is_Big == "Y":
        SUM = SUM + 50
else:
    SUM = 0

if SUM == 0:
    print("輸入錯誤!請輸入1~3")
else:
    if is_egg == "Y":
        SUM = SUM + 30
    if is_pork == "Y":
        SUM = SUM + 60
    if is_Discount == True:
        SUM = SUM-20
        print(f"加好加滿折扣價$20，總金額為${SUM}，祝您用餐愉快!")
    else:
        print(f"總金額為${SUM}，祝您用餐愉快!")