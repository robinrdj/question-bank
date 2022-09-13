class Quizbrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score=0
        self.q_list = q_list

    def still_has_questions(self):
        return self.question_no < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (true/false): ?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("u got it right")
            self.score += 1
        else:
            print("u got it wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Ur current score is {self.score}/{self.question_no}")
        print("\n")






