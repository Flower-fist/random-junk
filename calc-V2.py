##[]made by enrique
##[]code is structured based on the length of an
##[]expression, then the type/syntax,
##[]three piece cmds(commands) are divided into "infix" and
##[]"prefix" based on the position of the operating function

#import modules and define constants
e = 2.7182
import math
import random
#setup UI and whack
credits = '''program by enrique
             stack overflow sucks'''
manual = '''this uses standard notation, with the intentional 
            exlusion of parentense.
            basic arithmetic,
            exponents,
            roots,
            and basic trig are supported
            use 'q' to quit'''


print("basic calculator  >:")
print("c to view credits >:")
print("m to view manual  >:")

temp = input()
if temp == "c":
    print(credits)
elif temp == "m":
    print(manual)
else:
    pass

#define the infix case
def infix():
    temp[0] = int(temp[0])
    temp[2] = int(temp[2])
    if temp[1] == '+':
        result = temp[0] + temp[2]
        print(str(result))
    elif temp[1] == '-':
        result = temp[0] - temp[2]
        print(str(result))
    elif temp[1] == '*':
        result = temp[0] * temp[2]
        print(str(result))
    elif temp[1] == '/':
        result = temp[0] / temp[2]
        print(str(result))
    elif temp[1] == '**':
        result = temp[0] ** temp[2]
        print(str(result))

#define the prefix case
def prefix():
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    if temp[0] == 'root':
        result = temp[1]**(1/temp[2])
        print(str(result))
    elif temp[0] == 'log':
        result = math.log(temp[1],(temp[2]))
        print(str(result))
    elif temp[0] == 'rand':
        result = random.radiant(temp[1],temp[2])
        print(str(result))

#check if a thing is in infix or prefix form
def threePiece():
    if not temp[1].isdigit():
        infix()
    elif not temp[0].isdigit():
        prefix()
    else:
        print('incorrect syntax  >:')
        
#now define the two-piece case.
def twoPieces():
    if not str.isdigit(temp[0]):
        temp[1] = int(temp[1])
        if temp[0] == 'sqrt':
            result = temp[1]**(1/2)
            print(str(result))
        elif temp[0] == '^e':
            result = temp[1]**e
            print(str(result))
        elif temp[0] == 'ln':
            result = math.log(e,(temp[1]))
            print(str(result))
        elif temp[0] == 'sin':
            result = math.sin(temp[1])
            print(str(result))
        elif temp[0] == 'cos':
            result = math.cos(temp[1])
            print(str(result))
        elif temp[0] == 'tan':
            result = math.tan(temp[1])
            print(str(result))
        elif temp[0] == 'sec':
            result = math.sec(temp[1])
            print(str(result))
    else:
        print('incorrect snytax  >:')
    
#code loops through classic "fetch exuecute" cycle.
while True:
    temp = input()
    if temp == 'q':
        break
    temp = temp.split()
    lenght = len(temp)
    if lenght < 2:
        print("cannot perform with-")
        print("-out arguments    >:")
    else:
        if lenght == 2:
            twoPieces()
        elif lenght == 3:
            threePiece()
        else:
            print("too many argments>:")

