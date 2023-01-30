#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 15, or 20?"))
people = int(input("How many people are splitting the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
#format to round final amount to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")