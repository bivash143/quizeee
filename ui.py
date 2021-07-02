from tkinter import *
from quiz_brain import QuizBrain
BG_COLOR =  "#375362"

class UserInterface():

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzeee")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.score = Label(text="Score: 0", bg=BG_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=20)

        self.canvas =Canvas(width=300, height=200)
        self.question_text =self.canvas.create_text(150,
                                                    100,
                                                    width=280,
                                                    text="jjasdllads",
                                                    font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        
        self.right_btn_img = PhotoImage(file="./images/right.png")
        self.right_btn = Button(image=self.right_btn_img, highlightthickness=0, command=self.on_rt_click)
        self.right_btn.grid(row=2, column=0, pady=20)

        self.wrong_btn_img = PhotoImage(file="./images/wrong.png")
        self.wrong_btn = Button(image=self.wrong_btn_img, highlightthickness=0, command=self.on_rng_click)
        self.wrong_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop() 


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulation You Hvae Finished Your Quiz")
            self.right_btn.config(state="disable")
            self.wrong_btn.config(state="disable")


    def on_rng_click(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def on_rt_click(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def give_feedback(self, is_right: bool):
        if(is_right):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

