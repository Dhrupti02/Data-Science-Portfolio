# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:32:02 2022

@author: DHRUPTI PATEL
"""

import time
import csv
import matplotlib.pyplot as plt
import numpy as np

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

print("1. Which country has the highest medals?")
print("2. How many females and males have played?")
print("3. Where was olampyic held in 2008?")
print("4. Who won women silver in Mexico?")
print("5. How many prizes awarded in 2012?")
print("6. Find top N countries for bronze")
print("7. Find top N countries for silver")
print("8. Find top N countries for gold")
print("9. Find top N countries in the year 2012")


with open("summer.csv", 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
        
    for row in csvreader:
            rows.append(row)
            gender.append(row[6])
            year.append(row[0])
            country.append(row[5])
            medals.append(row[-1])
          
while True:
    question = input("Enter question you want to ask(* for exit): ")
    
    if question == '1':
        print(max(set(country), key = country.count))
    
    
    elif question == '2':
        for item in gender:
            if item in frequency:
              frequency[item] += 1
            else:
              frequency[item] = 1
        
        # mylabels = ["Males", "Females"]

        plt.pie(frequency.values(), labels=frequency.keys())
        plt.show()

        
    elif question == '3':
        for item in rows:
            if item[0] == '2008':
                city = item[1]
        print(city)
        

    elif question == '4':
        for item in rows:
            if item[1] == 'Mexico' and item[6] == 'Women' and item[8] == 'Silver':
                women = item[4]
        print(women)
        

    elif question == '5':
        for item in year:
            if item in frequency:
              frequency[item] += 1
            else:
              frequency[item] = 1
        print(frequency.get('2012'))
    
    elif question == '6':
        for item in rows:
            if item[8] == 'Bronze':
                    bronze_city.append(item[5])
            
        for item in bronze_city:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        sort_order = sort_orders[0:5]
        plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
        plt.title("Top contries that won Bronze")
        plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
        plt.xticks(rotation=70)
        plt.show()
    
    elif question == '7':
        for item in rows:
            if item[8] == 'Silver':
                    silver_city.append(item[5])
            
        for item in silver_city:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        sort_order = sort_orders[0:5]
        plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
        plt.title("Top contries that won Silver")
        plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
        plt.xticks(rotation=70)
        plt.show()
        
    elif question == '8':
        for item in rows:
            if item[8] == 'Gold':
                    gold_city.append(item[5])
            
        for item in gold_city:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        sort_order = sort_orders[0:5]
        plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
        plt.title("Top contries that won Gold")
        plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
        plt.xticks(rotation=70)
        plt.show()
        
    elif question == '9':
        for item in rows:
            if item[0] == '2012':
                    year_2012.append(item[5])
            
        for item in year_2012:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        sort_orders = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        sort_order = sort_orders[0:5]
        plt.bar(range(len(sort_order)), [val[1] for val in sort_order], align='center')
        plt.title("Top contries that won medal in the year 2012")
        plt.xticks(range(len(sort_order)), [val[0] for val in sort_order])
        plt.xticks(rotation=70)
        plt.show()
    
    elif question == '*':
        print("Thank you!")
        break
    
    else:
        print("Invalid choice.")