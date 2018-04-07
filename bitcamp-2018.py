import csv
import sys
import urllib.request
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup


ge_url  = "https://www.epa.gov/greenpower/green-power-partnership-national-top-100"

ge_page = urlopen(ge_url)
soup = BeautifulSoup(ge_page, 'html.parser')


water_file = open('/Users/Documents/bitcamp_data/water_data.csv', "rb")
emissions_file = open('/Users/Documents/bitcamp_data/emissions_data.csv', "rb")
forest_file = open('/Users/Documents/bitcamp_data/forest_data.csv', "rb")

class ParentCompany:

    def __init__(self, id, rate, record_values):
        self.id = id
        self.rate = rate
        if not hasattr(self, record_values):
            record_values = {}
        self.record_values = {**self.record_values, **record_values}

    def show_rate(self):
        print(self.rate)


class Company(ParentCompany):

    def __init__(self, id, rate, parent_company):
        ParentCompany.__init__(self, id, rate, {"Parent Company": parent_company})
