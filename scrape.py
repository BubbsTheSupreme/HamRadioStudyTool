from selectolax.parser import HTMLParser
# import database
import httpx


resp = httpx.get("https://hamexam.org/view_pool/18-Technician")

if resp.status_code == 200:
	question_div = []
	parse = HTMLParser(resp.text)
	content_divs = parse.css("div.content")
	content_divs.pop(0)
	for div in content_divs:
		node = div.css("h2")
		if node != []:
			question_div.append(div)
	for div in question_div:
		cards = div.css("div")
		for card in cards:
			qa = card.css("div p")
			answers = card.css("div li")
			print(qa)
			# for a, q in qa:
			# 	print(a)
			# 	print(q)
				# a = entry.css("span")
				# q = ""
				# if a != []:
				# 	a = a[0].text()
				# else:
				# 	q = entry.text()
				# for answer in answers:
				# 	ans_text = answer.css("span")[0]
				# 	print(f"{ans_text.text()} \n")

		
else:
	print(f"HTTP Status Code{resp.statuscode}")
	
#debugging commented section