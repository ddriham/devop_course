#!/usr/bin/env python3

def extract_availability():
    with open("log1.txt", "r") as log_file:
        available_list = []
        yard_list = []
        read_log_file = log_file.read().split("\n")

        for line in read_log_file:
            if "yard" in line:
                yard_list.append(line)
            else:
                available_list.append(line)

    list_available_dicts = []
    list_yard_dicts = []
    for i in range(len(available_list)-1):
        new_1 = {}
        new_1['name'] = available_list[i].partition(':')[0]
        new_1['day'] = available_list[i].split(' ')[4]
        new_1['time'] = int(available_list[i].partition('at')[2].partition(':')[0])
        list_available_dicts.append(new_1)
    for j in range(len(yard_list)):
        new_2 = {}
        new_2['name'] = yard_list[j].partition(':')[0]
        new_2['day'] = yard_list[j].split(' ')[5]
        new_2['time'] = int(yard_list[j].partition('at')[2].partition(':')[0])
        list_yard_dicts.append(new_2)
    log_file.close()

    return (list_available_dicts, list_yard_dicts)


def meeting_time():
    available_list, yard_list = extract_availability()
    people = list(set(i['name'] for i in available_list))
    number_of_people = len(people)
    available_slot = []
    for i in yard_list:
        lst = []
        for j in available_list:
            if i['day'] == j['day'] and i['time'] == j['time']:
                if i['name'] != j['name'] and j['name'] not in lst:
                    lst.append(j['name'])
                    if len(lst) == number_of_people - 1:
                        add_tuple = (i['name'], i['day'], i['time'])
                        if add_tuple not in available_slot:
                            available_slot.append(add_tuple)
    print ("There is {} meeting options!".format(len(available_slot)))
    if available_slot:
        for i in range(len(available_slot)):
            print ("All of us can meet at {}'s yard on {} at {}:00".format(available_slot[i][0], available_slot[i][1], available_slot[i][2]))
            a = input("Do you want to see another option? Yes/No ").title()
            if a == 'Yes' or a == '':
                if i != len(available_slot) -1:
                    continue
            else:
                print ("Thank you for using our meeting calculator! ")
                break
    else:
        print ("Sorry, there is no option where all of us can meet!")

    return



print(meeting_time())



