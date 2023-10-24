print("Hello! Welcome to College Budget Simulator! What is your name?")

user_name = str(input())

print("Nice to meet you" + " " + user_name + "!" + " " +
      "What college do you attend?")

college_name = str(input())

print("Ahhh I see!" + " " + college_name + " " + "is a great college!")

print("My goal is to help understand whether you are managing your money correctly.")

print("How many credits have you completed total? I want to know more about you.")

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
print("On average, there are about 15 weeks of school.")
print("Therfore, I'm going to multiply your data by 15.")

#preferences
print("What do you like to spend money on?")

spend = str(input())

print("Ok. ok. Good things to spend money on!")

print("This may seem private, but how much is in your bank account? This is essential.")

print("This will tell me how well you will start this journey.")

print("Trust me. I can be your best friend. Go ahead. Type away!")

#job pay
bank_account = int(input("$"))

print("Do you have a job?")

job_info = str(input())

if (job_info == "Yes" or "yes"):
  print("How much do you earn an hour?")
  job_hourly_rate = int(input())
  
  print("How many hours do you work?")
  hour_amount = int(input())

  daily_pay = (job_hourly_rate * hour_amount)

  print("This is your daily pay: $" + daily_pay)
  
  print("Typically how many days do you work this job a week?")

  day_info = int(input())

  total_pay = daily_pay * day_info

  print("This is your total pay: $" + str(total_pay))

  print("Updated balance:")

#travel pay
print("Do you have to pay transportation?")

travel_info = str(input())

if(travel_info == "Yes" or "yes"):
  print("How much money do you spend on transportation a week?")
  trans_pay = int(input())
else:
  print("Not paying for gas sounds great!")

#financial info
print("Are you financially cleared? Yes or no?")

cleared_info = str(input())

if(cleared_info == "No" or "no"):
  print("How much money do you pay each month?")
else:
  print("Great to hear you're financially cleared!")

#phone info
print("Do you have a phone bill?")

phone_info = str(input())

if(phone_info == "Yes" or "yes"):
  print(" How much is it a month?")
  phone_bill = str(input())
else:
  print("Not paying for phone bills sounds great!")

#subscriptions
print("How much money do you spend on subscriptions a month?")

sub_money = int(input())

print(bank_account - sub_money)

#activities
print("How much money do you spend on activites(parties, going out, etc.) each week?")

active_money = int(input())

print(bank_account - active_money)

#groceries
print("How much money do you spend on groceries each week?")

groceries_money = int(input())

print(bank_account - groceries_money)

#books
print("How much money do you spend on books for the semester?")

book_money = int(input())

print(bank_account - book_money)

#clothing
print("How much money do you spend on clothing each month?")
clothing_money = int(input())

print(bank_account - clothing_money)