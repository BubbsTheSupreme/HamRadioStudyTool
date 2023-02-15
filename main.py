from flashcards import Flashcards
import json

if __name__ == "__main__":
	with open("questions.json", "r") as f:
		data = json.load(f)
	fc = Flashcards(data)

	fc.quiz_ten()