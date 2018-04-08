import csv
import sys
import numpy as np
import pandas as pd
import urllib.request
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
import mysql

company_list = []

# ge_url  = "https://www.epa.gov/greenpower/green-power-partnership-national-top-100"
# ge_page = urlopen(ge_url)
# soup = BeautifulSoup(ge_page, 'html.parser')

class Company:

    def __init__(self, name):
        self.name = name
        self.rate = 5
        self.values = {}
        # self.record_values = record_values


    def update_field(self, key, val):
        self.values[key] = val


    def show_rate(self):
        print(self.rate)


with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/water_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[6] != 'No':
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
print(list(map(lambda x: x.__dict__, company_list)))
