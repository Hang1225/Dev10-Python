# function declaration
import os

def errMsg (input):
    print ('Please enter a {t} type value!'.format(t=input))

# variable declaration
class people:
    total_num = int
    menuSelection = int
    name = []
    slot = []

tournament = people

# Sign Up
def signUp():
    print ('\nParticipant Sign Up')
    print ('===================')
    temp_name = input ('Participant Name: ')
    temp_slot = int(input ('Desired Starting slot #[1-%i]: ' %(tournament.total_num)))
    # slot bound check
    if temp_slot > tournament.total_num:
        print ('Error:\nSlot is out of bound!')
    # slot vacancy check
    elif temp_slot not in tournament.slot:
        tournament.name.append(temp_name)
        tournament.slot.append(int(temp_slot))
        print ('Success:\n%s is signed up in starting slot #%i' %(temp_name,temp_slot))
    else: print ('Error:\nSlot #%i is filled.' %(temp_slot))

# cancel sign up
def cancel ():
    print ('\nParticipant Cancellation')
    print ('========================')
    temp_name = input ('Participant Name: ')
    # slot validation
    if temp_name in tournament.name:
        temp_slot = int(input ('Starting slot #[1-%i]: ' %(tournament.total_num)))
        correct_slot = tournament.slot[tournament.name.index(temp_name)]
        if temp_slot == correct_slot:
            print ('Success:\n%s has been cancelled from starting slot #%i' %(temp_name,temp_slot))
        else: 
            print('Error:\n%s is not in that starting slot.\n' %(temp_name))
            #output correct slot for name
            print('Participant name: %s' %(temp_name))
            print('Starting slot #[1-%i]: %i' %(tournament.total_num, correct_slot))
    else: 
        print ('%s is not registered!' %(temp_name))

# view all participants
def view (slot,view_r,view_l):
    #slot = central slot
    #view_r = output # of participants w/ slot # > central slot
    #view_l = '' slot # < central slot
    index_slot = []
    # handle out of bound situation
    if slot - view_l < 1:
        view_l = view_l - (1 - (slot - view_l)) #keep within bound
    # get slot index, use this index to get name
    for i in range(0,view_r+view_l+1):
        try:index_slot.append(tournament.slot.index(slot+i-view_l))
        except ValueError: index_slot.append('empty')
    #loop output result
    for i in range(0,view_r+view_l+1):
        try: _name = tournament.name[int(index_slot[i])]
        except ValueError: _name = '[empty]'
        #return slot-view_l+i, _name
        print ('%i: %s' %(slot-view_l+i,_name))

# load file
def load():
    _input = input('Please enter the file name with extension: \n')
    try: file = open(_input,'r')
    except FileNotFoundError: 
        print ('File not found!')
        load()
    _lines = file.read().splitlines()
    for i in range(1,len(_lines)-1): #-1 as last line stores capacity
        line = _lines[i].split(',')
        tournament.name.append(line[0])
        tournament.slot.append(int(line[1]))
    tournament.total_num = int(_lines[-1].split(',')[1])
    print (tournament.name,tournament.slot,tournament.total_num)
    print ('Sucess: File loaded!')
    file.close()

# save changes
def save ():
    _input = input ('Save your changes to CSV? [y/n]\n').lower()
    if _input == 'y':
        file = open('Tournament.csv','w+')
        file.write(f'name,slot\r\n') #header
        for i in range(0,len(tournament.name)):
            file.write('%s,%i\r\n' % (tournament.name[i],tournament.slot[i])) #data
        file.write('capacity,%i\r\n' %(tournament.total_num)) #endline
        file.close()
        print ('Success:\nChanges are saved to Tournament.csv')
    elif _input == 'n':
        print ('Changes are not saved!')
    else: 
        print ('Please enter [y/n] only!')
        save()
# exit program
def exit ():
    _input = input('Any unsaved changes will be lost.\nAre you sure you want to exit? [y/n]\n').lower()
    if _input == 'y':
        quit()
    elif _input == 'n':
        main()
    else: 
        print ('Please enter [y/n] only!')
        exit()
    
# main menu
def main():
    print ('\nParticipant Menu')
    print ('================')
    print ('1. Sign Up')
    print ('2. Cancel Sign Up')
    print ('3. View Participants')
    print ('4. Load file')
    print ('5. Save Changes')
    print ('6. Exit')
    tournament.menuSelection = int(input ('Please enter your selection number: '))
    # value integrity check
    while tournament.menuSelection > 6 or tournament.menuSelection <= 0:
        print ('Please enter a value between 1 and 5')
        tournament.menuSelection = int(input ('Please enter your selection number: '))
    
    # switch navigation
    if tournament.menuSelection == 1:
        signUp()
        main()
    elif tournament.menuSelection == 2:
        cancel()
        main()
    elif tournament.menuSelection == 3:
        print ('\nView Participants')
        print ('=================')
        _slot = int(input('Starting slot #[1-%i]: ' %(tournament.total_num)))
        # can customize # of participants to be displayed from both left and right
        view(_slot,5,5) 
        main()
    elif tournament.menuSelection == 4:
        print ('\nLoad File')
        print ('=========')
        load()
        main()

    elif tournament.menuSelection == 5:
        print ('\nSave Changes')
        print ('============')
        save()
        main()
    elif tournament.menuSelection == 6:
        print ('\nExit')
        print ('====\n')
        exit()

# intro prompt
print ('Welcome to Tournament Dev 100')
print ('=============================')
print (os.getcwd())

tournament.total_num = input ('Please enter the total number of participants : ')
# value integrity check
while not tournament.total_num.isnumeric():
    errMsg('integer')
    tournament.total_num = input ('Please enter the total number of participants : ')
tournament.total_num = int(tournament.total_num)
print ('There are %i participant slots ready for sign-ups.' % (tournament.total_num))
main()