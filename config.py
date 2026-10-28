import json
import os
    
def config_edit(config, config_path):
     
    
    while True:
        print("\nWhat would you like to do?")
        print("1. View current income values")
        print("2. Choose a value to edit")
        print("3. Quit")

        try:
             choice = int(input("\nPlease select a number from the menu: "))
        except ValueError:
             print("That's not a valid input! Use the numbers on the menu.")
        else:

            if choice == 1:
                
                print(config["values"])

            elif choice == 2:

               print(config["values"])

               choose = input("Type the value you wish to edit: ")
                         
               new_value = float(input("Choose the new value you wish to change it to: "))

               config["values"][choose] = new_value

               with open(config_path, "w") as file:

                    json.dump(config, file)
                         
                         
            
            elif choice == 3:
                 break
            
            else:
                 print("That number is not in the menu index, choose a number between 1 and 3.")
    
    return config
