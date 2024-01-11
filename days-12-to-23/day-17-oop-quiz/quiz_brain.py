class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def run_quiz(self):
        question_list_length = len(self.question_list)
        while self.question_number < question_list_length:
            self.next_question()
        score_percent = round(self.score / 12 * 100, 2)
        print(f"That was the last question, you got: {self.score} out of 12 correct. Final score is: {score_percent}%")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower().strip() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect...")