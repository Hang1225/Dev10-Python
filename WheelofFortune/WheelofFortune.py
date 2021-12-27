# import 
import time #sleep
import random #randomizer
import os #working directory
from subprocess import run
# variable declaration
class c_playerRecord:
    name = []
    bank = []
    pool = []

class c_wordBank:
    words = []
    category = []

class c_info:
    round = int
    currentPlayer = int
    played = []
    vowelPrice = int
    wordIndex = int
    guessed = [] #list of guessed letters
    usedIndex = [] #list of used words
# variable assignment
gameInfo = c_info
player = c_playerRecord
wordBank = c_wordBank
#message ID
m = {
    'welcome':0,
    'promptname':1,
    'start':2,
    'spin':3,
    'wheel-lost':4,
    'wheel-bankrupt':5,
    'guess-buyvowel':12,
    'guess-welcome':6,
    'pool':7,
    'guess-typecheck':8,
    'guess-validate':9,
    'guess-repeat':10,
    'guess-success':11,
    'wheel-error-yn':13,
    'guess-fail':14,
    'next':15,
    'round':16,
    'player':17,
    'guess-win':18,
    'guess-nomoney':19,
    'guess-reveal':20,
    'wheel-finalround':21,
    'insufficientfund':22,
    'guess-onlyvowel':23,
    'final-announcement':24,
    'guess-novowel':25,
    'final-stat':26,
    'final-win':27
}
# func declaration

# msg engine; handles all print logistics
def msg(msgID,msgInput='',msgInput2=''):
    if msgID == m['welcome']:
        print ('Welcome to the Wheel of Fortune')
        print ('===============================')
    elif msgID == m['promptname']:
        return input ('Player %i, please enter your name: ' %(msgInput))
    elif msgID == m['start']:
        print ('\nEntry completed, welcome %s' %(msgInput))
        return input('** Press "Enter" to start the game **')
    elif msgID == m['spin']:
        print ('\nRound: %i\nCurrent Player: %s\nPool: $%i' %(msgInput,msgInput2,player.pool[gameInfo.currentPlayer]))
        return input ('Please Press Enter to spin\n')
    elif msgID == m['wheel-lost']:
        print ('Oops %s, you lost this turn!' %(msgInput))
    elif msgID == m['wheel-bankrupt']:
        print ('Oh no bankrupt! Better luck next time %s!' %(msgInput))
    elif msgID == m['guess-welcome']:
        print ('\nGuess the Word')
        print ('==============')
        print('This word describes a {}, and has {} letters.\n'.format(msgInput,msgInput2))
        print ('Now take your guess!')
    elif msgID == m['pool']:
        print ('Congratulations! You spun $%i. Current pool: $%i' %(msgInput,msgInput2))
    elif msgID == m['guess-typecheck']:
        print('Please enter a word or letter!\n')
        return input('input: ').lower()
    # guess- validate
    elif msgID == m['guess-validate']:
        print('Please input a %s only!' %(msgInput))
        return input('input: ').lower()
    # guess - repeated entry
    elif msgID == m['guess-repeat']:
        print('You have guessed this letter already, try another one!')
    # guess - success
    elif msgID == m['guess-success']:
        print ('Good guess! The word is now: ' + ''.join(msgInput))
    # wheel - buy vowel prompt
    elif msgID == m['guess-buyvowel']:
        return input ('Do you want to buy an vowel for $%i? Enter [y/n]\n' %(gameInfo.vowelPrice)).lower()
    elif msgID == m['wheel-error-yn']:
        return input ('Please enter "y" or "n" only!\n').lower()
    elif msgID == m['guess-fail']:
        print ('Booo! Wrong guess!')
    elif msgID == m['next']:
        print ('Next up is %s' %(msgInput))
    elif msgID == m['guess-win']:
        print ('You got it! You just earned: $%i!' %(msgInput))
    elif msgID == m['guess-nomoney']:
        print ('Unable to purchase vowel, your pool is less than $250!')
    elif msgID == m['wheel-finalround']:
        print ('Welcome to the final round, %s.' %(player.name[msgInput]))
        print ('You have a total of $%i in your bank. If you win, you will receive an extra $2,000.' %(player.bank[msgInput]))
        print ('You will have a chance to guess 3 consonants and 1 vowel, at no cost!')
        print ('Now, good luck!')
    elif msgID == m['guess-reveal']:
        print ('Parts of the word is revealed: %s' %(''.join(msgInput)))
    elif msgID == m['insufficientfund']:
        print ('Only vowels are left unguessed, however your pool is insufficient to buy a vowel!')
    elif msgID == m['guess-onlyvowel']:
        print ('Only vowels are left unguessed, please guess an vowel!')
    elif msgID == m['final-announcement']:
        if msgInput + msgInput2 > 1:
            print ('Below is the number of guessed you have remaining:')
            print ('Vowels: %i' %(msgInput2))
            print ('Consonants: %i' %(msgInput))
        else:
            print ('You only have 1 guess left! Please guess the entire word!')
    elif msgID == m['guess-novowel']:
        print ('Only vowels are left unguessed but you ran out of vowel guesses, please guess the word!')
    elif msgID == m['final-stat']:
        print ('========== Result ==========')
        _export = 'Name,Bank\r\n'
        for i in range(1,4):
            _index = player.bank.index(max(player.bank))
            _export = _export + player.name[_index] + ',' + str(player.bank[_index]) + '\r\n'
            print ('%i. %s, bank: %i' %(i,player.name[_index],player.bank[_index]))
            player.bank[_index] = -1
        exportFile(_export)
    elif msgID == m['final-win']:
        print ('Congratulations %s, YOU WIN!' %(msgInput))
    return 
    
# input validation: consonant vs vowel
def validate(letter,status=0):
    # stat; 0: consonant, 1: vowel, 2: y/n validate
    _vowel = ['a','e','i','o','u']
    if status == 2:
        return True if letter == 'y' or letter =='n' else False 
    if letter in _vowel: # is a vowel
        return True if status == 1 else False
    elif letter not in _vowel:
        return True if status == 0 else False

# reads a list of words from file
def importWords():
    os.chdir(os.getcwd()+"/WheelofFortune")
    _file = open(os.getcwd()+'/wordbank.csv','r')
    _lines = _file.read().splitlines()
    for i in range(1,len(_lines)): 
        _list = _lines[i].split(',')
        wordBank.words.append(_list[0])
        wordBank.category.append(_list[1])
    _file.close()

#export file
def exportFile(text):
    _file = open(os.getcwd()+'/log.csv','w+') #write
    _file.write(text)
    _file.close()

# outputs the next playerID based on currentPlayerID
def next (playerID):  
    if playerID == 2:
        return 0
    else: return playerID + 1 

# simulation of spinning wheel; return int 
def spin():
    _pos = random.randint(0,23)
    if _pos < 2: return _pos # 0 = lose, 1 = bankrupt
    else:
        _pos = random.randint(2,18)
        return _pos * 50 # pool range from $100-$900, $50 interval

# store and pull game info
def info(status,code=0, value1=0,value2=0):
    # status: 0 = read; 1 = write
    if status == 0: #read info
        return gameInfo.round, gameInfo.currentPlayer, player.pool[gameInfo.currentPlayer]
    if status == 1: #write info
        if code == m['pool']:
            player.pool[value1] = value2
        elif code == m['round']:
            gameInfo.round = value1
        elif code == m['player']:
            gameInfo.currentPlayer = value1

# generate new word index
def generateWord():
    _index = random.randint(0,len(wordBank.words)-1)
    while _index in gameInfo.usedIndex:
        _index = random.randint(0,len(wordBank.words)-1)
    gameInfo.usedIndex.append(_index)
    return _index 

#check to see if only vowels are left unguessed
def onlyVowelCheck(remaining):
    _onlyVowel = True
    for i in remaining:
        if validate(i,0): #if consonant exists
            _onlyVowel = False
            break
    return _onlyVowel

# guess engine; handles guessing logistics
def guessLogistics(final=False,entryType=0):
    _limit_v = 50
    _limit_c = 50
    if final: 
         #final round: 3 consonants, 1 vowel
        _limit_v = 1
        _limit_c = 3
    _word = wordBank.words[gameInfo.wordIndex].lower() # correct word
    _ret = False # return value
    _entry = ['consonant','vowel']
    _str = ['-'] * len(_word) #initialize string to be revealed
    msg(m['guess-welcome'],wordBank.category[gameInfo.wordIndex],len(_word))
    # reveal letters if exist
    if gameInfo.guessed != []:
        for l in gameInfo.guessed:
            l_position = [i for i, n in enumerate(_word) if n == l]
            for i in range(0,len(l_position)):
                _str[l_position[i]] = l # reveal guessed letters
        msg(m['guess-reveal'],_str)
    while _limit_v + _limit_c > 0:
        # guess count announcement during final round
        if final:
            msg(m['final-announcement'],_limit_c,_limit_v)

        #only vowel left unguessed check
        if onlyVowelCheck(set(_word) - set(gameInfo.guessed)):
            if player.pool[gameInfo.currentPlayer] < gameInfo.vowelPrice: # insufficient fund
                msg(m['insufficientfund'])
                return False
            else: 
                player.pool[gameInfo.currentPlayer] -= gameInfo.vowelPrice # deduct vowel price
                if _limit_v > 0:
                    msg(m['guess-onlyvowel'])
                    entryType = 1 #restrict input to vowel only
                else: 
                    msg(m['guess-novowel'])
                    entryType = 0
        #input
        _input = input('guess: ').lower().strip()
        while _input.isalpha() != True and _input != ' ': # check input integrity 
            _input = msg(m['guess-typecheck'])
        #validate entry type: consonant/vowel 
        while not validate(_input,entryType): # 0 = consonant, 1 = vowel
            _input = msg(m['guess-validate'],_entry[entryType])
        #word match
        if _input == _word:
            _ret = True
            break
        #guessed word
        elif _input in gameInfo.guessed:
            msg(m['guess-repeat'])
            continue
        #letter match
        elif _input in _word and len(_input) == 1: 
            l_position = [i for i, n in enumerate(_word) if n == _input] # return all index for the guessed letter
            for i in range(0,len(l_position)):
                _str[l_position[i]] = _input # reveal guessed letters
            if '-' not in _str: # all letters are guessed
                _ret = True 
                break
            else: 
                if entryType == 0: _limit_c -=1 
                else: _limit_v -=1
                # guess correctly
                gameInfo.guessed.append(_input)
                msg(m['guess-success'],_str)
                if _limit_v > 0: 
                    _input = msg(m['guess-buyvowel'])
                    while not validate(_input,2):
                        _input = msg(m['wheel-error-yn']) 
                if _input == 'y': # if buy vowel
                    _pool = player.pool[gameInfo.currentPlayer]
                    if _pool < gameInfo.vowelPrice:
                        msg(m['guess-nomoney'])
                        entryType = 0
                        wheelLogistics(True)
                    else:
                        player.pool[gameInfo.currentPlayer] -= gameInfo.vowelPrice
                        entryType = 1 # allow vowel entry
                else:
                    entryType = 0
                    if final == False: wheelLogistics(True)      
        #no match
        else: 
            _ret = False
            break
    return _ret

# core engine; determines all logistics
def wheelLogistics(Gamestat=False):
    # check round status
    msg(m['final-stat'])
    if len(gameInfo.played) >= 3 and Gamestat == False: #if all players have played
        gameInfo.wordIndex = generateWord()
        gameInfo.guessed = []
        print ('\nLoading new round...')
        time.sleep(5)
        print ('\n=========== NEW ROUND ===========')
        gameInfo.round += 1 #next round
        gameInfo.played = [] #reset
    # round 3 logistics
    if gameInfo.round == 3:
        #set current player to player w/ highest bank
        gameInfo.wordIndex = generateWord()
        gameInfo.currentPlayer = player.bank.index(max(player.bank)) 
        msg(m['wheel-finalround'],gameInfo.currentPlayer)
        time.sleep(5)
        #set vowel price to 0
        gameInfo.vowelPrice = 0
        #reveal letters
        _reveal = ['R','S','T','L','N','E']
        gameInfo.guessed = []
        for i in _reveal:
            gameInfo.guessed.append(i.lower())
        #start
        if (guessLogistics (True)):
            player.bank[gameInfo.currentPlayer] += 2000
            msg (m['final-win'],player.name[gameInfo.currentPlayer])
            msg (m['final-stat'])
        else:
            msg(m['guess-fail']) 
            msg (m['final-stat'])
        return
    
    # get round info
    _round,_playerID,_pool = info(0)
    _name = player.name[_playerID]
    #prompt spin message
    _input = msg(m['spin'],_round,_name)
    _spinResult = spin()
    print ('*** Spinning...')
    time.sleep(2)
    if _name not in gameInfo.played:
        gameInfo.played.append(_name) # record played status
    #lose
    if _spinResult == 0:
        msg(m['wheel-lost'],_name)
        msg(m['next'],player.name[next(_playerID)])
        info(1,m['pool'],_playerID,0) # erase current player pool
        info(1,m['player'],next(_playerID)) # set current player to next in line
        wheelLogistics()
    #bankrupt
    elif _spinResult == 1: 
        msg(m['wheel-bankrupt'],_name)
        msg(m['next'],player.name[next(_playerID)])
        player.bank[_playerID] = 0 # clear bank
        info(1,m['pool'],_playerID,0) # erase current player pool
        info(1,m['player'],next(_playerID)) # set current player to next in line
        wheelLogistics()
    #prize
    else:
        player.pool[_playerID] += _spinResult
        msg(m['pool'],_spinResult,player.pool[_playerID]) # announce the pool
        # fresh turn
        if _pool == 0: 
            if guessLogistics(): #win the entire round
                player.bank[_playerID] += player.pool[_playerID]
                msg(m['guess-win'],player.pool[_playerID])
                print ('\nLoading new round...')
                time.sleep(5)
                print ('\n=========== NEW ROUND ===========')
                gameInfo.guessed = []
                info(1,m['pool'],_playerID,0) 
                info(1,m['player'],next(_playerID))
                info(1,m['round'],_round+1)
                gameInfo.played = []
                gameInfo.wordIndex = generateWord()
                wheelLogistics()
            else: #guessed wrong
                msg(m['guess-fail']) 
                msg(m['next'],player.name[next(_playerID)])
                info(1,m['pool'],_playerID,0) 
                info(1,m['player'],next(_playerID)) 
                wheelLogistics()

# prompt for initializing the program
def _prompt(): 
    msg(m['welcome'])
    # prompt name input
    for i in range(0,3):
        _name = msg(m['promptname'],i+1)
        player.name.append(_name.capitalize())
        # initialize array
        player.bank.append(0)
        player.pool.append(0)
    _name = [x for x in player.name]
    _key = msg(m['start'],','.join(_name))
    if _key == '':
        # load words from bank file
        importWords()
        # randomly determine turn order
        random.seed()
        #initialize game info
        info(1,m['round'],1)
        info(1,m['player'],random.randint(0,2))
        info(1,m['pool'],0)
        gameInfo.vowelPrice = 250
        gameInfo.wordIndex = generateWord()
        wheelLogistics(False) #start spinning
    else: print ('Good bye!')

# program begins
_prompt()