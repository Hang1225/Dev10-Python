import random
record = {'wins':0, "losses":0}
rand_record = []
def puzzel ():
    path = 'words_alpha.txt'
    file = open(path,'r').readlines()
    random.seed()
    _len = 0
    rand_num = random.randrange(0,len(file))
    input_list = []
    # pick random words
    while _len < 5 and file[rand_num] in rand_record: # constraint: 5 letters or above and no duplicate
        rand_num = random.randrange(0,len(file))
        _len = len(file[rand_num])
    else: 
        word = file[rand_num].strip() #remove spaces
        rand_record.append(word) #library of used words
        #print(rand_record)
    guess = 7
    prt_str = ['_'] * len(word)  
    print('Take a Guess! The word has %i letters\n' % len(word))
    while guess > 0:
        u_input = input('input: ')
        if u_input.isalpha() != True: # check input integrity 
            print('Please enter a word or letter!')
            continue
        if u_input.lower() == word.lower(): # word match
            logistic(1,word) # 1 = win, 0 = lost
            break
        elif u_input.lower() in input_list:
            print('You have guessed this letter already, try another one!')
            continue
        elif u_input.lower() in word.lower(): # letter match
            l_position = [i for i, n in enumerate(word.lower()) if n == u_input.lower()] # return all index for the guessed letter
            for i in range(0,len(l_position)):
                 prt_str[l_position[i]] = u_input.lower()
            if '_' not in prt_str: # all _ are occupied; == all blanks are filled
                 logistic(1,word)
            else: print ('Good guess! The word is now: ' + ''.join(prt_str)) # keep guessing
        else: #no match
            print('Wrong guess! Try again! Guesses remaining: {num}'.format(num=guess))
            guess-=1
        input_list.append(u_input.lower())
    else:
        logistic(0,word)

def logistic(condition,word):
    print ('-------------------------') # divider
    if condition == 0:
        print ('you have lost! The word is: %s' % (word))
        record['losses']+=1
    elif condition == 1: #win
        print ('you have won! The word is: %s' % (word))
        record['wins']+=1
    # user decision: continue/n
    print('You have won {} times and lost {} times'.format(record['wins'],record['losses']))
    ans = input('Would you like to play again? Enter Y/N\n')
    loop = True
    while loop:
        if ans.lower() == 'y':
            puzzel()
            break
        elif ans.lower() == 'n':
            print ('Have a good day!')
            break
        else: ans = input ('Invalid entry. Enter Y or N\n')


#puzzel() # call function to initiate