import requests 
import csv
# US Census API request 
# https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*
# & is used to separate arguments
# ? is where the parameter\arguments begin 
# to enter list of variables enter the name of the variables : comma separated 
# group(B08303)                                               


r = requests.get("https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*")
r2 = requests.get("https://api.census.gov/data/2020/acs/acs5?get=NAME,B01001_001E&for=county:037,039,041&in=state:06")

# Race call 
race = requests.get("https://api.census.gov/data/2020/acs/acs5?get=NAME,group(B03001)&for=state:*")
print(race.text)

x = r.json()
print(x[1])

print(r.json())
print(r2.text)
print(dir(r))


# Writing the csv data from the API request to CSV file
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')
r_json = r.json()

with open('commute_data.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerows(r_json)
