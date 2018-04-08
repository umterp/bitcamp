import csv
import sys

#create the list to store companies
company_list = []

class Company:


    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.values = {}

#increment a company's rate (for good env practice)
    def inc_rate(self):
        if self.rate < 10:
            self.rate = self.rate + 1

#decrement rate
    def dec_rate(self):
        if self.rate >= 1:
            self.rate = self.rate - 1

#as we find new env impact data, update the values field to reflect data
    def update_field(self, key, val):
        self.values[key] = val

    def show_rate(self):
        print(self.rate)

    def big_inc(self, num):
        for i in range(1, num):
            self.inc_rate()

    def big_dec(self, num):
        for i in range(1, num):
            self.dec_rate()


# if a company has a water policy, initialize it with a neutral rating
# if it does not, initialize it to 1 less than neutral
with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/water_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'No' in row[6]:
            new_company = Company(row[0], 4)
            new_company.update_field('water policy', 'No')
            company_list.append(new_company)
        else:
            new_company = Company(row[0], 5)
            new_company.update_field('water policy', 'Yes')
            company_list.append(new_company)

#change company's rating based on its emissions rating (assigned by Carbon Disclosure Project)
emissions_file = open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/emissions_data.csv', 'r')
with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/emissions_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i, j in enumerate(company_list):
            if j.__dict__['name'] == row[0] and row[7]:
                if 'A' in row[7]:
                    company_list[i].big_inc(4)
                elif 'B' in row[7]:
                    company_list[i].big_inc(2)
                elif 'C' in row[7]:
                    company_list[i].inc_rate()
                elif 'D' in row[7]:
                    company_list[i].dec_rate()
                else:
                    company_list[i].big_dec(3)
                company_list[i].update_field('emissions', row[7])


# retrieves forestry data i.e. forest risk assessment
with open('/Users/dirtydan/Github/personal-projects/bitcamp-2018/forest_data.csv') as f:
    reader = csv.reader(f)
    for i, j in enumerate(company_list):
        if j.__dict__['name'] == row[0] and row[6]:
            if 'Yes' in row[6]:
                company_list[i].big_dec(2)
            elif 'Partial' in row[6]:
                company_list[i].dec_rate()
            else:
                company_list[i].big_inc(2)


# pop the "organizations" label off the list
company_list.pop(0)


print(list(map(lambda x: x.__dict__, company_list)))
