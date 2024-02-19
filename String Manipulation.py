
# This is a program to manipulate strings
# It will request the user to enter a string and then print:

# Alternating (characters and then words) between upper and lower case.


# Program intro

print("\nThis program will convert an entered phrase into two different outputs.\n")

print("Output 1 - The characters of the phrase will alternate between upper and lower case.\n")

print("Output 2 - The words of the phrase will alternate between upper and lower case\n")


# Enter string

phrase = input("Please enter a phrase: ")



# Alternating characters

new_phrase = ""

for i in range(len(phrase)):

    if i % 2 == 0:

        new_phrase += phrase[i].upper()

    else:

        new_phrase += phrase[i].lower()

print(new_phrase)



phrase_list = phrase.split(" ")

new_phrase_2 = []




# Alternating words

for i in range(len(phrase_list)):

    if i % 2 == 0:
        
        new_phrase_2.append(phrase_list[i].upper())

    else:

        new_phrase_2.append(phrase_list[i].lower())

print(" ".join(new_phrase_2))