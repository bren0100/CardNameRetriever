import json, os, fnmatch, re
#json to be able to interact with and format the data
#os to be able to find the file within the designated file path
#fnmatch dependency has been removed. this should be removed.
#re text search for card names is done using regular expression

#function for verifying the existence of the file before attempting to open
def find(name, fullPath):
    isFound = False
    for roots, dirs, files in os.walk(fullPath):
        for file in files:
            print('Searching...') 
            if file == name:
                isFound = True
                print('Found!')
                return isFound
            else:
                isFound = False
    print('File not found in '+fullPath+' directory...')
    return isFound

#get the name of the deck
nameOfDeck = input('Enter the name of the deck:')

userName = os.path.expanduser('~')
fullPath = userName+r'/Documents/My Games/Tabletop Simulator/Saves/Saved Objects/ExportToTxt'
#Does the file exist?
#remember to remove addition to /commander decks also in the next block
deckExists = find(nameOfDeck+'.json', fullPath)

if deckExists:
    #open file
    json_data = open(fullPath+'//'+nameOfDeck+'.json')
    deckData = json.load(json_data)
    
    #convert the json data into string
    stringFormatDeckData = json.dumps(deckData, indent=2)
    
    #using regex iterate through the data to find the nickname of each card
    pattern = re.compile(r'Nickname\": \"(.+)\"', re.MULTILINE)
    listOfNames = pattern.finditer(stringFormatDeckData)
    
    #create the txt file
    txtFile = open(userName+r'/Desktop/'+nameOfDeck+'.txt', 'w+')
    
    #populate txt file
    for name in listOfNames:
        txtFile.write(name.group(1)+'\n')
        
    #cleanup
    txtFile.close()
    json_data.close()
    input('\nA .txt file has been created on your desktop!\nYou may close this window.')
else:
    input('\nThe File or Directory could not be found.')
    
