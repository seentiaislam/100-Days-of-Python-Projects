# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining = 90 - int(age)
months_remaining = round(years_remaining * 12)
weeks_remaining = round(years_remaining * 52)
days_remaining = round(years_remaining * 365)

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")



