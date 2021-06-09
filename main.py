#Enigma Machine

from functions import roterfunc, reflector
from functions import rotor1, roter2, roter3, rot1, rot2, rot3
from functions import test_word, round_one

#This is the change of letter that occurs in the first rotator. 
    #The way that the roter works is by 

roterfunc(rotor1, rot1)
#print(rotor1)
#print(rot1)

roterfunc(roter2, rot2)
#print(roter2)
#print(rot2)

roterfunc(roter3, rot3)
#print(roter3)
#print(rot3)

#This block of code is used to remove the last two elements in the list which aren't supposed to be there.
    #This is a temporary solution until a permament solution will be found. 
for i in range(2):
    del test_word[-1]

reflector()
print(test_word)

#This is the letter that will be added to the "round_one" list.
    #It's used to keep track of the letter which is spit out when it goes through the reflector.
round_one.append(test_word[len(test_word) - 1])