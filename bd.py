# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:36:27 2019

@author: Rodrigo
"""
import csv
import sqlite3

e = csv.writer(open('output.csv', 'w'))
e.writerow(['cpf','UC'])

conn = sqlite3.connect('enel.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM enel;
""")

for linha in cursor.fetchall():
    e.writerow(linha)
    print(linha)

conn.close()
