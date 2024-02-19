import math

# This is a program that allows the user to access two financial calculators.
# An investment calculator and a home loan repayment calculator.

# The program was designed with ease of use and scalability in mind.
# It aims to allow a wide range of users to access and understand its functionalities.





# Main Menu - Selecting the type of investment

calculations_available = 2

calculation_1 = "Investment"

calculation_2 = "Bond"


print("\nWelcome to the finance calculator!\n")

repeat = True

while repeat == True:
     
    print(f"There are currently {calculations_available} calculation options available:\n\n")

    print(f"{calculation_1} - Calculates the amount of interest you will earn on your investment.\n")

    print(f"{calculation_2} - Calculates the amount you will have to pay on a home loan.\n\n")


    selection = input(f"Please enter either '{calculation_1}' or '{calculation_2}' from the menu above to proceed: \n")


    selection = selection.lower()

    selection = selection.capitalize()




#   Investment - Principal

    if selection == calculation_1:

            print(f"\nLet's calculate your {calculation_1.lower()}.\n")


            valid_principal = False

            while valid_principal == False:

                try:

                    print("Please enter the principal amount:")

                    print("(E.g., the amount you would like to deposit in a savings account.)\n")

                    principal = float(input())

                    print("")

                    if principal != 0:

                        valid_principal = True

                    elif principal == 0:

                        print("If you invest 0, you get 0. Simple.")

                        print("Maybe try something different.\n")


                except ValueError:

                    print("It seems you have entered an invalid amount.\n") 

                    print("Please make sure you type only numbers. No letters or special characters.") 

                    print("For decimal numbers please use '.' as a decimal point instead of ','.\n")



# Investment - Interest rate

            valid_interest_rate = False


            while valid_interest_rate == False:

                    try:
                        print("Please enter the interest rate:")

                        print("(E.g., the interest rate that is offered in a savings account.)\n")

                        interest_rate = float(input())

                        print("")


                        if interest_rate > 0:

                            valid_interest_rate = True


                        elif interest_rate == 0:

                            print("If the interest rate is 0, the initial amount remains the same.")
                            
                            print("Maybe try something different.\n")


                        elif interest_rate < 0:
                             
                            print("\nFor this calculation, the interest rate has to be higher than 0.\n")


                    except ValueError:

                        print("It seems you have entered an invalid amount.\n") 

                        print("Please make sure you type only numbers. No letters or special characters like '%'.")

                        print("For decimal numbers please use '.' as a decimal point instead of ','.\n")



# Investment - Investment period

            valid_years_investing = False


            while valid_years_investing == False:

                    try:
                        print("How many years do you plan on investing for?")

                        print("(Note: This calculator uses full years only. Please enter a whole number.)\n")

                        years_investing = int(input())


                        if years_investing != 0 and years_investing > 0:

                            valid_years_investing = True

                            print("")


                        elif years_investing == 0:

                            print("0 years means right now, so the initial amount remains the same and will not accumulate interest over time.")

                            print("Maybe try something different.\n")

                    
                        elif years_investing < 0:
                        
                            print("It seems you have typed a negative number.\n")

                            print("For this calculation, the number of years has to be greater than 0. At least 1 or higher.\n")


                    except ValueError:

                        print("It seems you have entered an invalid amount.\n") 

                        print("Please make sure you type only whole numbers. No letters or special characters.\n") 



# Investment - Selecting simple or compound interest

            valid_interest = False


            while valid_interest == False:


                        print("Which type of interest would you like to calculate?\n")

                        print("Please enter either 'Simple' or 'Compound' (If unsure, enter 'Help'):\n")

                        interest = input()

                        interest = interest.lower()


# Investment - Simple interest 

                        if interest == "simple":

                            valid_interest = True

                            print(f"\n{interest_rate} %"f" simple interest applied to {principal} over {years_investing} years:\n")


                            interest_rate = interest_rate / 100

                            simple_interest_total = principal *(1 + interest_rate * years_investing)


# Investment - Simple interest: Final result
                            
                            print(simple_interest_total)

                            print("")


# Option - Back to Main Menu

                            try:
                                
                                print("Would you like to do another calculation?\n")

                                another_calculation = str(input("Please enter 'Yes' to continue or 'No' to exit:\n"))

                                another_calculation = another_calculation.lower()

                                print("")


# End Program

                                if another_calculation == "no":
                                    
                                    print("Thank you for using the finance calculator!\n")
                                    
                                    repeat = False
                                    
                                    break


                            except ValueError:
                                
                                print("Sorry, that is not a valid selection.\n")  

                                print("Simply type one of the options given below, then press enter.\n")



# Investment - Compound interest
                                
                        elif interest == "compound":

                            valid_interest = True

                            print(f"\n{interest_rate} %"f" compound interest applied to {principal} over {years_investing} years:\n")

                            interest_rate = interest_rate / 100

                            compound_interest_total = principal * math.pow((1 + interest_rate),years_investing)

# Investment - Compound interest: Final result

                            print(compound_interest_total)

                            print("")


# Option - Back to Main Menu

                            try:
                                
                                print("Would you like to do another calculation?\n")

                                another_calculation = str(input("Please enter 'Yes' to continue or 'No' to exit:\n"))

                                another_calculation = another_calculation.lower()

                                print("")


# End Program

                                if another_calculation == "no":
                                    
                                    print("Thank you for using the finance calculator!\n")

                                    repeat = False
                                    
                                    break


                            except ValueError:
                                
                                print("Sorry, that is not a valid selection.\n")    

                                print("Simply type one of the options given below, then press enter.\n")
                            


# Option - Help: Simple interest and Compound interest

                        elif interest == "help":
                        
                            print("\nSimple interest - As an example, let's imagine we deposit £1000 into a savings account.")
                            print("                  If the account offers 10%"" simple interest, this means that after:\n")
                            print("                  1 year - We will have ---> £1000 (our initial deposit) + £100 (the interest) = £1100\n")
                            print("                  The interest that we receive will always be 10%"" of the initial deposit.")
                            print("                  So, over the years, the balance in our savings account will change as below:\n")
                            print("                  After 1 Year  ---> £1100")
                            print("                  After 2 Years ---> £1200")
                            print("                  After 3 Years ---> £1300\n\n")


                            print("Compound interest - Now, let's imagine we deposit £1000 into a savings account")
                            print("                    and the account offers 10%"" compound interest. This means that after:\n")
                            print("                    1 year - We will have ---> £1000 (our initial deposit) + £100 (the interest) = £1100\n")
                            print("                    So far, after 1 year, the interest we receive is the same as the simple interest.")
                            print("                    But the difference comes after.\n")
                            print("                    The compound interest will be 10%"" of our accumulated amount instead of just the inital deposit.")
                            print("                    This means that on the second year we will now get 10%"" of £1100 = £1210\n")
                            print("                    So, over the years, the balance in our savings account will change as below:\n")
                            print("                    After 1 Year  ---> £1100")
                            print("                    After 2 Years ---> £1210")
                            print("                    After 3 Years ---> £1331\n\n")

                            print("                    We can see below how simple and compound interest will change the balance of our account differently over time:\n")

                            print("                    Years                    Simple                   Compound\n")       
                            print("                      1                       1100                      1100")
                            print("                      2                       1200                      1210")
                            print("                      3                       1300                      1331")
                            print("                      4                       1400                      1464")
                            print("                      5                       1500                      1611")
                            print("                      6                       1600                      1772")
                            print("                      7                       1700                      1949")
                            print("                      8                       1800                      2144")
                            print("                      9                       1900                      2358")
                            print("                     10                       2000                      2594\n\n")


                        else:
                            print("Sorry, that is not a valid selection.\n")    

                            print("To proceed, simply type one of the options given below, then press enter.\n")



# Bond

    if selection == calculation_2:

        try:

            print(f"\nLet's calculate your {calculation_2.lower()}.\n")


# Bond - Property value

            print("What is the current value of the property?")

            house_value = float(input("(Please type a number then press enter): \n\n"))

            print("")

        except ValueError:

            print("It seems you have entered an invalid amount.\n") 

            print("Please make sure you type only numbers. No letters or special characters.\n")

            print("For decimal numbers please use '.' as a decimal point instead of ','.\n")
    

# Bond - Interest rate

        valid_interest_rate = False


        while valid_interest_rate == False:

                try:
                    print("Please enter the interest rate:")

                    print("(E.g., the mortgage interest rate that is offered by your bank.)\n")

                    interest_rate = float(input())

                    print("")


                    if interest_rate > 0:

                            valid_interest_rate = True


                    elif interest_rate == 0:

                            print("If the interest rate is 0, the initial amount remains the same.")
                            
                            print("Maybe try something different.\n")


                    elif interest_rate < 0:
                             
                             print("\nFor this calculation, the interest rate has to be higher than 0.\n")


                except ValueError:
                        
                        print("It seems you have entered an invalid amount.\n") 

                        print("Please make sure you type only numbers. No letters or special characters like '%'.") 

                        print("For decimal numbers please use '.' as a decimal point instead of ','.\n")


# Bond - Repayment period

        print("How long do you plan to take to repay the bond?")

        print("(E.g., the time it will take until you finish paying off your mortgage to the bank.)\n")


        valid_repayment_time = False

        while valid_repayment_time == False:

            try:

                years_of_repayment = int(input("Please enter the amount of years: (you will be asked to enter the months after):\n\n"))

                print("")

            except ValueError:

                print("It seems you have entered an invalid amount.\n") 

                print("Please make sure you type only whole numbers. No letters or special characters.\n") 

            try:
                months_of_repayment = int(input("Please enter the amount of months:\n\n"))

                print("")

            except ValueError:

                print("It seems you have entered an invalid amount.\n") 

                print("Please make sure you type only whole numbers. No letters or special characters.\n")


            if years_of_repayment == 0 and months_of_repayment == 0:

                print("For this calculation, the total repayment time has to be at least month.\n")

            else:
                valid_repayment_time = True

                total_repayment_time = (years_of_repayment * 12) + months_of_repayment

                print("")


# Bond - Finishing

                print(f"\nFor a house currently valued at {house_value} with an interest rate of {interest_rate} %"f"\npaid over {years_of_repayment} years and {months_of_repayment} months, the monthly repayment would be:\n")

                interest_rate = interest_rate / 100

                monthly_repayment = ((interest_rate / 12) * house_value) / (1 - (1 + (interest_rate / 12))**(-total_repayment_time))

                print(monthly_repayment)

                print("")



# Option - Back to Main Menu

                try:
                                
                    print("Would you like to do another calculation?\n")

                    another_calculation = str(input("Please enter 'Yes' to continue or 'No' to exit:\n"))

                    another_calculation = another_calculation.lower()

                    print("")


# End Program

                    if another_calculation == "no":
                        
                        print("Thank you for using the finance calculator!\n")
                        
                        repeat = False
                        
                        break


                except ValueError:
                    
                    print("Sorry, that is not a valid selection.\n")   

                    print("Simply type one of the options given below, then press enter.\n")