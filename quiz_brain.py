import random


class DisplayQuestions:

    def __init__(self, questions, correct_answers, incorrect_answer):
        self.question_and_answers = []
        self.choices = []
        self.randomized_choices = []
        self.questions = questions
        self.correct_answers = correct_answers
        self.incorrect_answer = incorrect_answer
        self.total_answered = 0
        self.total_correct = 0
        self.total_wrong = 0
        self.question_number = 0

    def questions_and_answers(self):
        while self.question_number < len(self.questions):
            self.question_and_answers.append(self.questions[self.question_number])
            self.question_and_answers.append(self.correct_answers[self.question_number])
            for x in self.incorrect_answer[self.question_number]:
                self.question_and_answers.append(x)
            self.display_questions_and_answers()
            self.question_and_answers.clear()
            self.question_number += 1

    def display_questions_and_answers(self):
        print(f"Total question: {len(self.questions)} Correct: {self.total_correct} Wrong: {self.total_wrong}")
        print(self.question_and_answers[0])
        i = 0
        for e in self.question_and_answers[1:]:
            self.choices.append(e)
            i += 1
        random.shuffle(self.choices)
        i = 0
        for e in self.choices:
            self.randomized_choices.append(chr(97 + i)+". "+e)
            i += 1
        i = 0
        for e in self.randomized_choices:
            print(e)
        i += 1
        x = input("Answer: ").lower()
        self.check_answer(x)
        self.choices.clear()
        self.randomized_choices.clear()
        self.total_answered += 1

    def check_answer(self, answer):
        a_list = ["a", "b", "c", "d"]
        if answer not in a_list:
            print("Invalid answer")
            self.question_number -= 1
            self.total_answered -= 1
        else:
            for e in self.randomized_choices:
                if e[0] == answer:
                    if e[3:] == self.correct_answers[self.total_answered]:
                        self.total_correct += 1
                        print("Correct!")
                    else:
                        self.total_wrong += 1
                        print(f"Wrong. The correct answer: {self.correct_answers[self.total_answered]}")

