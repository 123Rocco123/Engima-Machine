#The collections packadge is used to shift the indexs in the roters list so as to make sure that the correct enigma process is used.
import collections

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']

#These are some of the orignal rotaters that were used in Engima machines, which were orignaly created in 1922. 
roter1 = ['D','M','T','W','S','I','L','R','U','Y','Q','N','K','F','E','J','C','A','Z','B','P','G','X','O','H','V']
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

rotater1_shift = 0
rotater2_shift = 0
rotater3_shift = 0

rot1 = collections.deque(roter1)
rot2 = collections.deque(roter2)
rot3 = collections.deque(roter3)

def roterfunc(rotor, rot):
    global start, rotater1_shift, rotater2_shift, rotater3_shift
    global rot1, rot2, rot3
    
    chosen_roter = rotor

    #This is the initial positions of the first rotater for the enigma machine. 
    while start == True:
        roter_pos = int(input("Choose the position of the first roter (1 - 26): "))
        test = input("Write your first word: ").lower()
        
        start = False

    #The following line is the rotation that occurs on the initial setup of the roters. 
    rot1.rotate(roter_pos * -1)

    for letters in alphabet:
        if test == letters:
            index = alphabet.index(letters)
            test_word.append(rot[index])

            if rotor == roter1:
                rot1.rotate(-1)
    
    print(test_word, rot[-1])
    
    if chosen_roter == roter1:
        rotater1_shift += 1