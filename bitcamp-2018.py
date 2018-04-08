import csv
import sys
import pandas as pd
from pandas.io import sql
import urllib.request
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
from sqlalchemy import Table, Column, Integer, String, ForeignKey


company_list = []

class Company:

    def __init__(self, name):
        self.name = name
        self.rate = 5
        self.values = {}
        # self.record_values = record_values


    def inc_rate(self):
        if self.rate < 10:
            self.rate = self.rate + 1

    def dec_rate(self):
        if self.rate >= 1:
            self.rate = self.rate - 1

    def update_field(self, key, val):
        self.values[key] = val


    def show_rate(self):
        print(self.rate)


with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/water_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'No' in row[6]:
            new_company = Company(row[0])
            new_company.update_field('water policy', 'Yes')
            company_list.append(new_company)
        else:
            new_company = Company(row[0])
            new_company.update_field('water policy', 'No')
            company_list.append(Company(row[0]))

emissions_file = open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/emissions_data.csv', 'r')
with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/emissions_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i, j in enumerate(company_list):
            if j.__dict__['name'] == row[0] and row[7]:
                company_list[i].update_field('emissions', row[7])


with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/forest_data.csv') as f:
    reader = csv.reader(f)
    for i, j in enumerate(company_list):
        if j.__dict__['name'] == row[0] and row[9] != 'No risk':
            company_list[i].update_field('forestry', 'risks present')


company_list.pop(0)

df = pd.DataFrame(company_list)

import sqlalchemy

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('cmudd', 'password', 'bitcamp2018')
print(con)
print(meta)



companies = Table('companies', meta,
    Column('name', String),
    Column('rating', String)
)

companies= {'extend_existing': True}

# Create the above tables
meta.create_all(con)

for i in company_list:
    clause = companies.insert().values(name=company_list[i].name, rating='United Kingdom')
    con.execute(clause)

# cnx = sql.connect(user='cmudd', database='bitcamp-2018', password='1g#ydOjWQHh', host='bitcamp-2018.mysql.database.azure.com')
#cnx = MySQLConnection(user='root', database='bitcamp-2018', password='1g#ydOjWQHh', host='bitcamp-2018.mysql.database.azure.com')


print(list(map(lambda x: x.__dict__, company_list)))
