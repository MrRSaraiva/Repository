# This is a program intended to contain a logical error


event_venue = "Coliseum of Dreams"
event_date = "Sunday, the 31st of March at 11:59pm"
total_tickets = 950
tickets_available = 351
double_tickets = 47
single_tickets = tickets_available - double_tickets

print("\nWelcome to the Grand Opera Nights!\n")

print(f"Our next great event is on {event_date} at the {event_venue}. The venue has a {total_tickets} seating capacity of which {tickets_available} are still available. \n")

print(f"There are {single_tickets} single tickets and {double_tickets} double tickets available. The double ticket option offers two tickets with seats next to each other and a complimentary bottle of champagne. \n")



# Solution:
# Fix Error ---> single_tickets does not take into account that double_tickets are made up of 2 seats each in its calculations.
#                This leads to an incorrect amount of single tickets available being displayed.