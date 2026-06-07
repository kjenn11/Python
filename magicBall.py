import random
# This is a Magic 8-Ball program that gives random answers to questions.

# User input for name and question
name = input("What is your name? ")
question = input("What is your question? ")

# Generate a random number between 1 and 9 to determine the answer
answer = ""
random_number = random.randint(1, 9)
if random_number == 1:
 answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
  
 # Print the question and the answer 
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
