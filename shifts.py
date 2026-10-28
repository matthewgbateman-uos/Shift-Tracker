import json
import calculations as c

def shift_update(data, file_path, bills):

    # Ask user for number of hours done this month.
    try:
        hours = float(input("How many hours did you do on your shift today? \n"))
    
    except ValueError:
        print("That's not a valid input!")

    data["shifts"].append(hours)

    with open(file_path, "w") as file:
        json.dump(data, file)

    hours_earned = sum(data["shifts"])
    
    try:
        holiday = float(input("How many days of holiday have you had this month?\n"))
    
    except ValueError:
            print("That's not a valid input!")
    
    lower, upper = c.pay_calc(hours_earned, holiday)

    # Return potential earnings.

    print(f"\nYou have done: {hours_earned} hours this month.")

    print(f"\nYou have earned between: \n\n £{lower:.2f} -> £{upper:.2f}")

    print(f"\nAfter bills you will have remaining between: \n\n £{lower - bills:.2f} -> £{upper - bills:.2f}\n")

    return

def shift_current(data, bills):

    hours_earned = sum(data["shifts"])

    try:
        holiday = float(input("How many days of holiday have you had this month?\n"))
    
    except ValueError:
            print("That's not a valid input!")

    lower, upper = c.pay_calc(hours_earned, holiday)

    print(f"\nYou have done {hours_earned} hours. \n\nYou have earned between:\n\n£{lower:.2f} -> £{upper:.2f}\n")

    print(f"After bills you will have remaining between:\n\n£{lower - bills:.2f} -> £{upper - bills:.2f}\n")

    return

def shift_calc(bills):

    try:
        hours = float(input("\nHow many hours? "))

    except ValueError:
            print("That's not a valid input!")

    try:
        holiday = float(input("\nHow many days of holiday? "))

    except ValueError:
            print("That's not a valid input!")

    lower, upper = c.pay_calc(hours,holiday)

    print(f"\nWith: {hours} hours and {holiday*7} hours holiday.\n\nYou will have earned between:\n\n £{lower:.2f} -> £{upper:.2f}\n")

    print(f"After bills you will have remaining between: \n\n£{lower - bills:.2f} -> £{upper - bills:.2f}\n")

    return

def shift_edit(data, file_path):

    print(data)

    try:
        question_remove = int(input(f"Please put in the index number you wish to remove: 0 - {len(data['shifts'])-1}"))
    
    except ValueError:
            print("That's not a valid input!")

    data["shifts"].pop(question_remove)
    
    print(data)
    
    with open(file_path, "w") as file:  
        
        json.dump(data, file)    
    
    return

def shift_reset(data, file_path):
     
    data["shifts"] = []

    with open(file_path, "w") as file:

        json.dump(data,file)    
