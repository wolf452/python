import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job = []
company = []
location = []
description = []


results = requests.get('https://wuzzuf.net/search/jobs?q=DevOps&a=hpb')
content = BeautifulSoup(results.content, 'lxml')

job_title = content.find_all("h2", {"class":"css-193uk2c"})
company_name = content.find_all("a", {"class":"css-ipsyv7"})
locations = content.find_all("span", {"class": "css-16x61xq"})
job_description = content.find_all("a", {"class": "css-5x9pm1"})

for i in range(len(job_title)):
    job.append(job_title[i].text.strip())
    company.append(company_name[i].text.strip())
    location.append(locations[i].text.strip())
    description.append(job_description[i].text.strip())
mylists=[job,company,location,description]
export=zip_longest(*mylists,)
with open('jobs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Job Title", "Company Name", "Location", "Description"])
    writer.writerows(export)

print(job)
print(company)
print(location)
print(description)

