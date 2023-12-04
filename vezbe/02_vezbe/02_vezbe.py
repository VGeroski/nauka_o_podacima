#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:36:17 2023

@author: vladimir
"""

print("Vezbe - Uvod u nauku o podacima");

import pandas as pd;

# ------------------ Ucitavanje podataka ------------------ 
#
# putanja do csv fajla
putanja = 'nba-stats.csv';

# ucitavanje iz csv fajla
df = pd.read_csv(putanja);

# prikazujemo prvih 6 redova
print(df.head(6));

# bez zaglavlja
# df = pd.read_csv(putanja, header = None);

# df = pd.read_csv(putanja, names = ['Pos', 'Age']);

# mozemo da menjamo separator
# df = pd.read_csv(putanja, sep=';');

# ------------------ Cuvanje podataka ------------------ 
# 
# cuvanje u csv
df.to_csv('sacuvano_csv.csv');
df.to_excel('sacuvano_excel.xlsx', sheet_name='Prvi sheet')

# ------------------ Sortiranje podataka ------------------ 
# 
# sortiranje, moze po jednoj ili vise kolona
# podrazumevano je u rastucem redosledu
df.sort_values(by=['Age']);

# rastuci redosled
df.sort_values(by=['Age'],ascending=False)

# sortiramo po dve kolone, ako postoje vise njih sa istim godinama, 
# onda se koristi G tabela  (odnosno ide sortiranje po G koloni)
df.sort_values(by=['Age', 'G'], ascending=[True, False]);

# stampaj prvih 5
print(df.head(5))

# Vecina operacija sa DataFrame-ovima ne menja originalni DataFrame, 
# vec vraca novi. Ukoliko hocemo da menjamo originalni, potrebno je da postavimo
# inplace=true

top_scorers = df.sort_values(['PTS'], ascending = False)
print(top_scorers.head(5))

top_scorers.sort_values(['PTS'], inplace = True)
print(top_scorers.head(5))

# slicno kao head(), tail(5) vraca poslednjih npr 5
print(top_scorers.tail(5))

# ------------------ Deskriptivna statistika ------------------ 
# 
deskriptivna_statistika = df.describe()

print(df['Age'].mode())

print(df['Age'].value_counts())

print(df['Pos'].value_counts())

print(df['Tm'].value_counts())

print(df['Age'].sum())

# ------------------ Filtriranje podataka ------------------ 
# 
# Nazivi kolona u tabeli
print(df.columns)