import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import sklearn
import timeit
from datetime import datetime 


#Librairie de modules fonctionnelle


"""Charger et afficher un nouveau fichier ".csv"
Snippet qui permet de charger les fichier ".csv"

df      = nom du dataframe de base
path    = l'emplacement du fichier brut '../Source/customers.csv'
delim   = le séparateur

"""
def load_csv_files_as_df(df, path, delim):
    df = pd.read_csv(path, sep=delim)
    return df


"""Afficher des données statistiques de base
Snippet qui permet de charger les statistiques de base pour un dataframe

df      = nom du dataframe ou les statistiques sont souhaité

"""
def statistique_rapide_df(df):
    print(df.shape) 
    print(df.head())  
    print(df.describe())
    print(df.info())  
    return


"""Convertir une colonne dans un df en datetime en ajoutant une nouvelle colonne Timestamp

Snippet qui permet d'ajouter et convertir une colonne d'un df en datetime (Timestamp)

df              = nom du dataframe ou les statistiques sont souhaité
new_col         = nouveau nom de colonne
column_name     = la colonne que l'on souhaite convertir
format          = None

"""
def convert_column_to_datetime(df, new_col, column_name, format=None):
    df
    df[new_col] = pd.to_datetime(df[column_name],format=format, errors='')
    return df


""" génère une colonne d'occurance des valeurs d'un colonnes

Snippet qui permet génère une colonne d'occurance des valeurs d'un colonnes

new_df          = nom du nouveau dataframe ou l'occurance se crée
df              = le dataframe analysé
col             = la colonne que l'on souhaite analyser

"""
def colonne_occurance_valeurs(new_df, df, col):
    new_df = df[[col]].value_counts(normalize=True)
    new_df.to_frame().reset_index(drop=False).sort_values(by='proportion', ascending=False)
    return