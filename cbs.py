print("Hello! Welcome to College Budget Simulator! What is your name?")

user_name = str(input())

print("Nice to meet you" + " " + user_name + "!" + " " +
      "What college do you attend?")

college_name = str(input())

print("Ahhh I see!" + " " + college_name + " " + "is a great college!")

print(
    "My goal is to help understand whether you are managing your money correctly."
)

print(
    "How many credits have you completed total? I want to know more about you."
)

classification = {1: "freshman", 2: "sophomore", 3: "junior", 4: "senior"}

class_info = int(input())

if 0 <= class_info <= 29:
  print("Oh a" + " " + classification[1] + "!" + " " + "That's great!")
elif 30 <= class_info <= 59:
  print("Oh a" + " " + classification[2] + "!" + " " + "That's great!")
elif 60 <= class_info <= 89:
  print("Oh a" + " " + classification[3] + "!" + " " + "That's great!")
elif 90 <= class_info <= 120:
  print("Oh a" + " " + classification[4] + "!" + " " + "That's great!")

print("Well get ready for some questions!")

print("What do you like to spend money on?")

spend = str(input())

print("Ok. ok. Good things to spend money on!")

print("This may seem private, but how much is in your bank account? This is essential.")

bank_account = int(input("$"))

print("Do you have a job?")

job_info = str(input())

print("How much do you earn an hour?")

job_info = str(input())

print("What's your form of transportation?")

travel_info = str(input())

print("How many weeks of school do you have left?")

weeks_of_school = str(input())

print("Do you have a phone bill? How much is it a month?")

phone_bill = str(input())

print("How much money do you spend on gas a week?")

gas_money = str(input())



