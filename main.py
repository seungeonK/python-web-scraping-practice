import requests
from bs4 import BeautifulSoup as BS

print('Put some skill that you are not familar with')

unfamiliar_skill = input('>')

print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BS(html_text, 'lxml')

#find(), find_all()
jobs = soup.find_all(
    name='li', 
    class_='clearfix job-bx wht-shd-bx'
)
for job in jobs:
    published_date = job.find(
        name = "span",
        class_ = "sim-posted"
    ).span.text
    
    if 'few' in published_date.lower():
        company_name = job.find(
            name = 'h3',
            class_ = 'joblist-comp-name',
        ).text.replace(' ', '')

        skills = job.find(
            name = 'span',
            class_ = 'srp-skills'
        ).text.replace(' ','')

        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f'Company Name: {company_name.strip()}')
            print(f'Requried Skills: {skills.strip()}')
            print(f'More Info: {more_info}')

            print('')