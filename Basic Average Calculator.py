#       Continuously request user to enter a number
#       When the user enters "-1", stop requesting input and display the average of the numbers entered except the "-1"


number = int(input("Please enter a number: "))
entries = 0
sum = 0

while number != -1:
    entries += 1
    sum += number
    number = int(input("Please enter a number: "))
    
    if number == -1:
        average = (sum / entries)
        print(average)