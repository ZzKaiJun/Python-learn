# 猜數字遊戲

# 變數作用域 全域變數、區域變數
#          global  local

# 函式內部更改全域變數

# a = 1
# def abc():
#     # global a
#     a = 2
#     print(f"函式內部:{a}")
# abc()
# print(f"函式外部:{a}")


#迴圈用法  break  continue

# for i in range(1,6):
#     print(i)
#     if i == 3:
#         break
#
# print("跳出迴圈")

# highest = 0
# for score in [10,20,30,23,100,39,100,39,95]:
#     if score == 100:
#         highest = score
#         break
#     if score > highest:
#         highest = score
#
# print(highest)
# print("結束")


#專案  猜數字遊戲
import random

print("歡迎來到猜數字遊戲")
print("謎底為0~100隨機的一個整數 (最多5次猜測機會)")

answer = random.randint(0,100)     #隨機產生0~100間的數字

for i in range(0,5):

    reEnter = True
    while reEnter:
        num = input("請輸入猜測的數字:")
        if num.isdigit():         #判斷字串是否為整數
            reEnter = False
        else:
            print("請輸入整數!")
    num = int(num)

    print(f"第{i+1}次猜測:")
    if num == answer:
        print("恭喜答對!")
        break
    elif num > answer:
        print("小一點")
    else:
        print("大一點")

    if i == 4:
        print(f"已經猜5次，遊戲結束，謎底為:{answer}")
        break

