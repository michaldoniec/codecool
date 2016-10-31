"""Program that computes numbers of doors that are opened after the 100 passage
through corridor with 100 doors.
"""


__author__ = "Michal Doniec"


passed = 0

step = 0

hall = ["c"]*100


def passing(list,step):
    """Function that close or open the door."""
    for num_door in range(step-1,len(list),step):
            if list[num_door] == "c":
                list[num_door] = "o"

            elif list[num_door] == "o":
                list[num_door] = "c"


while passed < 100:
    step += 1
    passing(hall,step)
    passed += 1


opened_doors = []

for num_door in range(len(hall)):  #to establish which doors are opened
    if hall[num_door] == "o":
        opened_doors.append(num_door+1)

opened = str(opened_doors).strip("[]")

print("The following doors are open: " + opened)
