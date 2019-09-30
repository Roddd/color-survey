#!/usr/bin/env python3.6

import io

d = {}
#TODO: If file does not exist, this crashes
#Please add a try/catch and create if file not found
#TODO: If file is empty or malformed, this crashes
#Please add or make sure format is: "1. Red:0,2. Green:0,3. Blue:0" as starter data
with io.open("survey.txt") as f:
    for line in f:
       line = line.replace("\n", "")
       list_stuff = line.split(",")
       for i in list_stuff:
           (key, val) = i.split(":")
           d[key] = int(val)
    f.close()

loop = True
while loop == True:
    choice_list = ["1. Red", "2. Green", "3. Blue"]
    print("What's your favorite color?")
    i = 0
    while i < 3:
        print(choice_list[i])
        i += 1
    try:
        choice = int(input("Type choice (num): "))
    except ValueError:
        choice = -1
    if choice > 0 and choice <= 3:
        loop = False

d.update({choice_list[choice - 1]:int(d[choice_list[choice - 1]]) + 1})

print("New values:")
print(d)

output = ""
for key,val in d.items():
    output = output + key + ":" + str(val) + ","

#TODO: If we cannot write to file (like permission issue), this will crash
#Please halp us exit gracefully (similarly if we can't read file)
with io.open("survey.txt", "w") as f:
    f.write(output.rstrip(","))
    f.write("\n")
    f.close
