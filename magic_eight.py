answer = ""

while answer != "quit":
	answer = input("What is your question?")
	if answer == "quit":
		break
	elif answer[-1] == "?":
		pass
	else:
		print("I'm sorry, I can only answer questions.")
