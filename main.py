from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("U have completed the quiz")
print(f"Ur total score is {quiz.score}/{len(question_bank)}")
