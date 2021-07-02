import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0
        self.correct_answer: bool

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        self.correct_answer = current_question.answer
        return f"Q.{self.question_no}:  {html.unescape(current_question.question)}"

    def check_answer(self, user_answer: str):
        if(user_answer == self.correct_answer):
            self.score += 1
            return True
        else:
            return False
