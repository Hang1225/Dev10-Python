from bs4 import BeautifulSoup
import requests
import csv

def getHTML(url):
    try:
        response = requests.get(url)
        return response.text
    except TypeError: 
        return -1

# method 1 - brute force find all attributes then match
def filterHTML(elementType,attributeType, _filter=''):
    title_unfiltered = list(map(lambda x: x.get(attributeType) if x.get(attributeType) != None else _filter, _data.find_all(elementType)))
    return list(filter(lambda x: x != _filter, title_unfiltered))

def exportData(data,header):
    with open('data.csv','w+') as file:
        csv.writer(file).writerow(header)
        for x in data:
            for i in x:
                csv.writer(file).writerow(i)
        file.close()
    return

_sum = []
for i in range(1,51): #50 pages total
    _htmldata = getHTML(f'https://books.toscrape.com/catalogue/page-{i}.html')
    if _htmldata != -1:
        _data = BeautifulSoup(_htmldata,'html.parser')
        # filter title
        _title = filterHTML('a','title')
        # filter rating
        _rating = list(map(lambda x: x[1],list(filter(lambda x: x[0] == 'star-rating',filterHTML('p','class')))))
        # filter price
        _price = list(map(lambda x: x.getText()[2:],_data.find_all('p',class_='price_color')))
        _cleaned = list(zip(_title,_rating,_price))
        _sum.append(_cleaned)
        print(f'retreiving data...on page {i}')
    else: print('Not able to retrieve html data!')
exportData(_sum,['Title','Rating','Price'])
print('data successfully exported.')


    


