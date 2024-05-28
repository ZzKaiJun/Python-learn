#測驗 計算機功能
#將第一個數和第二個數加起來
"""
number = str(input("請輸入一個兩位數:"))
Num1 = number[0]
Num2 = number[1]

print(type(Num1))
print(type(Num2))

print(int(Num1) + int(Num2))
"""
#字串用法
"""
print("我今年\"25\"歲")     #字串加入 ""
print("我是jj\n我今年25歲")  #字串中換行
input("請輸入你的身高\n")
"""

#f-string 字串裡直接使用其他資料型態
"""
name = "JJ"
age = 25
is_male = True

print("大家好我是"+str(name)+"，我今年"+str(age)+"歲，是否為男性:"+str(is_male))
print(f"大家好我是{name}，我今年{age}歲，是否為男性:{is_male}")
"""

#運算符號、數字用法  ctrl+/ 快速註解
# print(7//3)
# print(2**3)
# print(7%3)
# round(1.3333,2)  #四捨五入

#專案 bmi計算機  輸入身高(cm)、體重，計算出BMI (小數點取1位)
height = input("請輸入您的身高(cm):\n")
weight = input("請輸入您的體重(kg):\n")

height = height/100

bmi = round(float(weight)/(float(height)**2),1)
print(f"您的BMI為:{bmi}")

