#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill=input("What was the total bill?")
total_bill_as_float=float(total_bill)
give_bill=input("How much tip would like to give? 10, 12, or 15?")
give_bill_int=int(give_bill)
total_bill_as_float+=(total_bill_as_float*give_bill_int/100)
bill=input("How many people to split the bill?")
bill_int=int(bill)
total_bill_as_float/=bill_int
final_amount=round(total_bill_as_float,2)
final_amount="{:.2f}".format(total_bill_as_float)
print(f"Each person should pay: ${final_amount}")