# Branching assignment for predicting cost of electricity

rate1 = 0.07633
rate2 = 0.09259
kw_hours_used = int(input("Please enter the number of KW hours you have used: \n"))

if(kw_hours_used >= 0):
    if(kw_hours_used <= 1000):
        print("Your monthly bill will be $", (kw_hours_used * rate1), sep = "")
    if(kw_hours_used > 1000):
        print(f"Your monthly bill will be $", (1000 * rate1 + (kw_hours_used - 1000) * rate2), sep = "")
else:
    kw_hours_used = int(input("Please enter a number greater than or equal to 0: \n"))

    if (kw_hours_used >= 0):
        if (kw_hours_used <= 1000):
            print("Your monthly bill will be $", (kw_hours_used * rate1), sep="")
        if (kw_hours_used > 1000):
            print(f"Your monthly bill will be $", (1000 * rate1 + (kw_hours_used - 1000) * rate2), sep="")
    else:
        print("ERROR:Incompetent user detected \n")
        print("Goodbye")
