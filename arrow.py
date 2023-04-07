#!/usr/bin/env python3
### this function will print an arrow

def arrow(my_char, max_length):
    for i in range(1, max_length+1):
        print(my_char*i)
    for i in range(max_length-1, 0, -1):
        print(my_char*i)


arrow("*",7)
