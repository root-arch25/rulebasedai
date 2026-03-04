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
		elif mood.lower() in ["bad", "i feel bad", "i'm bad", "i am sad", "i feel sad"]:
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
			
			
	#own code
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
	#...
