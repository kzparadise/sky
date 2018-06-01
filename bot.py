import requests
import json
from bs4 import BeautifulSoup
import sqlite3
while True:
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    cursor = conn.cursor()
    url = 'https://api.kolesa.kz/app/adverts/search.json?sort_by=storageId=live&catId[0]=2&query[data][region.list]=9&withAdverts=0&limit=200&appId=857066529612&appKey=8aafd56935cbbd3367a46d6fb144f920'
    parsed_json = json.loads(requests.get(url).text)
    urls_id = parsed_json["identifiers"]
    for urls in urls_id:
        sql = "SELECT * FROM cars WHERE id=?"
        id_data=cursor.execute(sql, [str(urls)])
        if id_data.fetchall()==[]:
            data = BeautifulSoup(requests.get('https://m.kolesa.kz/a/show/' + str(urls)).text, 'lxml')
            title = data.find('h1', class_='').text.replace(' ', '').replace('\n', ' ')
            gorod = data.find_all('div', class_='wrap-info clearfix')[1].find_all('div', '')[1].text
            try:
                procent = data.find('span', class_='kolesa-score-label').text
            except AttributeError as e:
                continue
            views_data = requests.get('https://m.kolesa.kz/ms/views/kolesa/live/' + str(urls) + '/').json()
            views = views_data["data"][str(urls)]["nb_views"]
            link = 'https://m.kolesa.kz/a/show/' + str(urls)
            cursor.execute("INSERT INTO cars VALUES(?)", [str(urls)])
            conn.commit()    
            r = requests.post('https://api.telegram.org/bot318428525:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=548542772&text=' + title  + '%0A' + gorod + '%0A' + procent + '%0A' + link) 
        else:
            continue
    conn.close()
