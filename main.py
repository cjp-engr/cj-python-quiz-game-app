from data import question_data
from quiz_brain import DisplayQuestions

questions = []
correct_answers = []
incorrect_answers = []

for question in question_data:
    available_question = question["question"]
    correct_answer = question["correct_answer"]
    incorrect_answer = question["incorrect_answers"]
    questions.append(available_question)
    correct_answers.append(correct_answer)
    incorrect_answers.append(incorrect_answer)


quiz = DisplayQuestions(questions, correct_answers, incorrect_answers)
quiz.questions_and_answers()




