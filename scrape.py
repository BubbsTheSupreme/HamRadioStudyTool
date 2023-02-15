from bs4 import BeautifulSoup
import httpx
import json



resp = httpx.get("https://hamexam.org/view_pool/18-Technician")

flashcards = []

if resp.status_code == 200:
	soup = BeautifulSoup(resp.text, "html.parser")
	questions = soup.find_all("div", class_="question")
	for q in questions:
		answer = q.find("span", class_="correctAnswerLetter")
		question = q.find("p", class_="questionText")
		answers = q.find_all("span", class_="noMarks")
		cur_answers = []
		for a in answers:
			cur_answers.append(a.text)
		card = {
			"answer": answer.text,
			"question": question.text,
			"answers": cur_answers
		}
		flashcards.append(card)
	with open("questions.json", "w") as jsf:
		json.dump(flashcards, jsf, indent=4)
	figures = ["https://hamexam.org/images/figures/T2022/T1.jpg", "https://hamexam.org/images/figures/T2022/T2.jpg", "https://hamexam.org/images/figures/T2022/T3.jpg"]
	for f in figures:
		resp = httpx.get(f)
		with open(str(resp.url).split("/")[-1], "wb") as f:
			f.write(resp.content)
else:
	print(f"HTTP Status Code{resp.status_code}")
