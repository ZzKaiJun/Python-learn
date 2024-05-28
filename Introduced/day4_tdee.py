#函式(函數) function
# def print_info():
#     print("大家好我是jj")
#     print("今年26歲")
# print_info()

# def print_info(name,age,height):
#     print(f"大家好我是{name}")
#     print(f"今年{age}歲，身高{height}")
# print_info("jj",27,171)
# print_info(name = "jj",height= 171,age = 27)


#測驗  寫個函式，能找出3個數中最大的那個並顯示出來
# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         print(num1)
#     elif num2 >= num1 and num2 >= num3:
#         print(num2)
#     elif num3 >= num1 and num3 >= num2:
#         print(num3)
#
# find_max(20,50,30)

# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     elif num3 >= num1 and num3 >= num2:
#         return num3
#
# max = find_max(20,50,30)
# print(max)

def find_max(num1, num2, num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數!"
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

def find_min(num1, num2, num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數!"
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    elif num3 <= num1 and num3 <= num2:
        return num3
#
# max = find_max("你好",20,50)
# print(max)

#測驗2 寫函式會把最大數字-最小數字回傳

def max_min(num1,num2,num3):
    #結合之前做的find_max、find_min
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數!"
    return find_max(num1,num2,num3) - find_min(num1,num2,num3)

# num = max_min(40,20,54)
# print(num)


#專案 綜合健康計算機 (BMI BMR TDEE)

#bmi計算function
def get_bmi(height,weight):
    height = height/100
    bmi = weight/height**2
    bmi = round(bmi,1)
    return bmi

#bmr計算function
def get_bmr(sex,height,weight,age):
    if sex == "男":
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
        bmr = round(bmr, 2)
        return bmr
    else:
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
        bmr = round(bmr, 2)
        return bmr

#tdee計算function
def get_tdee(sex,height,weight,age,times):
    if sex == "男":
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
        bmr = round(bmr, 2)
    else:
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
        bmr = round(bmr, 2)

    if times == 1:
        tdee = bmr * 1.2
    elif times == 2:
        tdee = bmr * 1.375
    elif times == 3:
        tdee = bmr * 1.55
    elif times == 4:
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9
    tdee = round(tdee, 2)
    return tdee

print("歡迎使用綜合健康計算機!")
print("(1)計算BMI")
print("(2)計算基礎代謝率(BMR)")
print("(3)計算總熱量消耗(TDEE)")

type = input("請選擇要計算的項目 (輸入1 or 2 or 3)")
if type == "1":
    height = float(input("請輸入身高(cm)"))
    weight = float(input("請輸入體重(kg)"))
    bmi = get_bmi(height, weight)
    print(f"您的BMI為:{bmi}")
elif type == "2":
    sex = input("請輸入性別 (男or女)")
    height = float(input("請輸入身高(cm)"))
    weight = float(input("請輸入體重(kg)"))
    age = float(input("請輸入年齡"))
    bmr = get_bmr(sex, height, weight, age)
    print(f"您的基礎代謝率(BMR)為:{bmr}")
elif type == "3":
    sex = input("請輸入性別 (男or女)")
    height = float(input("請輸入身高(cm)"))
    weight = float(input("請輸入體重(kg)"))
    age = float(input("請輸入年齡"))

    print("(1)久坐、幾乎沒運動")
    print("(2)每周低強度運動1~3天")
    print("(3)每周中強度運動3~5天")
    print("(4)每周中強度運動6~7天")
    print("(5)勞力密集工作或是每天高強度運動訓練")
    times = float(input("請輸入運動量 (輸入1~5)"))
    tdee = get_tdee(sex, height, weight, age, times)
    print(f"您的每日總消耗熱量(TDEE)為:{tdee}")

