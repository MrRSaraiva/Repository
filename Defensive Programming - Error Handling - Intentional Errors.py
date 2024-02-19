# This program is intended to contain two syntax errors, a runtime error and a logical error

days_left_for_event = 79
total_tickets = 950
tickets_sold = 649
tickets_available = total_tickets - tickets_sold


print("\nWelcome to the online ticket office!")

print("\nThere are " + days_left_for_event + " days left for our next event!")                     # Runtime Error ---> Concatenation - Can't concatenate a string and an integer.                           

print(f"\nThere are {total_tickets} seats in total "and tickets_available" available.")            # Syntax Errors x2 ---> 1. Brackets - Two unnecessary brackets are misplaced in the middle of the print sentence. --- 2. Curly braces missing - tickets_available is not within curly braces which causes the f function not to work.


purchase_complete = False

while purchase_complete == False:

    try:
        tickets_purchased = int(input("\nPlease enter the number of tickets to purchase: "))


        if tickets_purchased >= 1 and tickets_purchased <= tickets_available and tickets_purchased != 0:
            
            purchase_complete = True
                                                                                                                         
            tickets_sold = tickets_sold + tickets_purchased                                                       

            print(f"\nYou have purchased {tickets_purchased} ticket/s! Thank you and enjoy the show!\n")        

            if tickets_available == 0:
                print("We are sold out!")
                break

            print(f"There are now {tickets_available} tickets available.")                  # Logical Error ---> tickets_available value is not changing after purchase_complete is True. The variable is not including the input value in its calculations.


        elif tickets_purchased <= 0:
            print("\nSorry, you have entered an incorrect value.")


        else: print(f"\nSorry... Unfortunately there are only {tickets_available} tickets available at the moment.")


    except: ValueError (print("\nSorry, you have entered an incorrect value."))