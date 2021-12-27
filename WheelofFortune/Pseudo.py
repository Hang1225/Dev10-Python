#functions
wheelLogistics
buyVowels
bankrupt

#Q: money used to buy vowels is deducted from the pool or actual bank?
    # -> pool 
#Q: In the case of the vowel does not appear, do they lose their turn?
    # -> lose turn 
#Q: single word, 
#   stretch -> multiple, or phrase?

#variable
#currentPlayer = rand (1,3) initialize

# new round prompt
# prompt category, len(word)
#class -> Answer
    #word -> str
    #category -> str

#class player # list, query by iD
    #bank -> int 
    #pool -> int 

# func spin -> return number ($)
# return -1 for bankrupt, 0 for lose turn
#rand from 1-24
#1 is bankrupt
#2 is lose turn
# num > 2 , then rand 2-18
#rest assign rand (100-900) with 50 interval
#50 * rand 2-18

# player cannot start consecutively in 2 rounds

# func wheelLogistics (playerID,correctWord)
# enforce round record
    # player cannot start consecutively in 2 rounds
    # mechanism to determine if a round ends
    # refresh data for a new round
    # separate final round mechanism -> single-player
        # R,S,T,L,N,E revealed
        # no cost for vowel (1)
        # consonants (3)
# n = 1 for playerID = 1,2, n = -2 for playerID = 3
# result = spin()
# result = lose/bankrupt -> wheelLogistics (playerID + n)
# prompt func guess(correctWord) <- from WordGuessingGame -> return bool
# determine next step based on return from guess()
# if true -> # prompt buyVowel option
# then wheelLogistics(playerID)
# if false -> wheelLogistics (playerID + n)

# guess
# func inputValidation -> consonant
# return guess result in bool

# func buyVowel
# input entry
# func inputValidation -> vowel -> return bool
# player.bank[player.ID] -= 250
# guess (input)