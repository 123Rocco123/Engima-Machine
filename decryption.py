import collections

from functions import alphabet
from functions import rotor1, roter2, roter3
from functions import reflector

initial_pos = []

rot1 = collections.deque(rotor1)
rot2 = collections.deque(rotor1)
rot3 = collections.deque(rotor1)

for i in range(3):
    print("Write the position of rotor", (i + 1))
    choice = input()

    initial_pos.append(choice)
    choice = ""

#The following is used to change the rotations of the rotors to the positions that the user selected.
for rotor_choices in initial_pos:
    if rotor_choices == 0:
        rot1.rotate(rotor_choices * -1)
    elif rotor_choices == 1:
        rot2.rotate(rotor_choices * -1)
    else:
        rot3.rotate(rotor_choices * -1)

#This is used for test purposes
print(rotor1, "\n")
print(rot1)

