# Engima Machine
 A simulator for the Engima Machine used by the Germans before and during the Second World War. Written in Python.

The way that the simulator works is by intially asking the user to setup their roters in posiiton. Meaning which index is supposed to be assigned to each letter in the roter. 

## How the machine works
Once the user has finished the inital setup, they'll be instructed to write out a message that they want to encrypt, with each letter that they add, the first roter (right most) will move by one. After the first roter has shifted 26 times, then the second roter will shift by one. Once that has done 26 rotations, then the third will.  

### Role of the Reflector
The role of the reflector is that of changing the letter that goes in to its assigned pair. For example, say that A and Z are paired with one another, if the letter A goes into the reflector, then the letter Z would come out of it. This is to further encrypt the message. 
