# Day 17/100 - The Quiz Project with (OOP)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = question["question"]
    a = question["answer"]
    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.run_quiz()
