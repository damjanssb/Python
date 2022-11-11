# studenti: 'D:\\Programi\\New folder\\Python\\studenti.csv'

import csv

with open('D:\\Programi\\New folder\\Python\\studenti.csv', encoding = 'utf-8') as d:
    tabela = list(csv.reader(d))
    
with open('D:\\Programi\\New folder\\Python\\studenti1.csv', 'w', encoding = 'utf-8', \
          newline = '') as d1:
    w = csv.writer(d1)
    w.writerows(tabela)
        
with open('D:\\Programi\\New folder\\Python\\studenti2.csv', 'w', encoding = 'utf-8', \
          newline = '') as d2:
    w = csv.writer(d2, delimiter=';')
    for red in tabela:
        w.writerow(red)
