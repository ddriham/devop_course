#!/usr/bin/env python3

def digits(ID):
    s = 0
    for i in range (8):
        digit = (int(ID[i]))
        if i % 2 == 0:
            s = s + digit
        else:
            digit = digit * 2
            if digit <= 9:
                s = s + digit
            else:
                ones = digit % 10
                tens = 1
                s = s + ones + tens
    ones = s % 10
    check_digit = 10 - ones
    if check_digit == 10:
        check_digit = 0
    return check_digit


ID = input("enter an ID to check: ")

print(digits(ID))
