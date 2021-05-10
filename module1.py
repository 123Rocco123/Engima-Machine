#Enigma Machine

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

#This is the initial positions of the first rotater for the enigma machine. 
roter_pos = int(input("Choose the position of the first roter (1 - 26): "))

rot1 = collections.deque(roter1)
rot2 = collections.deque(roter2)
rot3 = collections.deque(roter3)

rot1.rotate(roter_pos * -1)

print(roter1)
print(rot1)

test = input("Write your first word: ").lower()

test_word = []
test_word2 = []
test_word3 = []

rotater1_shift = 0
rotater2_shift = 0
rotater3_shift = 0

#This is the change of letter that occurs in the first rotator. 
for i in range(len(test)):
    for letters in alphabet:
        if test[i] == letters:
            index = alphabet.index(letters)
            test_word.append(rot1[index])

            rot1.rotate(-1)
            rotater1_shift += 1

#Whenever the rotater does a full revolution (26 ticks), then it will be set back to 0, its starting position, and the next rotater will shift by one. 
if rotater1_shift == 26:
    rotater1_shift = 0
    rotater2_shift += 1

    rot2.rotate(-1)

print(test_word)     

#This is the change of letter that occurs in the second rotator. 
for i in range(len(test_word)):
    for chars in alphabet:
        if chars == (test_word[i]).lower():
            index1 = alphabet.index(chars)
            test_word2.append(rot2[index1])

if rotater2_shift == 26:
    rotater2_shift = 0
    rotater3_shift += 1

    rot3.rotate(-1)

print(test_word2) 

#This is the change of letter that occurs in the third rotator. 
for i in range(len(test_word2)):
    for letts in alphabet:
        if letts == (test_word2[i]).lower():
            index2 = alphabet.index(letts)
            test_word3.append(rot3[index2])

print(test_word3)