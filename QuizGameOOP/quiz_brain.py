class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
       return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        persons_answer = input(f"Q.{self.question_number+1} {current_question.text} (True/False)? :")
        self.check_score(persons_answer, current_question.answer)
        self.question_number += 1

    def check_score(self,persons_answer, real_answer):
        if persons_answer.lower() == real_answer.lower():
            self.score += 1
            print("You've got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {real_answer}. Current Score: {self.score}/{self.question_number+1}")
        print("\n")
