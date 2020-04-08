# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import glob
import os
from prettytable import PrettyTable
import matplotlib
import matplotlib.pyplot as plt
import string


plt.rcParams['font.family'] = ['Keraleeyam']

bible_folder ="./bible_txt/"
allData = ""
letters = {}

files = [f for f in glob.glob(bible_folder + "*.txt", recursive=True)]

x = PrettyTable()

x.field_names = ["Letter",  "Count", "Percentage"]

for file in files:
    with open(file) as txt: # Use file to refer to the file object
        data = txt.read()
        allData+= data

allData = allData.strip() #remove whitespaces
allData = allData.translate(str.maketrans('', '', string.punctuation)) #remove punctuation

totalCount = 0

# The Unicode block for Malayalam is U+0D00–U+0D7F:
for letter in allData:
    if u'\u0d00' <= letter <= u'\u0d7f':
        totalCount+=1
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1

sortedLetters = sorted(letters.items(), key=lambda x: x[1], reverse=True)  

names = []
values = []



for letter in sortedLetters:
    percentage = (letter[1]/totalCount)*100
    x.add_row([letter[0], letter[1],percentage])
    names.append(letter[0])
    values.append([letter[1]])

x.add_row(["Total", "",totalCount])

print(x[0])


plt.plot(names, values)
plt.show()

file = open("output2.txt", "w") 
file.write(str(x))
file.close() 
