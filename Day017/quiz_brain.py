from question_model import Question
from data import question_data

class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_ques.text} (True/False): ")
        self.check_answer(user_answer, current_ques.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("This is correct answer.")
        else:
            print("Your answer is wrong")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")