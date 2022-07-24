#!/usr/bin/python
import sqlite3, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, text, inspect
import csv
import pandas as pd



conn = sqlite3.connect('my_data.db') 
c = conn.cursor()

df = pd.read_csv('top250-00-19.csv')
df.to_sql('top250', conn, if_exists='append', index = False)


#c.execute('''
#         SELECT Age, Name FROM top250 LIMIT 3
#          ''')
                     
#conn.commit()

#df = pd.DataFrame(c.fetchall())
#print (df)