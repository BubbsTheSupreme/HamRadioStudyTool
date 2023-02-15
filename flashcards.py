from random import shuffle
import sys
import os

def clear():
	size = os.get_terminal_size()
	for i in range(size[1]):
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")


class Flashcards:
	def __init__(self, cards):
		self.cards = cards
		shuffle(self.cards)

	def quiz_all(self):
		grade = 0
		answers = []
		clear()
		for c in self.cards:
			print(f"{c['question']}\n")
			for a in c["answers"]:
				print(a)
			answer = input("> ")
			answers.append(answer)
			clear()
		for a in range(0, (len(answers) - 1)):
			if answers[a].lower() == self.cards[a]["answer"][1].lower():
				grade += 1
		if (grade / len(answers) > 0.85):
			print(f"\033[0:32mScore: {grade}/{len(answers)}")
		else:
			print(f"\033[0:31mScore: {grade}/{len(answers)}")


	def quiz_ten(self):
		questions = self.cards[:10]
		grade = 0
		answers = []
		clear()
		for q in questions:
			print(f"{q['question']}\n")
			for a in q["answers"]:
				print(a)
			answer = input("> ")
			answers.append(answer)
			clear()
		for a in range(0, (len(answers) - 1)):
			if answers[a].lower() == questions[a]["answer"][1].lower():
				grade += 1
		if (grade / len(answers) > 0.85):
			print(f"\033[0:32mScore: {grade}/{len(answers)}")
		else:
			print(f"\033[0:31mScore: {grade}/{len(answers)}")	
