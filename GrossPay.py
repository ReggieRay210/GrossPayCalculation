#Calculate Your Hours

#create a variable for the amount of hours the user worked
hours = float(input("Enter total hours worked?: "))

#create a variable for the amount of money per hour the user gets paid 
payrate = float(input("Enter Pay per Hour: ")) 

#calculate the hours times the payrate to get the amount of money the user will get paid
regular_pay = hours * payrate 

#creates a condition that states that if the hours worked is over 40, then calculate the overtime pay
if hours > 40:  
    #get the time and a half and multiply it by the difference of the total hours worked and 40. then add it to the regular pay. 
    ot = ((hours-40) * (payrate * 1.5)) + regular_pay 
    
    # prints the overtime pay
    print("OT Gross Pay:", ot)
    
#if the hours worked did not pass 40 then it is considered regular pay    
else: 
    print("Regular Gross Pay:", regular_pay)
