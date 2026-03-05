
import random
import time
#variables
#own code idk
#
#
#
#

while True:
	question = input("You: ")
	
	if question.lower() in ["hello", "hi", "hey"]:
		print("Ai:Hello there!")
		
	elif question.lower() in ["bye", "exit", "see ya"]:
		print("Ai:Bye!")
		break
		
	elif question.lower() in ["how are you"]:
		print("Ai:I am fine and you?")
		mood = input("how are you: ")
		
		if mood.lower() in ["good", "i feel good", "i'm good", "i am good", "i am fine", "i'm fine"]:
			print("Ai:Nice!")
		elif mood.lower() in ["bad", "i'm bad", "i am sad", "i feel sad"]:
			print("Ai:Oh, hope you are getting better!")
			
	elif question.lower() in ["i am bored", "i'm bored"]:
		print("Ai:Oh, let's play a game!")
		time.sleep(0.01)
		print("   you need to guess my number")
		time.sleep(0.01)
		print("   it's a number from 1 to 10")
		
		urguess = input("Ai:Your guess: ")
		
		num = random.randint(1, 10)
		print(num)
		
		if urguess == num:
			print("Ai:right!It was", num)
		else:
			print("Ai:wrong, it was: ", num)
			
	elif question.lower() in ["tell me a joke", "joke"]:
		jokes = ["Ai:Why was 6 afraid of 7? beacause seven ate nine, HAHAHAHAHHAH",
		"Ai:what do you call a dog magician?An abracadabrador, AHAHHAHAHAHAHAHAHAH", 
		]
		random_joke = random.choice(jokes)
		print(random_joke)
		
	elif question.lower() in ["ask me something"]:
		print("Ai:Do you like water?")
		water = input("yes/no?: ")
		
		if water == "yes":
			print("Ai:Cool, me too!")
		elif water == "no":
			print("Ai:It's not that bad man")
		else:
			print("Ai:Answer:", water, "not found")
			
	elif question.lower() in ["ty", "thank you", "thx"]:
		print("Ai:No problem")
		
	elif question.lower() in ["who was linus torvalds", "who was linus torvalds?"]:
		print("Ai:Linus Torvalds, was a programmer born in 1969 in helsinki(finland).")
		time.sleep(0.1)
		print("   He showed in a very young age interests in computer and programming.")
		time.sleep(0.1)
		print("   In 1991, while studying at the University of Helsinki,")
		time.sleep(0.1)
		print("   he began developing a new operating system kernel")
		time.sleep(0.1)
		print("   He called it Linux, inspired by his first name and the Unix system.")
		time.sleep(0.1)
		print("   Torvalds released Linux as free and open-source software, ")
		time.sleep(0.1)
		print("   allowing anyone to use and modify it.")
		time.sleep(0.1)
		print("   The project quickly grew, attracting thousands.")
		time.sleep(0.1)
		print("   Today, Linux powers servers, smartphones, and countless")
		time.sleep(0.1)
		print("   devices, making Torvalds one of the most influential figures in computing.")	

	#own code...
	#
	#
	#
	#
	#
	#
	#
	
	else:
		print("Ai:Not found")
		
			
			
