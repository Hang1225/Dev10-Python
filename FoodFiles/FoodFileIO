import os 
import json
#variable declaration
_dir = os.getcwd() + '/Resources'
_header = ['foods','highfiber','low-glycemic-index','lowfat']
dict = {'foods':[],'highFiber':[],'lowGlycemicIndex':[],'lowFat':[]}

#function
def importFiles():
    _data = []
    for i in _header:
        file = open(_dir + '/' + i + '.txt','r')
        _list = file.read().splitlines()
        #empty check
        for n in range(1,len(_list)):
            _list[n] = _list[n].lower().strip()
            #check empty str, true if empty
            if not _list[n]:
                # insert error indicator to be deleted in cleaning process
                _list[n] = '*ERR'
            # yes or no integrity check
            if i != 'foods' and not validate(_list[n]):
                _list[n] = '*ERR'

        _data.append(_list)
    return _data

def validate(input):
    if input.lower() == 'yes' or input.lower() == 'no':
        return True
    return False

def dataCleaning(input): 

    for i in range(0,len(input)):
        # remove corrupted data
        indices = [i for i, x in enumerate(input[i]) if x == '*ERR']
        for x in range(len(indices)):
            # remove from all sets
            for v in range(0,4):
                input[v].pop(indices[x]-x) #pop reduces total # of elements, 
    
        # capitalize data
        input[i] = [n.capitalize() for n in input[i]]

        #custom cleaning
        if i == 0:
            input[i] = [f.replace('Sriacha','Siracha') for f in input[i]]
            input[i] =[f.replace('Salmon2','Salmon') for f in input[i]]

    return input

# convert 'yes' 'no' to boolean, must be validated first!
def strBool(input):
    return True if input.lower().strip() == 'yes' else False

def createDict(data):
    temp = []
    for i in range(1,len(data[0])):
        dict['foods']= data[0][i]
        dict['highFiber'] = data[1][i]
        dict['lowGlycemicIndex'] = data[2][i]
        dict['lowFat'] = data[3][i]
        temp.append(dict.copy())
    return temp

def importJson():
    with open('Data/data.json','r') as file:
        return json.loads(file.read())
        
#prompt

# part 1 
data = importFiles()
dataCleaning(data)
dict = createDict(data)
#write to file
with open("Data/data.json", "w+") as outfile:
    json.dump(dict, outfile)

# part 2
dict = importJson()
_count = 0
healthyfood = []
for x in dict:
    if strBool(x['highFiber']) and strBool(x['lowGlycemicIndex']) and strBool(x['lowFat']): 
        _count += 1
        healthyfood.append(x['foods'])

print('Number of high fiber, low glycemic, and low fat foods: %i, percentage: %s %%' %(_count,'{:.2f}'.format(_count/len(dict)*100)))
for x in healthyfood:
    print(f'{x} is a recommended food.')
