## caeser cipher
## based off of code by al Sweigart
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz'
MaxKeySize = len(SYMBOLS)

def getMode():
    while True:
        print('do you wish to encrypt\n or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt','e','decrypt','d']:
            return mode
        else:
            print('enter either \'encrypt\', \'e\', \'decrypt\' or \'d\' >:')

def getMessage():
    print('enter your message(\'plaintext\')')
    return input()

def getKey():
    key = 0
    while True:
        print('enter your key (1-%s)>:' %(MaxKeySize))
        key = int(input())
        if (key >= 1 and key <= MaxKeySize):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = int(SYMBOLS.find(symbol))
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
        
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += SYMBOLS[symbolIndex]
        
        translated += SYMBOLS[(symbolIndex + key) % MaxKeySize]
    
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('your \'ciphertext\' is:')
print(getTranslatedMessage(mode, message, key))