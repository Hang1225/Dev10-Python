import json
import csv
from functools import reduce
#variable
time = {'dispatchtime':0,'totalresponsetime':0,'totaltime':0}
#function
def importFile():
    with open('Resources/DetroitPoliceReport.csv','r') as file:
        _temp = [{x:y for x,y in x.items()}for x in csv.DictReader(file)]
        return list(filter(lambda x: not not x['zip_code'] and not not x['neighborhood'], _temp))

def calcAverage(input):
    _sum = reduce(lambda x,x1: x+x1, input)
    return '{:.2f}'.format(_sum/len(input))

#part 1
def part1(data):
    for header in list(time.keys()):
        time[header] = list(float(z[header]) for z in data if z[header] != '')
        print(f'Average {header}: {calcAverage(time[header])}')
#part 2
def part2(data):
    temp = {}
    output = []
    neighborhoods = set(z['neighborhood'] for z in data if z['neighborhood'] != '')
    for neighborhood in neighborhoods:
        temp['neighborhood'] = neighborhood
        for header in list(time.keys()):
            temp['average'+ header] = calcAverage(list(float(z[header]) for z in data if z[header] != '' and z['neighborhood'] == neighborhood))
        output.append(temp.copy())

    with open('Data/time.json','w+') as file:
        json.dump(output,file)

#prompt
data = importFile()
part1(data)
part2(data)
