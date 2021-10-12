##smart cipher crack (histogram method)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz'
MaxKeySize = len(SYMBOLS)

COMMONLETTERS = ['e','t','a','i','o','n','s','h','r']

def getCipherText():
    print('enter your \'ciphertext\'')
    return input()

def makeHistogram(text):
    histogram = {}
    for symbol in SYMBOLS:
        histogram[symbol] = text.count(symbol)

    return histogram

def filterHistogram(histogram):
    newHistogram = {}
    for k in histogram:
        if k in COMMONLETTERS:
            newHistogram[COMMONLETTERS] = k
    
    return newHistogram

def getKeys(hist):
    for keys in hist:
        ##calculate the distance to a common letter for each
        ##possible key in hist
        pass