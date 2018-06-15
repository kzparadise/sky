#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re
import sqlite3

conn = sqlite3.connect('/home/ubuntu/bot/ast/db-ast.sqlite')
cursor = conn.cursor()

a1 = requests.get("https://m.kolesa.kz/cars/astana/?page=1").text
a2 = requests.get("https://m.kolesa.kz/cars/astana/?page=2").text
urls = [a1, a2]
for url in urls:
    data_parse = BeautifulSoup(url, "lxml")
    tds = data_parse.find_all('div', class_='list-item')
    for td in tds:
        id_data = td.find('a', class_='result').get('href').replace('/a/show/','')      
        sql = "SELECT * FROM cars WHERE id=?"
        id_db = cursor.execute(sql, [id_data]).fetchall()            
        if id_db==[]:
            data = BeautifulSoup(requests.get('https://kolesa.kz/a/show/' + id_data).text, 'lxml')
            try:
                marka_data = data.find('h1', class_='a-title__text').find_all('span', '')[0].text
            except AttributeError:
                marka_data = "пусто"    
            try:    
                model_data = data.find('h1', class_='a-title__text').find_all('span', '')[1].text
            except AttributeError:
                model_data = "пусто"
            try:
                god_data = data.find('h1', class_='a-title__text').find_all('span', '')[2].text
            except AttributeError:
                god_data = "пусто"
            try:
                city = data.find('dd', class_='value clearfix').text
            except AttributeError:
                city = "пусто"
            try:
                procent = data.find('span', class_='kolesa-score-label').text        
            except AttributeError:
                procent = "пусто"
            try:
                cena = data.find('span', class_='a-price__text').text.replace(' ', '').replace('\n', '')
            except AttributeError:
                cena = "пусто"
            views_data = requests.get('https://m.kolesa.kz/ms/views/kolesa/live/' + id_data + '/').json()
            views = views_data["data"][id_data]["nb_views"]           
            link = 'https://m.kolesa.kz/a/show/' + id_data                        
            probel = '%0A'
            telo = marka_data + " " + model_data + " " + god_data + probel + cena + probel + city + probel + procent + probel + "Просмотры - " + str(views) + probel + link
                
            
            if marka_data=="Toyota":
                tima = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=486955668&text=" + telo)
            else:
                pass

        
            
             
            rr = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=318428525&text=" + telo)
            olg = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=351637087&text=" + telo)
            if procent.find("дешевле")==-1:
                pass
            else:
                if int(float(procent.replace('на', '').replace('%', '').replace('дешевле', '').replace(' ', '')))>20:
                    if model_data.find("Camry")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("Patrol")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("Land Cruiser Prado")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("Land Cruiser")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("Avensis")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("X5")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("X6")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 570")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 470")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("Highlander")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if marka_data.find("Rover")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 230")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 240")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 250")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 270")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 280")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 290")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 300")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 320")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 350")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 400")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("LX 500")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 55 AMG")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 63 AMG")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    if model_data.find("G 65 AMG")==-1:
                        pass
                    else:
                        dauren = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=220228483&text=" + telo)
                    
                else:
                    pass
            
            if procent.find("дешевле")==-1:
                pass
            else:
                if int(float(procent.replace('на', '').replace('%', '').replace('дешевле', '').replace(' ', '')))>10:
                    if int(god_data)>2000:
                        ast = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=289789020&text=" + telo)
                    else:
                        pass
                else:
                    pass
            
            if procent.find("дешевле")==-1:
                pass
            else:
                if int(float(procent.replace('на', '').replace('%', '').replace('дешевле', '').replace(' ', '')))>15:
                    if int(god_data)>1995:
                        if int(cena.replace('\xa0', '').replace('₸', ''))>750000:
                            if int(cena.replace('\xa0', '').replace('₸', ''))<2500000:
                                sergei = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=502825828&text=" + telo)
                            else:
                                pass
                        else:
                            pass
                        
                    else:
                        pass
                else:
                    pass
            
            if procent.find("дешевле")==-1:
                pass
            else:
                if int(float(procent.replace('на', '').replace('%', '').replace('дешевле', '').replace(' ', '')))>20:
                    if int(god_data)>2012:
                        aleksandr = requests.post("https://api.telegram.org/bot589971674:AAEm1J2O5QPVL7J0A4p6mChfSWlFfpl0VCQ/sendMessage?chat_id=206928111&text=" + telo)
                    else:
                        pass
                else:
                    pass
        else:
            continue
        cursor.execute("INSERT INTO cars VALUES(?)", [id_data])
        conn.commit() 
conn.close()
