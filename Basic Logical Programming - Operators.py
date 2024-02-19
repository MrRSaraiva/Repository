
#   This is a program that determines the reward a person competing in a triathlon will receive based on their performance

#   The program was created according to the information from the "Competition Award Details" file.




#   Request input times from the user (in minutes) for: swimming, cycling and running

swimming = int(input("How many minutes did it take you to finish the swimming?: "))

cycling = int(input("How many minutes did it take you to finish the cycling?: "))

running = int(input("How many minutes did it take you to finish the running?: "))



#   Sum all 3 inputs for the total time of the triathlon

total_time = int(swimming + cycling + running)
print(("It took you {} minutes to finish the triathlon.").format(total_time))



#   Write conditions for all of the following total time ranges: 0-100 , 101-105 , 106-110 , 111+

if (total_time > 0) and (total_time <= 100):
    print("Congratulations! You have finished within the qualifying time.\nYou were awarded with:\nProvincial Colours!")

elif (total_time > 100) and (total_time <= 105):
    print("You have finished within 5 minutes of the qualifying time. \nYou were awarded with:\nProvincial Half Colours!")

elif (total_time > 105) and (total_time <= 110):
    print("You have finished within 10 minutes of the qualifying time. \nYou were awarded with:\nProvincial Scroll!")

elif (total_time > 111):
    print("You have finished with more than 10 minutes off the qualifying time. \nYou didn't receive an award. Better luck next time!")