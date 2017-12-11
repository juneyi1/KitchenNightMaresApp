import pandas as pd
import numpy as np
import csv, sqlite3
from pandas.io import sql
import psycopg2 as pg
from sqlalchemy import create_engine

import pg_credential

c = pg_credential.credential()
HOST = c['host']
DATABASE = c['database']
USER = c['user']
PASSWORD = c['password']

df = pd.read_csv('database.csv')
df.rename(columns={'Claimed?': 'claimed', 'reviews':'review', 'probability':'prediction',
                   'Mon': 'mon', 'Tue': 'tue', 'Wed': 'wed', 'Thu': 'thu', 
                   'Fri': 'fri', 'Sat': 'sat', 'Sun': 'sun', 'Mon1': 'mon1', 
                   'Tue1': 'tue1', 'Wed1': 'wed1', 'Thu1': 'thu1', 'Fri1': 'fri1', 
                   'Sat1': 'sat1', 'Sun1': 'sun1', 'Takes Reservations': 'takes_reservations',
                   'Delivery': 'delivery', 'Take-out': 'take_out', 'Accepts Credit Cards': 'accepts_credit_cards',
                   'Parking': 'parking', 'Good for Kids':'good_for_kids', 
                   'Good for Groups': 'good_for_groups', 'Attire': 'attire',
                   'Noise Level': 'noise_level', 'Alcohol': 'alcohol', 
                   'Outdoor Seating': 'outdoor_seating', 'Has TV': 'hastv', 
                   'Wi-Fi': 'wifi', 'first_review':'first_review_date', 
                   'last_review':'last_review_date'}, inplace=True)
df = df[['yelp_id', 'name', 'claimed', 'ratings', 'ratings_notation', 'review', 'dollar_signs',
         'category', 'prediction', 'address1', 'address2', 'between', 'neighborhood', 
         'phone', 'website','mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun','mon1', 
         'tue1', 'wed1','thu1', 'fri1', 'sat1', 'sun1', 'takes_reservations', 'delivery',
         'take_out','accepts_credit_cards', 'parking', 'good_for_kids', 'good_for_groups', 
         'attire', 'noise_level', 'alcohol', 'outdoor_seating', 'wifi', 'hastv', 
         'first_review_date', 'last_review_date', 'permanently_closed']].copy()
df['review'] = df['review'].astype(int)
df['website'] = df['website'].apply(lambda x: x.replace('http://','').replace('www.','') if type(x)==str else x)
empty = ['dollar_signs', 'category', 'address1', 'between','neighborhood', 'phone', 'website']
df[empty] = df[empty].fillna('')
NA = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 
      'mon1', 'tue1', 'wed1','thu1', 'fri1', 'sat1', 'sun1', 
      'takes_reservations', 'delivery','take_out','accepts_credit_cards', 
      'parking', 'good_for_kids', 'good_for_groups', 'attire', 'noise_level', 
      'alcohol', 'outdoor_seating', 'wifi', 'hastv',]
df[NA] = df[NA].fillna('N/A')
df.reset_index(inplace=True)
df['id'] = df['index'] + 1
df.drop(['index'], inplace=True, axis=1)

postgresql = 'postgresql://' + USER + ':' + PASSWORD + '@' + HOST + ':' + '5432/' + DATABASE
engine = create_engine(postgresql)
df.to_sql(name ='restaurants_restaurant', con=engine, if_exists='replace', index=False)
