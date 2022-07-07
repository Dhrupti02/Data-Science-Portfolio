# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:22:56 2022

@author: DHRUPTI PATEL
"""

from flask import Flask, redirect, url_for, request, render_template
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64
import pandas as pd
import sqlite3 as sq

app = Flask(__name__)

# # Load CSV data into Pandas DataFrame
data = pd.read_csv('inf2.csv')

data = data.fillna(data['31-01-2018'].mean())
data.to_csv('inf.csv')

df = pd.read_csv('inf.csv')

city = []
prices = []
states = []
res = []
city_list = []
minm = []
maxm = []

connection = sq.connect('information.db')
 
# # Create a cursor object
curser = connection.cursor()

# Run create table sql query
# curser.execute("create table inf2" \
#               " (RegionID INTEGER PRIMARY KEY AUTOINCREMENT, \
#              	SizeRank INTEGER ,\
#              	RegionName TEXT ,\
#                 RegionType TEXT ,\
#                 StateName TEXT , \
#               '2018-01-31' INTEGER, '2018-02-28' INTEGER , \
#               '2018-03-31' INTEGER , '2018-04-30' INTEGER , \
#               '2018-05-31' INTEGER , '2018-06-30' INTEGER , \
#               '2018-07-31' INTEGER , '2018-08-31' INTEGER , \
#               '2018-09-30' INTEGER , '2018-10-31' INTEGER ,\
#               '2018-11-30' INTEGER , '2018-12-31' INTEGER , \
#               '2019-01-31' INTEGER , '2019-02-28' INTEGER , \
#               '2019-03-31' INTEGER , '2019-04-30' INTEGER , \
#               '2019-05-31' INTEGER , '2019-06-30' INTEGER , \
#               '2019-07-31' INTEGER , '2019-08-31' INTEGER ,\
#               '2019-09-30' INTEGER , '2019-10-31' INTEGER , \
#               '2019-11-30' INTEGER , '2019-12-31' INTEGER ,\
#               '2020-01-31' INTEGER , '2020-02-29' INTEGER ,\
#               '2020-03-31' INTEGER , '2020-04-30' INTEGER , \
#               '2020-05-31' INTEGER , '2020-06-30' INTEGER ,\
#               '2020-07-31' INTEGER , '2020-08-31' INTEGER ,\
#               '2020-09-30' INTEGER , '2020-10-31' INTEGER , \
#               '2020-11-30' INTEGER , '2020-12-31' INTEGER , \
#               '2021-01-31' INTEGER , '2021-02-28' INTEGER ,\
#               '2021-03-31' INTEGER , '2021-04-30' INTEGER ,\
#               '2021-05-31' INTEGER , '2021-06-30' INTEGER , \
#               '2021-07-31' INTEGER , '2021-08-31' INTEGER ,\
#               '2021-09-30' INTEGER , '2021-10-31' INTEGER , \
#               '2021-11-30' INTEGER , '2021-12-31' INTEGER )")
    
# # # Write the data to a sqlite db table
# df.to_sql('inf2', connection, if_exists='replace', index=False)
   
# # Run select sql query
curser.execute('select * from inf2')
 
# Fetch all records
# as list of tuples
records = curser.fetchall()

c = curser.execute('select RegionName from inf2 group by StateName')
for i in c:
    city_list.append(i)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
       choice = request.form['choice']
       if choice == '1':
           for row in records:
               city.append(row[3])
               prices.append(row[6:])
               states.append(row[5])
           res = [sum(ele) / len(prices) for ele in zip(*prices)]
           cities = city[:48]

           city_dict = dict(zip(cities, res))
           
           img1 = BytesIO()
           sort_order = sorted(city_dict.items(), key=lambda x: x[1], reverse=True)
           plt.figure(figsize = (15,8))
           plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
           plt.title("Top contries that won Bronze")
           plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
           plt.xticks(rotation=90)
           plt.savefig(img1, format='png')
           plt.close()
           img1.seek(0)
           plot_url1 = base64.b64encode(img1.getvalue()).decode('utf8')
            
           return render_template('index.html', plot_url=plot_url1)   
       
       elif choice == '2':
            return render_template('index.html',prediction_text=city_list) 
     
       elif choice == '3':
           for i in records:
               ii = i[6:]
               minm.append(min(ii))
           minmm = dict(zip(minm,city))
           return render_template('index.html',minmm=minmm)
       
       elif choice == '4':
           for i in records:
               ii = i[6:]
               maxm.append(max(ii))
           maxmm = dict(zip(maxm,city))
           return render_template('index.html',maxmm=maxmm)
       
       else:
            return "Invalid choice"
        

@app.route('/login',methods = ['POST'])
def login1():
       r_id = request.form['r_id']
       for i in records:
           for j in i:
               if r_id == j:
                 img2 = BytesIO()
                 plt.figure(figsize = (15,8))
                 plt.plot(i[6:])
                 plt.title("Sale prices for the given region id")
                 plt.xticks(rotation=90)
                 plt.savefig(img2, format='png')
                 plt.close()
                 img2.seek(0)
                 plot_url2 = base64.b64encode(img2.getvalue()).decode('utf8')
                 
                 return render_template('index.html', plot_url=plot_url2)   
       
        
if __name__ == '__main__':
   app.run(debug = False)