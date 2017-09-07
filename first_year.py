# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 16:15:52 2017

@author: Wycliffe
"""
import json

import csv

#reading the file data into a variable
with open('first_years.txt', 'r') as myfile:
    data = myfile.read()
 
print(data)  # Have a look at how the json data looks like    

freshas_parsed = json.loads(data)
fresha_data = freshas_parsed['message']  #the key for the array of all the json objects

# open a file for writing
freshas_data = open('First Years Data - Copy', 'w') # in this directory

# create the csv writer object
csvwriter = csv.writer(freshas_data)

count = 0


for fresha in fresha_data:
    if count == 0:
        header = fresha.keys()
        csvwriter.writerow(header)
        #count += 1
        
    csvwriter.writerow(fresha.values())
    
freshas_data.close()

