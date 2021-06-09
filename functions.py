#The collections packadge is used to shift the indexs in the roters list so as to make sure that the correct enigma process is used.
import collections

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']

#These are some of the orignal rotaters that were used in Engima machines, which were orignaly created in 1922. 
rotor1 = ['D','M','T','W','S','I','L','R','U','Y','Q','N','K','F','E','J','C','A','Z','B','P','G','X','O','H','V']
roter2 = ['H','Q','Z','G','P','J','T','M','O','B','L','N','C','I','F','D','Y','A','W','V','E','U','S','R','K','X']
roter3 = ['U','Q','N','T','L','S','Z','F','M','R','E','H','D','P','X','K','I','B','V','Y','G','J','C','W','O','A']

#The dictionary below is the Engima Machine's relfector, Which is the final stage of the first cycle of the encryption.
relfector1 = {'i':'u', 
              'a':'s',
              'd':'v',
              'g':'l',
              'f':'t',
              'o':'x',
              'e':'z',
              'c':'h',
              'm':'r',
              'k':'n',
              'b':'q',
              'p':'w'}

start = True

test_word = []
round_one = []

rotater1_shift = 0
rotater2_shift = 0
rotater3_shift = 0

index1 = 0

rot1 = collections.deque(rotor1)
rot2 = collections.deque(roter2)
rot3 = collections.deque(roter3)


#The function below is the blueprint for the roters, its used to determine how the roters are supposed to act when they are to encrypt a word or letter. 
def roterfunc(rotor, rot):
    #The global statements are used to access the variables that were defined outside of the function. 
    global start, rotater1_shift, rotater2_shift, rotater3_shift
    global rot1, rot2, rot3
    global index1
    
    #The chosen_roter function is used to determine which roter is currently being used to encrypt the word, and how the roter has to rotate or not. 
    chosen_roter = rotor

    #This is the initial positions of the first rotater for the enigma machine. 
    while start == True:
        global test

        if start == True:
            rotor_pos = int(input("Choose the position of the first roter (1 - 26): "))
            test = input("Write your first word: ").lower()
        
            start = False

            #The following line is the rotation that occurs on the initial setup of the roters. 
            rot1.rotate(rotor_pos * -1)

    #The for loop is used to cycle through the alphabet and see if the letter which is being encrypted matches or not.
        #If it does match, then the index of that letter will be used to be put in the roter, and whichever letter corresponds to that index will be outputted. 
    if rotor == rotor1:
        for letters in alphabet:
            if test == letters:
                index = alphabet.index(letters)
                test_word.append(rot[index])

                if rotor == rotor1:
                    rot1.rotate(-1)
    else:
        for letters1 in alphabet:
            if letters1 == test_word[len(test_word) - 1].lower():
                index = alphabet.index(letters1)
                test_word.append(rot[index])

    if chosen_roter == rotor1:
        rotater1_shift += 1

#The function below is used for the reflector.
    #The for loop is used to cycle through the pairs in the dictionary, and find the letter which have to be swapped with oneanother.
def reflector():
    #The for loop is to cycle through all of the letter pairs which are found in the reflector.
    for letters in relfector1:
        #Since all the letters are lower case in the reflector, we have to make sure that the lower dot-function is used. 
            #If the pairs aren't found because they're not the key, then we cycle through the values, and append that to the list.
        if letters == test_word[2].lower():
            test_word.append(relfector1[letters].upper())
        elif relfector1[letters] == test_word[2].lower():
            test_word.append(letters.upper())