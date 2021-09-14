import random
##[]mad libs
##[]so  'libs' the thing to fill out
##[]and 'mads' is are the things we're filling in
##[]so these are both list of strings
print('''MAD LIBS:
      program by enrique.rkt
      INSTRUCTIONS:
      first player will write out a lib:
      the second will write out the reqisit words
      NOTES:
      the program does not enforce rules 
      such as word type or number of given words:
      these rules must be player enforced.
      thank you for your time.
      have fun!!''')
#pre-made-libs: computer stored libs for the game.
#(feature not used)

#preMadeLibs =
#[[][][][]]
#temp = random.radiant(0,3)
#libs = preMadeLibs[temp]

temp = input()
libs = temp.split()
temp =input()
mads = temp.split()
#now we have a lib to fill out and some word two fill out
#so this is done by removing a blank 
#and then inserting the 'correct' (that is the, 'funny')
#vaule.

for i in range(len(libs)):
    if not libs[i] == '[]':
        pass
    else:
        libs.pop(i)
        libs.insert(i,mads[i])
#now libs has all of blanks filled in.
#now we need to print out libs. the completed list.
for i in range(len(libs)):
    print(libs[i], end= ' ')
print('', end = '\n')
