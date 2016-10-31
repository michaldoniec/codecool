"""Program that computes numbers of doors that are opened after the 100 passage
through corridor with 100 doors.
"""


__author__ = "Michal Doniec"


passed = 0

step = 0

hall = ["c"]*100

while passed < 100:  #loops 100-times
    step += 1
    for num_door in range(step-1,len(hall),step):
        if hall[num_door] == "c":
            hall[num_door] = "o"
        elif hall[num_door] == "o":
            hall[num_door] = "c"
    passed += 1

opened_doors = []

for num_door in range(len(hall)):  #to establish which doors are opened
    if hall[num_door] == "o":
        opened_doors.append(num_door+1)

opened = str(opened_doors).strip("[]")

print("The following doors are open: " + opened)
