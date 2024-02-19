# This is a program that calculates the cost of holidays based on input choices from the user.


# Introduction
print("\nWelcome to the holiday planner.\n\nHere you can select a travel package deal tailored to suit your requirements.\n")
print("This week we have these 4 amazing destinations to choose from:\n")

# Flight
while True:

    # Flight - Deals
    print("1 - Lisbon\t\t£76")
    print("2 - Rome\t\t£88")
    print("3 - Istanbul\t\t£128")
    print("4 - Tokyo\t\t£359")
    print()
    print("Please select your destination from the above options:\n(For example: For Lisbon type '1' and press 'enter'.)")

    # Flight - Choice
    try:
        city_flight = int(input())

        if city_flight == 1:
            print("Lisbon, great choice.")
            break
        if city_flight == 2:
            print("Rome, great choice.")
            break
        if city_flight == 3:
            print("Istanbul, great choice.")
            break
        if city_flight == 4:
            print("Tokyo, great choice.")
            break      
        else:
            print("Sorry, that is an invalid selection. Valid selections are 1, 2, 3 or 4.\n")

    except ValueError:
        print("Sorry, that is an invalid selection. Valid selections are 1, 2, 3 or 4.\n")
print()

# Nights
while True:
    print("How many nights would you like to stay at the hotel?")
    print("Our price is £92 per night.\n")
    print("Please type the number of nights then press 'enter'.")
    print("(For example: 2)")

    try:
        num_nights = int(input())
        if num_nights > 0:
            break
        else:
            print("The minimum number of nights to book is 1.\n")
    except ValueError:
        print("Sorry, that is an invalid selection. Please type only whole numbers such as 1 or 2.\n")


# Car Rental
while True:
    print("\nWould you like to rent a car during your stay?")
    print("The price is £25 per day.\n")
    print("Please type 'yes' or 'no' and press 'enter':")

    # Car Rental - Yes or No
    car_or_not = str(input())
    car_or_not = car_or_not.lower()

    if car_or_not == "yes" or car_or_not == "no":
        break
    else:
        print("\nPlease type either 'yes' or 'no' and press 'enter' to proceed.")


if car_or_not == ("yes"):
    while True:
        try:
            # Car Rental - Number of Days
            print("\nHow many days would you like to rent a car for?")
            print("(Please type a number and press 'enter':)")
            rental_days = int(input())
    
            # Checking if the car rental days does not exceed the length of stay to prevent overpaying
            if rental_days > (num_nights + 1):
                    print("\nThe days selected to rent a car exceed the length of your stay.")
                    print(f"You have selected to stay for {num_nights} night/s at the hotel.\n")

            else:
                print("\nGreat!")
                break
                
        except ValueError:
            print("Sorry, that is an invalid selection. Please type only whole numbers such as 1 or 2.\n")

elif car_or_not == ("no"):
    rental_days = 0
    print("\nOk.")

else:
        print("Sorry, that is an invalid selection. Valid selections are 'yes' or 'no'.\n")

print("Let's proceed.\n")
print("Here are the price details of your trip.\n")
    

# Flight Cost Function - Calculate and Print
def plane_cost(city_flight):
    if city_flight == 1:
        flight_cost = 76

    elif city_flight == 2:
        flight_cost = 88

    elif city_flight == 3:
        flight_cost = 128

    elif city_flight == 4:
        flight_cost = 359

    return flight_cost

print("\nFlight cost:")
print(plane_cost(city_flight))


# Hotel Cost Function - Calculate and Print
def hotel_cost(num_nights):
    price_per_night = 92
    total_cost = price_per_night * num_nights

    return total_cost

print("\nHotel cost:")
print(hotel_cost(num_nights))


# Car Rental Cost Function - Calculate and Print
def car_rental(rental_days):
    daily_rental_cost = 25
    total_rental_cost = daily_rental_cost * rental_days

    return total_rental_cost

print("\nCar rental cost:")
print(car_rental(rental_days))


# Total Holiday Cost Function - Calculate and Print
def holiday_cost(hotel, plane, car):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    return hotel + plane + car

print("\nTotal holiday package cost:")
print(holiday_cost(hotel_cost, plane_cost, car_rental))
print()