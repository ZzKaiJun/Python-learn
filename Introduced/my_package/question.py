class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

class QuestionGame:
    def __init__(self, questions, score):
        self.questions = questions
        self.score = score

    def play(self):
        for question in self.questions:
            choice = input(question.description)
            if choice == question.answer:
                print("恭喜答對")
                self.score += 1
            else:
                print(f"答錯了。答案為{question.answer}")
