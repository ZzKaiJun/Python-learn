#剪刀石頭布 遊戲 paper scissor stone

#引入模組
# import health
# print(health.get_bmi(171,80))

#random模組
#https://docs.python.org/zh-cn/3/library/random.html
import random

# print(random.randint(1,100))
#
# #回傳0-0.99999間的一個數
# num = random.random()
# print(num)
# #回傳0-9.99999間的一個數
# num = random.random()
# print(num*10)


#測驗1  擲硬幣程式
# if random.randint(0,1) == 0:
#     print("正面")
# else:
#     print("反面")


#列表 list

# scores = [80, 50 ,60 ,35, 68, 32]
# print(scores[1])
# print(scores[-1])
#
# scores.append(50)
# print(scores.count(50))

#測驗2  今晚吃什麼
# dinner = ["滷肉飯", "咖哩飯", "牛肉麵", "漢堡", "叉燒", "拉麵"]
# num = random.randint(1,len(dinner))
# print(dinner[num-1])

#進階版
# print("歡迎使用今晚吃什麼")
# food_str = input("請輸入晚餐選項 (中間請用, 隔開)\n")   #字串型態，需要轉換成列表
# food = food_str.split(',')  #分割字串
#
# num = random.randint(1,len(food))
# print(food[num-1])

#巢狀列表  nested list
# nums = [
#     [1,2,3] ,
#     [4,5,6] ,
#     [7,8,9]
# ]
# print(nums[0][1])


#專案5 s剪刀 r石頭 p布
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

player = input("請輸入字母: s(剪刀) r(石頭) p(布)")
srp = ["s" , "r", "p"]
computer = srp[random.randint(0,2)]
result = ""

if player == "s":
    print(f"你出:\n{scissor}")
    if computer == "s":
        print(f"電腦出:\n{scissor}")
        result = "平手"
        print(result)
    elif computer == "r":
        print(f"電腦出:\n{rock}")
        result = "你輸了"
        print(result)
    else:
        print(f"電腦出:\n{paper}")
        result = "你贏了"
        print(result)

elif player == "r":
    print(f"你出:\n{rock}")
    if computer == "s":
        print(f"電腦出:\n{scissor}")
        result = "你贏了"
        print(result)
    elif computer == "r":
        print(f"電腦出:\n{rock}")
        result = "平手"
        print(result)
    else:
        print(f"電腦出:\n{paper}")
        result = "你輸了"
        print(result)
else:
    print(f"你出:\n{paper}")
    if computer == "s":
        print(f"電腦出:\n{scissor}")
        result = "你輸了"
        print(result)
    elif computer == "r":
        print(f"電腦出:\n{rock}")
        result = "你贏了"
        print(result)
    else:
        print(f"電腦出:\n{paper}")
        result = "平手"
        print(result)
