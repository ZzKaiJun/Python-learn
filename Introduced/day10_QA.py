#問答程式

#類別 class   物件 object
#如果要顯示手機的資料，只靠單一種資料型態難以表示

#phone1就是一個物件，他是根據Phone這個類別創建出來的
# class Phone:
#     pass
#
# phone1 = Phone()
# phone1.number = "123"
# phone1.price = 8000
# phone1.waterproof = True
# print(phone1)
# print(phone1.number)
#
# phone2 = Phone()
# phone1.number = "456"
# phone1.price = 16200
# phone1.waterproof = False

#屬性 attribute
#初始函式  __init__   每當物件被創建,就會呼叫初始函式
#類別裡面的函式  method:方法
# class Phone():
#     def __init__(self, number, price, waterproof, power):
#         self.number = number
#         self.price = price
#         self.waterproof = waterproof
#         self.power = power
#
#     def play(self, consume):
#         self.power -= consume
#         if self.power < 0:
#             self.power = 0
#
# phone1 = Phone("123",8000,True, 80)
# print(f"phone1原先電量:{phone1.power}")
# phone1.play(90)
# print(f"phone2後來電量:{phone1.power}")
#
#
#
# phone2 = Phone("456",5000,False, 60)
# print(f"phone2原先電量:{phone2.power}")
# phone2.play(20)
# print(f"phone2後來電量:{phone2.power}")



#測驗1

#創建一個class Question
#有兩個屬性  description   answer
#有一個方法 ask  印出問題並取得輸入，答對回傳True;答錯回傳False

# class Question():
#     def __init__(self, description, answer):
#         self.description = description
#         self.answer = answer
#
#     def ask(self):
#         choice = input(self.description)
#         if choice == self.answer:
#             print("恭喜答對!")
#         else:
#             print(f"答錯了!正確答案是{self.answer}")
#
#
# question = Question("請問2+4等於?\n(a)5\n(b)6\n(c)7\n","b")
# question.ask()



#測驗2
#創建一個 QuestionGame
#有兩個屬性 questions  score
#有一個方法 play 可以印出所有問題並取得輸入，最後印出答對多少題

# class Question:
#     def __init__(self, description, answer):
#         self.description = description
#         self.answer = answer
#
# class QuestionGame:
#     def __init__(self, questions, score):
#         self.questions = questions
#         self.score = score
#
#     def play(self):
#         for question in self.questions:
#             choice = input(question.description)
#             if choice == question.answer:
#                 print("恭喜答對")
#                 self.score += 1
#             else:
#                 print(f"答錯了。答案為{question.answer}")
#
#
# question1 = Question("請問1+1等於?\n(a)1\n(b)2\n(c)3\n","b")
# question2 = Question("請問2+2等於?\n(a)2\n(b)3\n(c)4\n","c")
# question3 = Question("請問3+2等於?\n(a)5\n(b)6\n(c)7\n","a")
# Questions = [question1, question2, question3]
# Question_Game = QuestionGame(Questions,0)
# Question_Game.play()
# print(f"總共答對{Question_Game.score}")


#專案
# QuestionGame 增加一個方法 random_pick 可以傳入要隨機挑選幾題
# 修改play方法  隨機挑5題讓使用者回答
# 完成問答程式
import random
import json
class Question:
    def __init__(self , description , answer):
        self.description = description
        self.answer = answer

    def ask(self):
        choice = input(self.description)
        if choice == self.answer:
            return True
        else:
            return False

class QuestionGame:
    def __init__(self, question):
        self.questions = question
        self.score = 0

    def play(self):
        self.score = 0  #初始化分數
        for question in self.questions:
            choice = input(question.description)
            if choice == question.answer:
                print("恭喜答對!")
                self.score += 1
            else:
                print(f"答錯了，正確答案為:{question.answer}")

        print(f"總共答對{self.score}題")

    def random_pick(self):
        question_num = int(input("請問要回答幾題 (最多10題)"))
        if question_num > 10:
            question_num = 10
        random_question_list = random.sample(self.questions,question_num)

        self.score = 0  # 初始化分數
        for question in random_question_list:
            choice = input(question.description)
            if choice == question.answer:
                print("恭喜答對!")
                self.score += 1
            else:
                print(f"答錯了，正確答案為:{question.answer}")

        print(f"總共答對{self.score}題")


#用open的方式讀取資料
list = []
with open("questions.json", "r", encoding="utf-8") as f:
    list = json.loads(f.read())

question_list = [
  {
    "description": "請問1+1=?\n(a)2\n(b)3\n(c)4\n",
    "answer": "a"
  },
  {
    "description": "請問2+2=?\n(a)2\n(b)3\n(c)4\n",
    "answer": "c"
  },
  {
    "description": "請問4+4=?\n(a)7\n(b)8\n(c)9\n",
    "answer": "b"
  },
  {
    "description": "請問1公尺=幾公分?\n(a)1\n(b)10\n(c)100\n",
    "answer": "c"
  },
  {
    "description": "請問1公斤=幾公克?\n(a)100\n(b)1000\n(c)10000\n",
    "answer": "b"
  },
  {
    "description": "請問1年有幾天?\n(a)365\n(b)1000\n(c)10000\n",
    "answer": "a"
  },
  {
    "description": "請問小白帥嗎?\n(a)帥爆\n(b)還好\n(c)醜死了\n",
    "answer": "a"
  },
  {
    "description": "請問蛋的英文是?\n(a)apple\n(b)dog\n(c)egg\n",
    "answer": "c"
  },
  {
    "description": "請問貓的英文是?\n(a)egg\n(b)cat\n(c)dog\n",
    "answer": "b"
  },
  {
    "description": "請問狗的英文是?\n(a)apple\n(b)banana\n(c)dog\n",
    "answer": "c"
  }
]
print(list == question_list)


#此為正確的建立方法
questions = []
for question in question_list:
    des = question["description"]
    ans = question["answer"]
    q = Question(des , ans)
    questions.append(q)
Question_Game = QuestionGame(questions)

#偷懶的方法
# Question_Game = QuestionGame(question_list)


# Question_Game.play()
Question_Game.random_pick()














