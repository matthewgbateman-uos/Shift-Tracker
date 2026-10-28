import json
import os

def bills_edit(bill, bill_path, bills):
     
    
    while True:
        print("\nWhat would you like to do?")
        print("1. View total bills")
        print("2. View bills type & amount")
        print("3. Remove a bill")
        print("4. Add a new bill")
        print("5. Quit")

        try:
             choice = int(input("\nPlease select a number from the menu: "))
        except ValueError:
             print("That's not a valid input! Use the numbers on the menu.")
        else:
            if choice == 1:
                print(bills)
            elif choice == 2:
                print(bill["bills"])
            elif choice == 3:
                print(bill["bills"])
                
                choose = input("Type the bill name to remove the bill: ")
                
                bill["bills"].pop(choose)

                with open(bill_path, "w") as file:

                    json.dump(bill, file)
                
                bills = sum(bill["bills"].values())
                
            elif choice == 4:
                  
                name = input("Type the name of bill you wish to add: ")

                try:

                    amount = float(input("Enter the bill amount: "))

                except ValueError:
                     
                    print("That's not a valid input! Please write out the amount in numbers")
                
                else:
                    bill["bills"][name] = amount

                    with open(bill_path, "w") as file:

                          json.dump(bill, file)
                    
                    bills = sum(bill["bills"].values())
                
                    
            
            elif choice == 5:
                 break
            
            else:
                 print("That number is not in the menu index, choose a number between 1 and 5.")
    
    return bills

