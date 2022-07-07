# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:18:03 2022

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

app = Flask(__name__)

rows = []
gender = []
year = []
country = []
medals = []
bronze_city = []
silver_city = []
gold_city = []
year_2012 = []
            
frequency = {}

with open("summer.csv", 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
        
    for row in csvreader:
            rows.append(row)
            gender.append(row[6])
            year.append(row[0])
            country.append(row[5])
            medals.append(row[-1])

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
  
@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      choice = request.form['choice']
      if choice == '1':
          max_madels = max(set(country), key = country.count)
          return render_template('index.html',prediction_text="{} has the highest medals".format(max_madels))    
      
      elif choice == '2':
          for item in gender:
              if item in frequency:
                frequency[item] += 1
              else:
                frequency[item] = 1
          
          # mylabels = ["Males", "Females"]
          img = BytesIO()
          plt.pie(frequency.values(), labels=frequency.keys())
          plt.savefig(img, format='png')
          plt.close()
          img.seek(0)
          plot_url = base64.b64encode(img.getvalue()).decode('utf8')

          return render_template('index.html', plot_url=plot_url)
          

          
      elif choice == '3':
          for item in rows:
              if item[0] == '2008':
                  city = item[1]
          
          return render_template('index.html',prediction_text="Olympic in 2008 held in {}".format(city))    
          

      elif choice == '4':
          for item in rows:
              if item[1] == 'Mexico' and item[6] == 'Women' and item[8] == 'Silver':
                  women = item[4]

          return render_template('index.html',prediction_text="{} won women silver in Mexico".format(women))    
          

      elif choice == '5':
          for item in year:
              if item in frequency:
                frequency[item] += 1
              else:
                frequency[item] = 1
          prizes = frequency.get('2012')
          return render_template('index.html',prediction_text="Total {} prizes awarded in 2012".format(prizes))    
      
      elif choice == '6':
          for item in rows:
              if item[8] == 'Bronze':
                      bronze_city.append(item[5])
              
          for item in bronze_city:
              if item in frequency:
                  frequency[item] += 1
              else:
                  frequency[item] = 1
                  
          img1 = BytesIO()
          sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
          sort_order = sort_orders[0:5]
          plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
          plt.title("Top contries that won Bronze")
          plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
          plt.xticks(rotation=70)
          plt.savefig(img1, format='png')
          plt.close()
          img1.seek(0)
          plot_url1 = base64.b64encode(img1.getvalue()).decode('utf8')

          return render_template('index.html', plot_url=plot_url1)
      
      elif choice == '7':
          for item in rows:
              if item[8] == 'Silver':
                      silver_city.append(item[5])
              
          for item in silver_city:
              if item in frequency:
                  frequency[item] += 1
              else:
                  frequency[item] = 1

          sort_orders1 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
          sort_order1 = sort_orders1[0:5]
          
          img2 = BytesIO()
          plt.bar(range(len(sort_order1)), [val[1] for val in sort_order1], align='center')
          plt.title("Top contries that won Silver")
          plt.xticks(range(len(sort_order1)), [val[0] for val in sort_order1])
          plt.xticks(rotation=70)
          plt.savefig(img2, format='png')
          plt.close()
          img2.seek(0)
          plot_url2 = base64.b64encode(img2.getvalue()).decode('utf8')

          return render_template('index.html', plot_url=plot_url2)
          
      elif choice == '8':
          for item in rows:
              if item[8] == 'Gold':
                      gold_city.append(item[5])
              
          for item in gold_city:
              if item in frequency:
                  frequency[item] += 1
              else:
                  frequency[item] = 1

          sort_orders2 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
          sort_order2 = sort_orders2[0:5]
          
          img3 = BytesIO()
          plt.bar(range(len(sort_order2)), [val[1] for val in sort_order2], align='center')
          plt.title("Top contries that won Gold")
          plt.xticks(range(len(sort_order2)), [val[0] for val in sort_order2])
          plt.xticks(rotation=70)
          plt.savefig(img3, format='png')
          plt.close()
          img3.seek(0)
          plot_url3 = base64.b64encode(img3.getvalue()).decode('utf8')

          return render_template('index.html', plot_url=plot_url3)
          
      elif choice == '9':
          for item in rows:
              if item[0] == '2012':
                      year_2012.append(item[5])
              
          for item in year_2012:
              if item in frequency:
                  frequency[item] += 1
              else:
                  frequency[item] = 1

          sort_orders3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
          sort_order3 = sort_orders3[0:5]
          
          img4 = BytesIO()
          plt.bar(range(len(sort_order3)), [val[1] for val in sort_order3], align='center')
          plt.title("Top contries that won medal in the year 2012")
          plt.xticks(range(len(sort_order3)), [val[0] for val in sort_order3])
          plt.xticks(rotation=70)
          plt.savefig(img4, format='png')
          plt.close()
          img4.seek(0)
          plot_url4 = base64.b64encode(img4.getvalue()).decode('utf8')

          return render_template('index.html', plot_url=plot_url4)
         
      else:
          return "Invalid choice"
   
  
if __name__ == '__main__':
   app.run(debug = False)