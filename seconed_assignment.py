#!/usr/bin/env python3

# check all the string chars, using the methodes .islower() and .isupper()
# and switch between the lower to upper and vice versa


given_string = input("please enter a string to change: ")
new_string = ''                      # this is the new string that will contains the switched characters
for i in given_string:
    if i.islower():                  # check if i is lowercase
        sw = i.upper()               # replace it to uppercase
        new_string = new_string + sw # add the new i to new_string
    else:                            # else means that i is uppercase so do the opposite
        sw = i.lower()
        new_string = new_string + sw

print (new_string)

in this task the input is a string that seperated with commas
the output should be the seconed higher int in that string

string_score = input("please enter the scores sperate with comma: ") # taking scores from the subscriber as a string

list_score = list(string_score.split(',')) # change the string to list

new_list_score = [] # this list is to identify and remove duplicates

for score in list_score:
    if not score in new_list_score:     # chack if score allready exsist in the new list
        new_list_score.append(score)         # if not --> add score to the new list

int_list = [int(x) for x in new_list_score] # change the list member to intger using list comprehension
# if the list is string the sorted will not work correctly for scores with 2 or more digits!!

sort_int_list = sorted(int_list) # sort the int_list from the biggest to the smallest

print (sort_int_list[-2]) # print the list-member that locate before the last one
