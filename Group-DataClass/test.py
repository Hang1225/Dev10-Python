import requests
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass,field

@dataclass
class races:
    index: str
    name: str
    speed: int
    size: str
    traits: dict
    subraces: dict
    # alignment: str #desc
    # age: str #desc
    # size_desc: str #desc
    # starting_proficiencies: list
    # language: list
    # language_desc: list

    def __str__(self):
        print(f'index: {self.index}')
        print(f'name: {self.name}')
        print(f'speed: {self.speed}')
        print(f'size: {self.size}')
        print(f'traits: {", ".join(self.traits.keys())}')
        print(f'subraces: {", ".join(self.subraces.keys())}')
        return '\r'

#read html data into json
def getJSON(url):
    return requests.get(url).json()

# import races data
def importRaces():
    _races = {}
    _race = {}
    _url_main = 'https://www.dnd5eapi.co'
    _url_sub = '/api/races'
    _json = getJSON(_url_main + _url_sub)
    for x in _json['results']:
        _traits = {}
        _subraces = {}
        #specific detail nested in url
        _temp_dict = getJSON(_url_main + x['url'])
        #subrace list
        for s in _temp_dict['subraces']:
            _subraces[s['name']] = s['index']
        #trait list
        for s in _temp_dict['traits']:
            _traits[s['name']] = s['index']

        _races[x['index']] = races(x['index'],x['name'],_temp_dict['speed'],_temp_dict['size'],_traits,_subraces)
    return _races

listofRaces = _import()
for x in listofRaces:
    print(listofRaces[x])
