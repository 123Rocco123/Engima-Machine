#Enigma Machine

from functions import roterfunc, reflector
from functions import rotor1, roter2, roter3, rot1, rot2, rot3
from functions import test_word, round_one

choice = input("Do you want to encrypt or decrypt (Enc / Dec)?").capitalize()

def encryption_process():
    #This is the change of letter that occurs in the first rotator. 
        #The way that the roter works is by moving whenever it recieves an electric signal by a place, while the sequence of the alphabet for the roter remains the same.

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

    for encrpyted in round_one[len(round_one) - 1]:
        roterfunc(roter3, rot3)
        roterfunc(roter2, rot2)
        roterfunc(roter1, rot1)

def decryption_process():
    pass

#This is the selection process which is used to choose between if the user wants to decrypt or encrypt
if choice == "Enc":
    encryption_process()
elif choice == "Dec":
    decryption_process()
else:
    while choice != "Enc" or choice != "Dec":
        print("Invalid Input\n")
        choice