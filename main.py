#! /usr/bin/python3
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface

question_bank = [Question(x["question"], x["correct_answer"])
                for x in question_data]

quiz = QuizBrain(question_bank)
quiz_ui = UserInterface(quiz)

print("You have completed the Quiz")
print(f"Yout final score was {quiz.score}/{quiz.question_no}")
