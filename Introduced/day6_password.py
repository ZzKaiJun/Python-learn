#密碼產生器
import health

#While 迴圈
# i = 1
# while i < 6:
#     print("87")
#     i += 1

# name = input("請猜猜我叫什麼名字(2個字)")
# while name != "JJ":
#     print("猜錯了，再猜一次")
#     name = input("請猜猜我叫什麼名字")
# print("恭喜你猜對!")


#測驗1 BMI計算(迴圈)
# height = float(input("請輸入你的身高(cm)"))
# weight = float(input("請輸入你的體重(kg)"))
# bmi = health.get_bmi(height,weight)
# print(f"您的bmi為:{bmi}")
# retry = input("請問你還要再計算嗎? (請輸入y or n)").lower()
# while retry == "y":
#     height = float(input("請輸入你的身高(cm)"))
#     weight = float(input("請輸入你的體重(kg)"))
#     bmi = health.get_bmi(height, weight)
#     print(f"您的bmi為:{bmi}")
#     retry = input("請問你還要再計算嗎? (請輸入y or n)").lower()
# print("計算結束!")


#for 迴圈(循環)  for loop
# for item in "我是JJ":
#     print(item)
# print("程式結束")


# for item in ["小黑","小白","小綠"]:
#     print(item)
# print("程式結束")


# scores = [100, 55, 65, 43, 49, 95, 84]
# sum = 0
# for score in scores:
#     sum += score
# print(f"所有人成績加總為:{sum}")

#測驗2 找出最高成績
# scores_str = input("請輸入學生的成績(中間用,隔開)\n")
# scores = scores_str.split(',')
# max_scores = 0
# for score in scores:
#     if float(score) > max_scores:
#         max_scores = float(score)
#
# print(f"最高分為:{max_scores}")

#range() 函式

# for i in range(1,11):
#     print(i)

# for i in range(1,11,3):
#     print(i)

#測驗3 計算1~100之間，所有偶數整合 (包含100)
# sum=0
# for i in range(0,101,2):
#     sum += i
# print(sum)


#專案  密碼產生器
import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

print("歡迎使用密碼產生器~")
upper_num = int(input("請問需要幾個大寫字母?"))
lower_num = int(input("請問需要幾個小寫字母?"))
numbers_num = int(input("請問需要幾個數字?"))
symbols_num = int(input("請問需要幾個符號?"))

password = ""
for i in range(1,upper_num+1):
    #大寫字母
    num = random.randint(0,len(letters_upper)-1)
    password += letters_upper[num]
print("大寫:"+password)

for i in range(1,lower_num+1):
    #小寫字母
    num = random.randint(0, len(letters_lower)-1)
    password += letters_lower[num]
print("小寫:"+password)

for i in range(1,numbers_num+1):
    #數字
    num = random.randint(0, len(numbers)-1)
    password += numbers[num]
print("數字:"+password)

for i in range(1,symbols_num+1):
    #符號
    num = random.randint(0, len(symbols)-1)
    password += symbols[num]
print("符號:"+password)

print("原本的:" + password)

password_list = list(password)
random.shuffle(password_list)
password_random = ''.join(password_list)
print("打亂後的:" + password_random)

